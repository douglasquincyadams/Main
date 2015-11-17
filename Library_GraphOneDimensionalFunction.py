
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
    Xlabel = None, 
    Ylabel = None, 
    PlotTitle = None,
    CheckArguments = True,  
    PrintExtra = False,     
    SaveFigureFilePath = None,
    ):


    try:
        font = {
            'weight' : 'bold',
            'size'   : 22 
            }

        matplotlib.rc('font', **font)
    except:
        pass


    if (CheckArguments):
        ArgumentErrorMessage = ""
        if (Functions == None):
            ArgumentErrorMessage += "(Functions == None)\n"
        if (ObservedDataset != None and ObservedDataset.shape[1] != 1 ):
            ArgumentErrorMessage += "ObservedDataset.shape[1] != 1"
    

        if (Type_NumpyTwoDimensionalDataset.Main(ObservedDataset) != True ):
            if (DomainMaximumPoint == None or DomainMinimumPoint == None ):
                ArgumentErrorMessage += "(Type_NumpyTwoDimensionalDataset.Main(ObservedDataset) != True)\n"
                if (ObservedDataset == None):
                    ArgumentErrorMessage += "(Dataset == None)\n"
                if (DomainMinimumPoint  == None):
                    ArgumentErrorMessage += "(DomainMinimumPoint  == None)\n"
                if (DomainMaximumPoint  == None):
                    ArgumentErrorMessage += "(DomainMaximumPoint  == None)\n"

        if (len(ArgumentErrorMessage) > 0 ):

            print "ObservedDataset.shape", ObservedDataset.shape
            print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    #If a dataset was passed, try to infer the plot minimums and maximums:
    if (DomainMinimumPoint  == None):
        DomainMinimumPoint  = numpy.nanmin(ObservedDataset, axis = 0)
    if (DomainMaximumPoint  == None):
        DomainMaximumPoint  = numpy.nanmax(ObservedDataset, axis = 0) 

    if (ObservedDataset != None and ShowObservedDataset == True):
        plt.plot(ObservedDataset, numpy.zeros(ObservedDataset.shape), 'k+', markersize = 100)


    if (PrintExtra):
        print "DomainMinimumPoint ", DomainMinimumPoint 
        print "DomainMaximumPoint ", DomainMaximumPoint 

    Step = (DomainMaximumPoint  - DomainMinimumPoint )/100.0
    Points = numpy.atleast_2d( np.arange(DomainMinimumPoint , DomainMaximumPoint , Step) ).T

    if (FunctionLabels == None):
        FunctionLabels = [None]*len(Functions)
    FunctionIndexes = range(len(Functions))

    #Reorder functions and labels to have the main function first
    if (MainFunctionIndex != None):
        if (MainFunctionOrderRatioRequirement == None):
            MainFunctionOrderRatioRequirement = numpy.inf
        if (MainFunctionDifferenceRequirement == None):
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
        Values = []
        for (Point, PointIndex) in zip(Points, range(len(Points))):
            #print "Point", Point
            Point = numpy.array( [float(Point) ] ) 
            Value = numpy.nan
            try:
                Value = Function( Point )
            except:
                pass    
        
            Value = numpy.float64(Value)
            ValueNotNan = not numpy.isnan(Value)

            #If We are restricting the graph to show things near the main function, set other values to nans
            if (FunctionIndex != MainFunctionIndex and MainFunctionIndex != None and ValueNotNan ):
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

        if (FunctionIndex == MainFunctionIndex):
            MainFunctionValues = Values

        plt.plot(Points,  Values, label = FunctionLabel)

    plt.grid(True)

    #Add lables:
    if (Xlabel != None):
        plt.xlabel(Xlabel)
    if (Ylabel != None):
        plt.ylabel(Ylabel)
    if (PlotTitle != None):
        plt.title(PlotTitle)
    if (not None in FunctionLabels):
        plt.legend(loc = 'best')

    if (SaveFigureFilePath != None):
        SaveFigureFilePath = os.path.realpath(SaveFigureFilePath)
        if (not Library_StringFileNameLastExtension.Main(SaveFigureFilePath) in ['png', '.jpg'] ):
            SaveFigureFilePath += '.png'
        plt.savefig( SaveFigureFilePath )




    return plt






