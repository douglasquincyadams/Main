
"""
Description:
    A simple wrapper around "Library_GraphOneDimensionalFunction"
    Which can be called on a dataset without any thought or effort
"""


import Library_GraphOneDimensionalFunction
import Library_KernelDensityEstimation

def Main(
    DomainMinimumPoint = None,       
    DomainMaximumPoint = None,       
    ObservedDataset = None,         
    Xlabel = None, 
    Ylabel = None, 
    PlotTitle = None,
    CheckArguments = True,  
    PrintExtra = False,     
    SaveFigureFilePath = None,
    ):


    #Make a kernel to model the data:
    KernelDensityFunction = lambda(Point): Library_KernelDensityEstimation.Main( \
        Point = Point,\
        Dataset = ObservedDataset,\
        PrintExtra = False\
        )

    #Graph the Kernel Density Estimation:
    Library_GraphOneDimensionalFunction.Main(\
        Functions = [KernelDensityFunction] ,\
        DomainMinimumPoint = DomainMinimumPoint,       \
        DomainMaximumPoint = DomainMaximumPoint,       \
        ObservedDataset = ObservedDataset,         \
        Xlabel = Xlabel, \
        Ylabel = Ylabel, \
        PlotTitle = PlotTitle,\
        CheckArguments = CheckArguments,  \
        PrintExtra = PrintExtra,     \
        SaveFigureFilePath = SaveFigureFilePath,\
        )
