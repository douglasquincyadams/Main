"""
DESCRIPTION:
    Graphs the data extracted from fermi fits file

"""

from astropy.cosmology import FlatLambdaCDM
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt
import numpy
import collections
import os

#------------------------------------------------------------------------------
import Const_LocalDirectoriesFermiFiles
import Library_DateStringNowGMT

import Library_GraphOneDimensionalHistogram
import Library_GraphOneDimensionalFunction
#import Library_GraphTwoDimensionDensityColorMap
import Library_GraphOneDimensionalKernelDensity


def Main(
    EventsNumpyArray = None, 
#    EventsColumnNames = None, 
    DirectoryGeneratedGraphs = None, 
    PrintExtra = False, 
    ):

    #DIRECTORY DEFINING
    DirectoryGeneratedGraphsCurrentRun = DirectoryGeneratedGraphs + "/" + Library_DateStringNowGMT.Main()
    if not os.path.exists(DirectoryGeneratedGraphsCurrentRun):
        os.makedirs(DirectoryGeneratedGraphsCurrentRun)

    #DATA SLICING
    print 'EventsNumpyArray.shape', EventsNumpyArray.shape
    NumPoints = EventsNumpyArray.shape[0]

    EventEnergies = EventsNumpyArray["ENERGY"]
    EventGalacticLongitudes = EventsNumpyArray["L"]
    EventGalacticLatitudes = EventsNumpyArray["B"]

    Log10EventEnergies = numpy.log10(EventEnergies)
    Log10Log10EventEnergies = numpy.log10(Log10EventEnergies)
    Log10Log10Log10EventEnergies = numpy.log10(Log10Log10EventEnergies)

    #GRAPH FILENAME PREPARATION:
    GraphFileNamePrefix = Library_DateStringNowGMT.Main()[0:11]

    #GRAPH IMAGE SIZING:
    #   Default to common monitor size:  
    #   1920pixels by 1080 pixels
    Inch_in_Pixels = 80.0
    MonitorSize = (1920.0/Inch_in_Pixels,1080.0/Inch_in_Pixels)

    #ENERGY PLOT
    fig = plt.figure(figsize=MonitorSize)
    Library_GraphOneDimensionalHistogram.Main(\
        ObservedDataset = numpy.atleast_2d(Log10EventEnergies).T,\
        IncludeIntegral = False, \
        BinCount = 100,\
        LogCounts = True,\
        Xlabel = 'Log10EventEnergies',\
        Ylabel = 'Count',\
        PlotTitle = 'ENERGY', \
        SaveFigureFilePath = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10EventEnergies.png'\
        )

    #LATITUDE, LONGITUDE, Log10Log10Log10ENERGIES 2D
    fig = plt.figure(figsize=MonitorSize)
    subplot = fig.add_subplot(111)

    scatter = subplot.scatter(\
        EventGalacticLongitudes - 180.0, \
        EventGalacticLatitudes, \
        marker= 'o', \
        s = 1, \
        c = Log10Log10Log10EventEnergies, \
        edgecolors='none'\
        )

    subplot.set_xlabel('EventGalacticLongitudes')
    subplot.set_ylabel('EventGalacticLatitudes')
    fig.colorbar( scatter, label = 'Log10Log10Log10EventEnergies' ) 
    plt.grid(True)
    plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'GalacticLongitude_GalacticLatitude_Log10Log10Log10EventEnergies_All.png' )

    #LATITUDE, LONGITUDE, Log10Log10Log10ENERGIES 3D
    """
    fig = plt.figure(figsize=MonitorSize)
    subplot = fig.add_subplot(111, projection='3d')
    scatter = subplot.scatter(\
        EventGalacticLongitudes, \
        EventGalacticLatitudes, \
        Log10Log10Log10EventEnergies, \
        marker= 'o', \
        s = 2, \
        c = Log10Log10Log10EventEnergies, \
        edgecolors='none'\
        )
    fig.colorbar( scatter, label = 'Log10Log10Log10EventEnergies' ) 
    subplot.set_xlabel('EventGalacticLongitudes')
    subplot.set_ylabel('EventGalacticLatitudes')
    subplot.set_zlabel('Log10Log10Log10EventEnergies')
    #plt.draw()
    plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10Masses_Log10Distances_Log10Log10Log10EventEnergies_3D.png' )
    plt.grid(True)
    """

    #MANY GRAPH PLOTS BY ENERGY BINS:  
    #   LATITUDE, LONGITUDE, ENERGIES 2D
    DirectoryGeneratedGraphsCurrentRunBinnedEnergies = DirectoryGeneratedGraphsCurrentRun + "/BinnedEnergies"
    if not os.path.exists(DirectoryGeneratedGraphsCurrentRunBinnedEnergies):
        os.makedirs(DirectoryGeneratedGraphsCurrentRunBinnedEnergies)

    NumEnergyBins = 10
    MinEnergy = numpy.min(EventEnergies)
    MaxEnergy = numpy.max(EventEnergies)

    EnergyBinEdges = numpy.linspace(MinEnergy, MaxEnergy, NumEnergyBins+1 )

    CurrentEnergyBin = 0 
    k = 0
    while (k < NumEnergyBins):
        SingleEnergyBinMin = EnergyBinEdges[k]
        SingleEnergyBinMax = EnergyBinEdges[k + 1]
        #SingleEnergyBinMax = 1000000 #-> If Cumulative
        EnergyBinDataset = EventsNumpyArray[numpy.where( \
            (EventsNumpyArray['ENERGY'] < SingleEnergyBinMax) \
            & (SingleEnergyBinMin < EventsNumpyArray['ENERGY']) \
            )]
        EnergyBinDatasetEnergies = EnergyBinDataset["ENERGY"]
        EnergyBinDatasetGalacticLongitudes = EnergyBinDataset["L"]
        EnergyBinDatasetGalacticLatitudes = EnergyBinDataset["B"]

        NumPoints = EnergyBinDataset.shape[0]

        print 'BIN #', k
        print 'SingleEnergyBinMin', SingleEnergyBinMin
        print 'SingleEnergyBinMax', SingleEnergyBinMax
        print 'NumPoints', NumPoints

        if (NumPoints > 0 ):


            fig = plt.figure(figsize=MonitorSize)
            subplot = fig.add_subplot(111)

            scatter = subplot.scatter(\
                EnergyBinDatasetGalacticLongitudes - 180.0, \
                EnergyBinDatasetGalacticLatitudes, \
                marker= 'o', \
                s = 4000.0/numpy.sqrt(NumPoints), \
                c = EnergyBinDatasetEnergies, \
                edgecolors='none'\
                )

            subplot.set_xlabel('EnergyBinDatasetGalacticLongitudes')
            subplot.set_ylabel('EnergyBinDatasetGalacticLatitudes')
            fig.colorbar( scatter, label = 'EnergyBinDatasetEnergies' ) 
            plt.grid(True)

            BinRangeSaveSuffix = '_min' + str(SingleEnergyBinMin) + '_max' + str( SingleEnergyBinMax )
            EnergyBinSavePlotFilename = 'GalacticLongitude_GalacticLatitude_EnergyBinDatasetEnergies' + BinRangeSaveSuffix + '.png' 
            plt.savefig( DirectoryGeneratedGraphsCurrentRunBinnedEnergies + '/' + GraphFileNamePrefix + EnergyBinSavePlotFilename )
        else:
            print "NumPoints <=0 ... not saving fig"
        k = k + 1


    #Close all open figures
    matplotlib.pyplot.close("all")





