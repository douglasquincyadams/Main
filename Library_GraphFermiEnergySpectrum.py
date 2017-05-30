"""
DESCRIPTION:

    Kind of a one-off file to be used by fermi analysis papers 


ARGS:

RETURNS
"""
import warnings
import os
import matplotlib
import matplotlib.pyplot
import numpy
import pprint
import scipy
import scipy.spatial as spatial
import scipy.optimize as optimize

#import scipy.optimize.curve_fit
#------------------------------------------------------------------------------
import Library_DatasetGetMaximumDatapoint
import Library_DatasetGetMinimumDatapoint
import Library_DateStringNowGMT
import Library_EvaluateFunctionsAtNumpyDataPoints
import Library_GeneratePolynomial
import Library_GraphOneDimensionalHistogram
import Library_GraphSkyMap
import Library_LeastSquaresLinearFindCoefficients
import Library_PrintDatasetStatistics

import Library_MaximizeLikelihoodFunction
import Library_ModelFunctionToLikelihoodFunction
import Library_LikelihoodFunctionToDeltaLogLikelihoodFunction
import Library_DigitClock
import Library_Poisson



def Main(
    DirectoryGeneratedGraphs = None,
    PhotonEnergiesNotFromPointSourcesFromGalaxyGroups = None,
    PhotonLocationsNotFromPointSourcesFromGalaxyGroups = None,
    CheckArguments = True, 
    ):

    #ARGS Cannot be null
    if (CheckArguments):
        ArgumentErrorMessage = ""
        if (DirectoryGeneratedGraphs == None):
            ArgumentErrorMessage += 'DirectoryGeneratedGraphs == None'
        if (PhotonEnergiesNotFromPointSourcesFromGalaxyGroups == None):
            ArgumentErrorMessage += 'PhotonEnergiesNotFromPointSourcesFromGalaxyGroups == None'
        if (PhotonLocationsNotFromPointSourcesFromGalaxyGroups == None):
            ArgumentErrorMessage += 'PhotonLocationsNotFromPointSourcesFromGalaxyGroups == None'
        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    print '\n\nBegining To Make Graphs...\n\n'


    #Take some log10's for graphing purposes:
    Log10PhotonEnergiesNotFromPointSourcesFromGalaxyGroups = numpy.log10(PhotonEnergiesNotFromPointSourcesFromGalaxyGroups)
    #Library_PrintDatasetStatistics.Main(Log10PhotonEnergiesNotFromPointSourcesFromGalaxyGroups, 'Log10PhotonEnergiesNotFromPointSourcesFromGalaxyGroups', 1)

    #Setup the directories
    DirectoryGeneratedGraphsCurrentRun = DirectoryGeneratedGraphs + "/" + Library_DateStringNowGMT.Main()
    if not os.path.exists(DirectoryGeneratedGraphsCurrentRun):
        os.makedirs(DirectoryGeneratedGraphsCurrentRun)
    GraphFileNamePrefix = Library_DateStringNowGMT.Main()[0:11]

    #size the graphs
    #   Default to common monitor size:  
    #   1920pixels by 1080 pixels
    print 'Sizing the graphs...'
    Inch_in_Pixels = 80.0
    MonitorSize = (1920.0/Inch_in_Pixels,1080.0/Inch_in_Pixels)


    #sky map
    print '\nMaking the sky map'
    Library_GraphSkyMap.Main(
        Longitudes                  = PhotonLocationsNotFromPointSourcesFromGalaxyGroups[:,0] , #Lon
        Latitudes                   = PhotonLocationsNotFromPointSourcesFromGalaxyGroups[:,1] , #Lat
        Zvalues                     = Log10PhotonEnergiesNotFromPointSourcesFromGalaxyGroups,
        Zlabel                      = 'Log10PhotonEnergiesNotFromPointSourcesFromGalaxyGroups',
        Projection                  = "Mollweide",
        SaveFigureFilePath          = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'PhotonLocationsNotFromPointSourcesFromGalaxyGroups.png'\
        )

    
    #Plot Energy Spectrum Simple Histogram (no scaling)
    print 'Plotting the Energy Spectrum'
    SpectrumSaveFilePathPlain = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'PhotonEnergiesNotFromPointSourcesFromGalaxyGroups.png'
    fig = matplotlib.pyplot.figure(figsize=MonitorSize)

    Counts, BinEdges, Patches = Library_GraphOneDimensionalHistogram.Main(\
        ObservedDataset     = numpy.atleast_2d( PhotonEnergiesNotFromPointSourcesFromGalaxyGroups ).T,
        IncludeIntegral     = False, 
        BinCount            = 100,
        LogCounts           = False,
        Xlabel              = 'Log10PhotonEnergies',
        Ylabel              = 'Log10Count',
        PlotTitle           = 'ENERGY', 
        SaveFigureFilePath  = SpectrumSaveFilePathPlain,
        )
    """
    #Extract information from the histogram bins for fitting:
    Library_PrintDatasetStatistics.Main(Counts, 'Counts', 1)
    Library_PrintDatasetStatistics.Main(BinEdges, 'BinEdges', 1)

    Log10Counts = numpy.log10(Counts)
    Library_PrintDatasetStatistics.Main(Log10Counts, 'Log10Counts', 1)

    #Find the midpoints of each of the bins to associate with the counts
    BinMidPoints = []
    BinCount = len(BinEdges) - 1
    k = 0
    while (k < BinCount ):
        BinMidPoints.append((BinEdges[k] + BinEdges[k + 1])/2)
        k = k + 1
    BinMidPoints = numpy.array(BinMidPoints)
    Library_PrintDatasetStatistics.Main(BinMidPoints, 'BinMidPoints', 1)


    #Describe the energies and counts in terms datasets
    #Energies = BinMidPoints
    #Library_PrintDatasetStatistics.Main(Energies, 'Energies', 1)

    #EnergiesDataset = numpy.atleast_2d(Energies).T
    #Library_PrintDatasetStatistics.Main(EnergiesDataset, 'EnergiesDataset', 1)

    #Log10EnergiesDataset = numpy.log10(EnergiesDataset)
    #Library_PrintDatasetStatistics.Main(Log10EnergiesDataset, 'Log10EnergiesDataset', 1)

    #Dataset = numpy.vstack((Energies,  Counts)).T
    #Library_PrintDatasetStatistics.Main(Dataset, 'Dataset', 1)
    """
























