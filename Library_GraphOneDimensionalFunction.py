
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

import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import numpy
#------------------------------------------------------------------------------
import Type_NumpyTwoDimensionalDataset
def Main(\
    Functions = None,       \
    DomainMinimumPoint = None,       \
    DomainMaximumPoint = None,       \
    ObservedDataset = None,         \
    ShowObservedDataset = True, \
    Xlabel = None, \
    Ylabel = None, \
    PlotTitle = None,\
    CheckArguments = True,  \
    PrintExtra = False,     \
    SaveFigureFilePath = None,\
    ):

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

    for Function in Functions:
        Values = []
        for Point in Points:
            #print "Point", Point
            Value = Function(Point)
            Values.append(Value)

        plt.plot(Points,  Values)

    plt.grid(True)

    #Add lables:
    if (Xlabel != None):
        plt.xlabel(Xlabel)
    if (Ylabel != None):
        plt.ylabel(Ylabel)
    if (PlotTitle != None):
        plt.title(PlotTitle)

    if (SaveFigureFilePath != None):
        plt.savefig( SaveFigureFilePath )

    return plt






