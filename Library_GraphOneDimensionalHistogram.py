"""
ARGS :

    ObservedDataset:
        The observed points
        == [point1, point2, ... , pointN]
        Used for scatter presentation
        In this case, each point is only 1 dimension

    Xlabel: ...
    Ylabel: ...
    PlotTitle: ...

RETURNS:
    The plot object. 
    Can be futher modified outside the scope of this function

"""
import matplotlib
import matplotlib.pylab as plt
import matplotlib.patches as mpatches
import numpy 
#------------------------------------------------------------------------------
import Type_NumpyTwoDimensionalDataset


def Main(                   
    ObservedDataset = None,         

    BinCount = 50, 
    BinSize = None,

    BinMin = None,
    BinMax = None,
    Weights = None, 
    Normed = False,
    NormalizationFactor = None,
    NormalizeToBinWidths = False,

    LogCounts = False,
    LogX = False,
    IncludeIntegral = False, 
    Xlabel = None, 
    Ylabel = None, 
    PlotTitle = None,

    CheckArguments = True,  
    PrintExtra = False,     
    SaveFigureFilePath = None,
    ):

    if (CheckArguments):
        ArgumentErrorMessage = ""
        if ( Type_NumpyTwoDimensionalDataset.Main(ObservedDataset) != True ):
            ArgumentErrorMessage += "( Type_NumpyTwoDimensionalDataset.Main(ObservedDataset) != True )"  + "\n"
        if (ObservedDataset != None and ObservedDataset.shape[1] != 1 ):
            ArgumentErrorMessage += "ObservedDataset.shape[1] != 1"
        if (len(ArgumentErrorMessage) > 0 ):
            if (PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    if (BinMin == None):
        xmin = numpy.min(ObservedDataset)
    else:
        xmin = BinMin

    if (BinMax == None):
        xmax = numpy.max(ObservedDataset)
    else:
        xmax = BinMax

    if (PrintExtra):
        print 'xmin', xmin
        print 'xmax', xmax

    xrng = xmax - xmin

    #NormalizationFactor = 1
    if (NormalizeToBinWidths):
        DatasetRange = xmax - xmin
        BinWidth = DatasetRange / BinCount
        NormalizationFactor = (1.0/BinWidth)


    if (NormalizationFactor != None):
        Weights = numpy.atleast_2d( numpy.ones( len(ObservedDataset)  ) * NormalizationFactor ).T
        if (PrintExtra):
            print 'Weights.shape', Weights.shape

    if (BinSize != None):
        BinCount = float(xrng) / float(BinSize)

    HistogramBarColor = 'g'
    Counts, BinEdges, Patches = plt.hist(
        ObservedDataset, 
        weights = Weights, 
        bins = BinCount, 
        normed=Normed,  #This is different than the LogX way of doing things -> bins change edges 
        log=LogCounts, 
        facecolor= HistogramBarColor, 
        alpha=.5,
        label = Xlabel,
        range = (xmin, xmax),
        )
    plt.grid(True)
    #HistogramLegendPiece = mpatches.Patch(color=HistogramBarColor, label=Xlabel)

    IntegralHistogramBarColor = 'b'

    if (IncludeIntegral):   
        Integral_n_minusInfToX = []
        TotalSeen = 0
        for value in Counts:
            TotalSeen += value
            Integral_n_minusInfToX.append(TotalSeen) 

        matplotlib.pyplot.bar(\
            left = BinEdges[:-1], \
            width = xrng/BinCount, \
            height = Integral_n_minusInfToX, \
            alpha=0.25 ,\
            label = 'Integral(Count('+ Xlabel + ')) From -Inf to X'  \
            ) 

    #IntegralHistogramLegendPiece = mpatches.Patch(\
    #    color=IntegralHistogramBarColor, label = 'Integral' + Xlabel )

    #Add some labels:
    #plt.legend(handles=[HistogramLegendPiece, IntegralHistogramLegendPiece])
    plt.legend(loc = 'upper left')




        
    if (LogX): #THIS WORKS!!!
        plt.gca().set_xscale('log')


    if (Xlabel != None):
        plt.xlabel(Xlabel)

    if (Ylabel != None):
        plt.ylabel(Ylabel)

    if (PlotTitle != None):
        plt.title(PlotTitle)
    
    if (SaveFigureFilePath != None):
        plt.savefig( SaveFigureFilePath )

    return Counts, BinEdges, Patches




