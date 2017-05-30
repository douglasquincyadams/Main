"""
DESCRIPTION:
    Makes graphs of galaxy cluster data

ARGS:
    ClusterData:
        Type: `Type_TwoDimensionalNumpyArray`
        Description: Contains all the data we need about Galaxy clusters to make graphs
            
    ClusterDataColumnNames
        Type: Python List
        Description: 
            [
            "GalaxyCount"
            "VelocityInCmPerSec"
            "MassInGrams"
            "GalacticLongitudeInDegrees"
            "GalacticLatitudeInDegrees"
            "DistanceInCm"
            "Jsmooth"
            "RvirInCm"
            "VisualAngleInDegrees"           #-> assumes that the sun is in the same place as the fermi telescope
            "IntensityInJPerDegreesSquared"
            "Jclumpy"
            ]

    

RETURNS:
    None
"""
from astropy.cosmology import FlatLambdaCDM
from mpl_toolkits.mplot3d import Axes3D

import matplotlib
import matplotlib.pyplot
import matplotlib.pyplot as plt

import numpy
import collections
import os
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Ellipse
#------------------------------------------------------------------------------
import Const_LocalDirectoriesGalaxyGroupsFiles

import Config_AstronomyConstants as astroconst

import Library_DateStringNowGMT
import Library_GraphOneDimensionalHistogram
import Library_GraphOneDimensionalFunction

import Library_GraphOneDimensionalKernelDensity
import Library_PrintDatasetStatistics
import Library_GraphSkyMap

#def MakeClusterGraphs(ClusterData = None, ClusterDataColumnNames = None, PrintExtra = False):

