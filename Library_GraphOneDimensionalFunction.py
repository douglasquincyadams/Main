
"""
@author: Adams, Douglas

DESCRIPTION:
    Used to graph arbitrary functions of one variable
    (There is really nothing complicated going on here)
    Also has the capability of throwing the scatter plot in the background of the line graphs
    Matplotlib Compatability:
        fig = plt.figure() 
            NOT included in the function.
            Instead infers that an existing fig must exist
        plt.draw()
            NOT included int he function
            fig can be added to after this function runs

ARGS:
    Functions:
        Array of python functions
        == [Function1, Function2, ..., FunctionN]
        FunctionK (where: 1 <= K <= N):
            Designed to 
            ARGS (1Count):
                Point:
                    == [x1] -> where x1 is a number on the Real Number line
                    
            FunctionK(x) = y
    
    DomainMinimumPoint:
        used for plot boundaries
        numpy array of two values:
            [x_min, y_min]

    DomainMaximumPoint:
        used for plot boundaries
        numpy array of two values:
            [x_max, y_max]

    ObservedDataset:
        The observed points
        == [point1, point2, ... , pointN]
        Used for scatter presentation
        In this case, each points is only 1 dimension

RETURNS:
    The plot object. 
    Can be futher modified outside the scope of this function


"""
import datetime
import os
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import numpy
#------------------------------------------------------------------------------
import Library_OrderOfMagnitudeRatioSmallCheck
import Library_HardDifferenceSmallCheck
import Type_NumpyTwoDimensionalDataset
import Library_ArraySwapTwoElements
import Library_StringFileNameLastExtension
import Library_PrintExceptionObject