def Main(
    ClusterData = None, 
    ClusterDataColumnNames = None, 
    DatasetNames = [],
    DirectoryGeneratedGraphs = None, 
    PrintExtra = False
    ):

    #DIRECTORY DEFINING
    DirectoryDatasetNamesSuffix = "_".join(DatasetNames)
    DirectoryGeneratedGraphsCurrentRun = DirectoryGeneratedGraphs  + "/" + Library_DateStringNowGMT.Main() + "_" + DirectoryDatasetNamesSuffix
    if not os.path.exists(DirectoryGeneratedGraphsCurrentRun):
        os.makedirs(DirectoryGeneratedGraphsCurrentRun)
    GraphFileNamePrefix = Library_DateStringNowGMT.Main()[0:11]
    
    print "Preparing to make graphs..."

    #Graph image sizing: 
    #   Default to common monitor size:  
    #   1920pixels by 1080 pixels
    Inch_in_Pixels = 80.0
    MonitorSize = (1920.0/Inch_in_Pixels,1080.0/Inch_in_Pixels)




    #Numpy2Ds:
    NumberGroups = len( ClusterData )
    Jsmooths = ClusterData[:,[ClusterDataColumnNames.index("Jsmooth")] ]

    #LOG10s
    Log10Masses_in_SolarMasses      = numpy.log10(ClusterData[:,[ClusterDataColumnNames.index("MassInGrams")] ] / astroconst.MassSolar_in_grams)
    Log10Distances_in_MegaParsecs   = numpy.log10(ClusterData[:,[ClusterDataColumnNames.index("DistanceInCm")] ] / astroconst.MegaParsec_in_cm )
    Log10VisualAngles_in_degrees    = numpy.log10(ClusterData[:,[ClusterDataColumnNames.index("VisualAngleInDegrees")] ])
    Log10Jsmooths                   = numpy.log10(ClusterData[:,[ClusterDataColumnNames.index("Jsmooth")] ])
    Log10GalaxyCounts               = numpy.log10(ClusterData[:,[ClusterDataColumnNames.index("GalaxyCount")] ])

    #LOG10s 1D
    Log10Masses_in_SolarMasses_1D       = Log10Masses_in_SolarMasses.T[0]
    Log10Distances_in_MegaParsecs_1D    = Log10Distances_in_MegaParsecs.T[0]
    Log10VisualAngles_in_degrees_1D     = Log10VisualAngles_in_degrees.T[0]
    Log10Jsmooths_1D                    = Log10Jsmooths.T[0]

    #1D
    VisualAngles_in_degrees_1D          = ClusterData[:,[ClusterDataColumnNames.index("VisualAngleInDegrees")] ].T[0]
    Intensity_JperDegreesSquared_1D     = ClusterData[:,[ClusterDataColumnNames.index("IntensityInJPerDegreesSquared")] ].T[0]
    GalaxyCounts_1D                     = ClusterData[:,[ClusterDataColumnNames.index("GalaxyCount")] ].T[0]
    Log10GalaxyCounts_1D                = Log10GalaxyCounts.T[0]
    GalacticLongitude_in_degrees_1D     = ClusterData[:,[ClusterDataColumnNames.index("GalacticLongitudeInDegrees")] ].T[0]
    GalacticLatitude_in_degrees_1D      = ClusterData[:,[ClusterDataColumnNames.index("GalacticLatitudeInDegrees")] ].T[0]    
    Jsmooths_1D                         = Jsmooths.T[0]
    print "Making Graphs..."


    Library_PrintDatasetStatistics.Main( VisualAngles_in_degrees_1D, 'VisualAngles_in_degrees_1D', 1 )

    #SKY PLOT
    #plt.show()

    Shapes = []
    
    for k in range(NumberGroups):
        GroupLat = GalacticLatitude_in_degrees_1D[k]
        GroupLon = GalacticLongitude_in_degrees_1D[k] - 180. 
        GroupRadius = VisualAngles_in_degrees_1D[k]
        #print 'GroupRadius', GroupRadius
        GroupCircle = Ellipse(xy = (GroupLon, GroupLat) , width=GroupRadius, height=GroupRadius, angle=0)
        Shapes.append(GroupCircle)


    Library_GraphSkyMap.Main(
    #    Latitudes                   = None ,
    #    Longitudes                  = None ,
        Zvalues                     = Log10Jsmooths_1D ,
        Zlabel                      = "Log10DarkMatterDensity"    ,
        Shapes                      = Shapes ,
        Projection                  = "Rectangle" ,
    #    DirectoryGeneratedGraphs    = None ,
        SaveFigureFilePath          = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'RectangularGroupsBadRadii.png',
    #    DatasetNames                = [] ,
    )


    Library_GraphSkyMap.Main(
        Latitudes                   = GalacticLatitude_in_degrees_1D ,
        Longitudes                  = GalacticLongitude_in_degrees_1D ,
        Zvalues                     = Log10Jsmooths_1D ,
    #    Zlabel                      = ""    ,
    #    Shapes                      = Shapes ,
        Projection                  = "Mollweide" ,
    #    DirectoryGeneratedGraphs    = None ,
        SaveFigureFilePath          = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'MollweideGroupCenters.png',
    #    DatasetNames                = [] ,
    )



    #MASS PLOT:
    plt.figure(figsize=MonitorSize)
    Library_GraphOneDimensionalHistogram.Main(\
        ObservedDataset = Log10Masses_in_SolarMasses,\
        IncludeIntegral = True, \
        Xlabel = 'Log10Masses_in_SolarMasses',\
        Ylabel = 'Count',\
        PlotTitle = 'MASS', \
        SaveFigureFilePath = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10Masses_Count.png'\
        )

    plt.figure(figsize=MonitorSize)
    Library_GraphOneDimensionalHistogram.Main(\
        ObservedDataset = Log10Masses_in_SolarMasses, \
        Weights = Jsmooths,\
        IncludeIntegral = True, \
        Xlabel = 'Log10Masses_in_SolarMasses',\
        Ylabel = 'Count * Jsmooth',\
        PlotTitle = 'MASS', \
        SaveFigureFilePath = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10Masses_CountTimesJsmooth.png'\
        )
    
    #DISTANCE PLOT
    plt.figure(figsize=MonitorSize)
    Library_GraphOneDimensionalHistogram.Main(\
        ObservedDataset = Log10Distances_in_MegaParsecs,\
        IncludeIntegral = True, \
        Xlabel = 'Log10Distances_in_MegaParsecs',\
        Ylabel = 'Count',\
        PlotTitle = 'DISTANCE', \
        SaveFigureFilePath = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10Distances_Count.png'\
        )

    plt.figure(figsize=MonitorSize)
    Library_GraphOneDimensionalHistogram.Main(\
        ObservedDataset = Log10Distances_in_MegaParsecs, \
        Weights = Jsmooths,\
        IncludeIntegral = True, \
        Xlabel = 'Log10Distances_in_MegaParsecs',\
        Ylabel = 'Count * Jsmooth',\
        PlotTitle = 'DISTANCE', \
        SaveFigureFilePath = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10Distances_CountTimesJsmooth.png'\
        )

    #VISUALANGLE PLOT    ----
    plt.figure(figsize=MonitorSize)
    Library_GraphOneDimensionalHistogram.Main(\
        ObservedDataset = Log10VisualAngles_in_degrees,\
        IncludeIntegral = True, \
        Xlabel = 'Log10VisualAngles_in_degrees',\
        Ylabel = 'Count',\
        PlotTitle = 'VisualAngles', \
        SaveFigureFilePath = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10VisualAngles_Count.png'\
        )

    plt.figure(figsize=MonitorSize)
    Library_GraphOneDimensionalHistogram.Main(\
        ObservedDataset = Log10VisualAngles_in_degrees, \
        Weights = Jsmooths,\
        IncludeIntegral = True, \
        Xlabel = 'Log10VisualAngles_in_degrees',\
        Ylabel = 'Count * Jsmooth',\
        PlotTitle = 'VisualAngles', \
        SaveFigureFilePath = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10VisualAngles_CountTimesJsmooth.png'\
        )

    #JSMOOTH PLOT:
    plt.figure(figsize=MonitorSize)
    Library_GraphOneDimensionalHistogram.Main(\
        ObservedDataset = Log10Jsmooths,\
        IncludeIntegral = True, \
        Xlabel = 'Log10Jsmooths',\
        Ylabel = 'Count', \
        PlotTitle = 'JSMOOTH', \
        SaveFigureFilePath = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10Jsmooths_Count.png'\
        )

    plt.figure(figsize=MonitorSize)
    Library_GraphOneDimensionalHistogram.Main(\
        ObservedDataset = Log10Jsmooths,\
        Weights = Jsmooths,\
        IncludeIntegral = True, \
        Xlabel = 'Log10(Jsmooth)',\
        Ylabel = 'Count * Jsmooth', \
        PlotTitle = 'JSMOOTH', \
        SaveFigureFilePath = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10Jsmooths_CountTimesJsmooth.png'\
        )

    #GALAXYCOUNT VS. MASS:
    fig = plt.figure(figsize=MonitorSize)
    subplot = fig.add_subplot(111)
    subplot.plot(Log10GalaxyCounts_1D, Log10Masses_in_SolarMasses_1D,  'k+', markersize=2)
    subplot.set_xlabel('Log10GalaxyCounts_1D')
    subplot.set_ylabel('log10(Masses_in_SolarMasses)')
    subplot.set_title('GALAXYCOUNT VS. MASS')
    plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'LOG10GALAXYCOUNT_MASS.png' )

    #JSMOOTH VS. MASS
    fig = plt.figure(figsize=MonitorSize)
    subplot = fig.add_subplot(111)
    subplot.plot(Log10Jsmooths_1D, Log10Masses_in_SolarMasses_1D, 'k.', markersize=1.0)
    subplot.set_xlabel('log10(Jsmooths)')
    subplot.set_ylabel('log10(Masses_in_SolarMasses)')
    subplot.set_title('JSMOOTH VS. MASS')
    plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'JSMOOTH_MASS.png' )

    #JSMOOTH VS. DISTANCE:
    fig = plt.figure(figsize=MonitorSize)
    subplot = fig.add_subplot(111)
    subplot.plot(Log10Jsmooths_1D, Log10Distances_in_MegaParsecs_1D, 'k.', markersize=1.0)
    subplot.set_xlabel('log10(Jsmooths)')
    subplot.set_ylabel('log10(Distances_in_MegaParsecs)')
    subplot.set_title('JSMOOTH VS. DISTANCE')
    plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'JSMOOTH_DISTANCE.png' )

    #JSMOOTH VS. VISUALANGLE:
    fig = plt.figure(figsize=MonitorSize)
    subplot = fig.add_subplot(111)
    subplot.plot( VisualAngles_in_degrees_1D, Log10Jsmooths_1D, 'k.', markersize=10)
    subplot.set_xlabel('VisualAngles_in_degrees')
    subplot.set_ylabel('log10(Jsmooths)')
    subplot.set_title('JSMOOTH VS. VISUAL_ANGLE')
    plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'JSMOOTH_VISUALANGLE.png' )

    #JSMOOTH VS. INTENSITY:
    fig = plt.figure(figsize=MonitorSize)
    subplot = fig.add_subplot(111)
    subplot.plot( Log10Jsmooths_1D, Intensity_JperDegreesSquared_1D, 'k.', markersize=10)
    subplot.set_xlabel('log10(Jsmooths)')
    subplot.set_ylabel('Intensity_JperDegreesSquared_1D')
    subplot.set_title('JSMOOTH VS. JSMOOTHINTENSITY')
    plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'JSMOOTH_JSMOOTHINTENSITY.png' )
    
    #MASS VS. DISTANCE:
    fig = plt.figure(figsize=MonitorSize)
    subplot = fig.add_subplot(111)
    subplot.plot(Log10Masses_in_SolarMasses_1D, Log10Distances_in_MegaParsecs_1D, 'k.', markersize=1.0)
    subplot.set_xlabel('log10(Masses_in_SolarMasses)')
    subplot.set_ylabel('log10(Distances_in_MegaParsecs)')
    subplot.set_title('MASS VS. DISTANCE')
    plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'MASS_DISTANCE.png' )
   
    #MASS VS DISTANCE VS JSMOOTH 2D + Color:
    fig = plt.figure(figsize=MonitorSize)
    subplot = fig.add_subplot(111)
    scatter = subplot.scatter(\
        Log10Masses_in_SolarMasses_1D, \
        Log10Distances_in_MegaParsecs_1D, \

        marker= 'o', \
        s = 10.0, \
        c = Log10Jsmooths_1D, \
        edgecolors='none'\
        )
    subplot.set_xlabel('Log10Masses_in_SolarMasses')
    subplot.set_ylabel('Log10Distances_in_MegaParsecs')
    fig.colorbar( scatter, label = 'Log10Jsmooths' ) 
    plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10Masses_Log10Distances_Log10Jsmooths_2D.png' )

    #GALAXYCOUNT VS. MASS VS. JSMOOTH 2D + Color:
    fig = plt.figure(figsize=MonitorSize)
    subplot = fig.add_subplot(111)
    scatter = subplot.scatter(\
        GalaxyCounts_1D, \
        Log10Masses_in_SolarMasses_1D, \

        marker= 'o', \
        s = 10.0, \
        c = Log10Jsmooths_1D, \
        edgecolors='none'\
        )
    subplot.set_xlabel('GalaxyCounts')
    subplot.set_ylabel('Log10Masses_in_SolarMasses')
    fig.colorbar( scatter, label = 'Log10Jsmooths' ) 
    plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'GalaxyCounts_Log10Masses_Log10Jsmooths_2D.png' )

    #MASS VS DISTANCE VS JSMOOTHINTENSITY
    fig = plt.figure(figsize=MonitorSize)
    subplot = fig.add_subplot(111)
    scatter = subplot.scatter(\
        Log10Masses_in_SolarMasses_1D, \
        Log10Distances_in_MegaParsecs_1D, \

        marker= 'o', \
        s = 10.0, \
        c = Intensity_JperDegreesSquared_1D, \
        edgecolors='none'\
        )
    subplot.set_xlabel('Log10Masses_in_SolarMasses')
    subplot.set_ylabel('Log10Distances_in_MegaParsecs')
    fig.colorbar( scatter, label = 'Intensity_JperDegreesSquared_1D' ) 
    plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10Masses_Log10Distances_JsmoothIntensity_2D.png' )

    #MASS VS DISTANCE VS VISUALANGLE VS JSMOOTH 3D:
    fig = plt.figure(figsize=MonitorSize)
    subplot = fig.add_subplot(111, projection='3d')
    scatter = subplot.scatter(\
        Log10Masses_in_SolarMasses_1D, \
        Log10Distances_in_MegaParsecs_1D, \
        numpy.sqrt(VisualAngles_in_degrees_1D), \

        marker= 'o', \
        s = 10, \
        c = Intensity_JperDegreesSquared_1D, \
        edgecolors='none'\
        )
    fig.colorbar( scatter , label = 'Intensity_JperDegreesSquared_1D') 
    subplot.set_xlabel('Log10Masses_in_SolarMasses')
    subplot.set_ylabel('Log10Distances_in_MegaParsecs')
    subplot.set_zlabel('VisualAngles_in_degrees_1D')
    plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10Masses_Log10Distances_VisualAngles_Intensity_3D.png' )

    #MASS VS DISTANCE VS JSMOOTH 3D:
    fig = plt.figure(figsize=MonitorSize)
    subplot = fig.add_subplot(111, projection='3d')
    scatter = subplot.scatter(\
        Log10Masses_in_SolarMasses_1D, \
        Log10Distances_in_MegaParsecs_1D, \
        Log10Jsmooths_1D, \
        marker= 'o', \
        s = .5, \
        c = Log10Jsmooths, \
        edgecolors='none'\
        )
    fig.colorbar( scatter ) 
    subplot.set_xlabel('Log10Masses_in_SolarMasses')
    subplot.set_ylabel('Log10Distances_in_MegaParsecs')
    subplot.set_zlabel('Log10Jsmooths')
    plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10Masses_Log10Distances_Log10Jsmooths_3D.png' )
    
    #Show all the plots (off by default):
    #plt.show()

    #Close all open figures
    matplotlib.pyplot.close("all")




