def Main(
    Functions = None, 
    FunctionLabels = None,      
    DomainMinimumPoint = None,       
    DomainMaximumPoint = None,       
    MainFunctionIndex = None,
    MainFunctionOrderRatioRequirement = None,
    MainFunctionDifferenceRequirement = None,
    ObservedDataset = None,         
    ShowObservedDataset = True, 
    LogDomain = False, 
    LogRange = False,
    PrintTimeExecution = False,
    Xlabel = None, 
    Ylabel = None, 
    PlotTitle = None,
    CheckArguments = True,  
    DomainPointCount = 1000,
    PrintExtra = False,     
    SaveFigureFilePath = None,
    ):

    #FORMATTING:
    #Fix font
    try:
        font = {
            'weight' : 'bold',
            'size'   : 22 
            }

        matplotlib.rc('font', **font)
    except:
        pass

    DomainPointCount = float(DomainPointCount)

    if (CheckArguments):
        ArgumentErrorMessage = ""
        if (Functions is None):
            ArgumentErrorMessage += "(Functions is None)\n"
        if (ObservedDataset is not None and ObservedDataset.shape[1] != 1 ):
            ArgumentErrorMessage += "ObservedDataset.shape[1] != 1"
        if FunctionLabels is not None and len(FunctionLabels) != len(Functions):
            ArgumentErrorMessage += "len(FunctionLabels) !=  len(Functions)\n"
            

        if (Type_NumpyTwoDimensionalDataset.Main(ObservedDataset) != True ):
            if (DomainMaximumPoint is None or DomainMinimumPoint is None ):
                ArgumentErrorMessage += "(Type_NumpyTwoDimensionalDataset.Main(ObservedDataset) != True)\n"
                if (ObservedDataset is None):
                    ArgumentErrorMessage += "(Dataset is None)\n"
                if (DomainMinimumPoint  is None):
                    ArgumentErrorMessage += "(DomainMinimumPoint  is None)\n"
                if (DomainMaximumPoint  is None):
                    ArgumentErrorMessage += "(DomainMaximumPoint  is None)\n"

        if (len(ArgumentErrorMessage) > 0 ):

            print "ObservedDataset.shape", ObservedDataset.shape
            print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    #If a dataset was passed, try to infer the plot minimums and maximums:
    if (DomainMinimumPoint  is None):
        DomainMinimumPoint  = numpy.nanmin(ObservedDataset, axis = 0)
    if (DomainMaximumPoint  is None):
        DomainMaximumPoint  = numpy.nanmax(ObservedDataset, axis = 0) 

    if (ObservedDataset is not None and ShowObservedDataset == True):
        plt.plot(ObservedDataset, numpy.zeros(ObservedDataset.shape), 'k+', markersize = 100)

    if (PrintExtra):
        print "DomainMinimumPoint ", DomainMinimumPoint 
        print "DomainMaximumPoint ", DomainMaximumPoint 

    Step = (DomainMaximumPoint  - DomainMinimumPoint )/DomainPointCount
    Points = numpy.atleast_2d( np.arange(DomainMinimumPoint , DomainMaximumPoint , Step) ).T

    if (FunctionLabels is None):
        FunctionLabels = [None]*len(Functions)
    FunctionIndexes = range(len(Functions))

    #Reorder functions and labels to have the main function first
    if (MainFunctionIndex is not None):
        if (MainFunctionOrderRatioRequirement is None):
            MainFunctionOrderRatioRequirement = numpy.inf
        if (MainFunctionDifferenceRequirement is None):
            MainFunctionDifferenceRequirement = numpy.inf
        Functions = Library_ArraySwapTwoElements.Main(
            Array = Functions,
            Index1 = 0,
            Index2 = MainFunctionIndex,
            )
        FunctionLabels = Library_ArraySwapTwoElements.Main(
            Array = FunctionLabels,
            Index1 = 0,
            Index2 = MainFunctionIndex,
            )
        MainFunctionIndex = 0 

    MainFunctionValues = []
    for (Function, FunctionLabel, FunctionIndex) in zip(Functions, FunctionLabels, FunctionIndexes):
        #print 'FunctionIndex', FunctionIndex

        StartTime = datetime.datetime.utcnow()

        Values = []
        for (Point, PointIndex) in zip(Points, range(len(Points))):
            #print "Point", Point
            Point = numpy.array( [float(Point) ] ) 
            Value = numpy.nan
            try:
                Value = Function( Point )
            except Exception as ExceptionObject:
                print 'Failed to plot Point == ', str(Point)    
                Library_PrintExceptionObject.Main(ExceptionObject)
               

            Value = numpy.float64(Value)
            ValueNotNan = not numpy.isnan(Value)

            #If We are restricting the graph to show things near the main function, set other values to nans
            if (FunctionIndex != MainFunctionIndex and MainFunctionIndex is not None and ValueNotNan ):
                #print 'MainFunctionIndex', MainFunctionIndex
                MainFunctionValue = MainFunctionValues[PointIndex]
                MainFunctionOrderOfMagnitudeRatioSmallCheck = Library_OrderOfMagnitudeRatioSmallCheck.Main( 
                    Value, 
                    MainFunctionValue, 
                    MainFunctionOrderRatioRequirement ,
                    PrintExtra = False,
                    )

                MainFunctionHardDifferenceSmallCheck = Library_HardDifferenceSmallCheck.Main( 
                    Value, 
                    MainFunctionValue, 
                    MainFunctionDifferenceRequirement ,
                    PrintExtra = False,
                    )

                if ( not MainFunctionOrderOfMagnitudeRatioSmallCheck or not MainFunctionHardDifferenceSmallCheck):
                    Value = numpy.nan

            Values.append(Value)

        EndTime = datetime.datetime.utcnow()
        if (PrintTimeExecution):
            print FunctionLabel, ' TimeExecution: ', EndTime - StartTime

        if (FunctionIndex == MainFunctionIndex):
            MainFunctionValues = Values

        if (LogDomain):
            pass
        if (LogRange):
            Values = numpy.log(Values)
    
            

        plt.plot(Points,  Values, label = FunctionLabel)

    plt.grid(True)

    #Add lables:
    if (Xlabel is not None):
        plt.xlabel(Xlabel)
    if (Ylabel is not None):
        plt.ylabel(Ylabel)
    if (PlotTitle is not None):
        plt.title(PlotTitle)
    if (not None in FunctionLabels):
        plt.legend(loc = 'best')

    if (SaveFigureFilePath is not None):
        SaveFigureFilePath = os.path.realpath(SaveFigureFilePath)
        if (not Library_StringFileNameLastExtension.Main(SaveFigureFilePath) in ['png', '.jpg'] ):
            SaveFigureFilePath += '.png'
        plt.savefig( SaveFigureFilePath )




    return plt






