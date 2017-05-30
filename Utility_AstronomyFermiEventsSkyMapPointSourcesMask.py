"""
DESCRIPTION:
    Graphs a sky map of all the fermi events which are NOT from point sources
    Takes a naive approach and collects all events which are within 1 angular degree of a given point souce
    
    Possible Improvements:
        Calculate the point sources to be elipses based on their errors
        Calculate the radius of inclusion based on photon energy (error goes down with higher energy)


"""
import pyfits
import astropy
import scipy
from scipy import spatial
import numpy
import datetime
import os
import matplotlib
import matplotlib.pyplot
#------------------------------------------------------------------------------
import Const_LocalDirectoriesFermiFiles
import Const_LocalDirectoriesGalaxyGroupsFiles

import Library_DateStringNowGMT
import Library_DataGetFermiEvents
import Library_GraphSkyMap
import Library_MemoryLimit
import Library_PrintDatasetStatistics
import Library_GraphOneDimensionalHistogram
import Library_GeometrySphericalToCartesianCoordinates
#SET MEMORY LIMIT TO N-GIGABYTES (Avoid Crashing Computer):
Library_MemoryLimit.Main(Bytes = 4*1000000000) 

pi = numpy.pi
#EVENTS
#extract
EventsDataSourceFilename = 'filtered_events_10GeV_1TeV_zmax100_GTI_ultraclean.fits'
EventsDirectorySourceDataFile = Const_LocalDirectoriesFermiFiles.DataFilesCutsDirectory + '/' + EventsDataSourceFilename
EventsNumpyArray, EventsColumnNames = Library_DataGetFermiEvents.Main(\
    Filepath = EventsDirectorySourceDataFile,\
    PrintExtra = False,\
    )
EventsCount = len(EventsNumpyArray)

#Event Locations
EventGalacticLongitudes = EventsNumpyArray["L"]
EventGalacticLatitudes = EventsNumpyArray["B"]
FermiEventLocations = numpy.vstack((EventGalacticLongitudes, EventGalacticLatitudes) ).T #[Longitude, Latitude]
Library_PrintDatasetStatistics.Main(FermiEventLocations, "FermiEventLocations", 1)

#Event Locations 3d projected coordinates on unit sphere:
FermiEventLocations3DTupleTranspose = \
    Library_GeometrySphericalToCartesianCoordinates.Main(
        Radius          = numpy.ones(shape = (EventsCount,)),
        Inclination     = EventGalacticLatitudes * pi/180  + pi/2,  #needs to be in radians and transformed from latitude to inclination
        Azimuth         = EventGalacticLongitudes * pi/180,         #needs to be in radians
    )
FermiEventLocations3D = numpy.array( FermiEventLocations3DTupleTranspose ).T #This is a 3D cartesian `Type_TwoDimensionalNumpyDataset`
Library_PrintDatasetStatistics.Main( FermiEventLocations3D , 'FermiEventLocations3D', 1)
####FermiEventLocations3D.shape:
#   FermiEventLocationsX = numpy.array(FermiEventLocations3DTranspose)[0]
#   FermiEventLocationsY = numpy.array(FermiEventLocations3DTranspose)[1]
#   FermiEventLocationsZ = numpy.array(FermiEventLocations3DTranspose)[2]


#Event Engergies
EventEnergies = EventsNumpyArray["ENERGY"]
Library_PrintDatasetStatistics.Main(EventEnergies, "EventEnergies", 1)



#POINT SOURCES
PointSourcesDataFileName = "gll_psc_v14.fit"
PointSourcesDataDirectory = Const_LocalDirectoriesFermiFiles.DataPointSourcesDirectory
PointSourcesDataFilePath = PointSourcesDataDirectory + "/" + PointSourcesDataFileName
PointSources = pyfits.getdata(PointSourcesDataFilePath,1)

PointSourcesCount = len(PointSources)
PointSourceLongitudes = PointSources['GLON']
PointSourceLatitudes = PointSources['GLAT']
PointSourceLocations = numpy.vstack((PointSources['GLON'], PointSources['GLAT']) ).T #[Longitude, Latitude]
Library_PrintDatasetStatistics.Main(PointSourceLocations, "PointSourceLocations", 1)

#PointSourceAngularRadii = numpy.average(numpy.vstack( (PointSources['Conf_95_SemiMajor'], PointSources['Conf_95_SemiMinor']) ), axis = 0 )
PointSourceAngularRadii = numpy.ones(PointSourcesCount)
Library_PrintDatasetStatistics.Main(PointSourceAngularRadii, "PointSourceAngularRadii", 1)




#Point Source Locations 3d projected coordinates on unit sphere (these have centers on the unit sphere):
PointSourceDistances = numpy.ones(PointSourcesCount)
SurfaceProjectedPointSourceCenterLocations3DTupleTranspose = \
    Library_GeometrySphericalToCartesianCoordinates.Main(
        Radius          = 1.0,
        Inclination     = PointSourceLatitudes * pi/180  + pi/2,  #needs to be in radians and transformed from latitude to inclination
        Azimuth         = PointSourceLongitudes * pi/180,         #needs to be in radians
    )
SurfaceProjectedPointSourceLocations3D = numpy.array( SurfaceProjectedPointSourceCenterLocations3DTupleTranspose ).T #This is a 3D cartesian `Type_TwoDimensionalNumpyDataset`
Library_PrintDatasetStatistics.Main( SurfaceProjectedPointSourceLocations3D , 'SurfaceProjectedPointSourceLocations3D', 1)


SurfaceProjectedPointSourceRadii = numpy.ones(PointSourcesCount) * numpy.sqrt( 1 + 1 - 2*numpy.cos(1*pi/180.) ) #Law of cosines
Library_PrintDatasetStatistics.Main(SurfaceProjectedPointSourceRadii, "SurfaceProjectedPointSourceRadii", 1)




#INTERSECT EVENTS && POINTSOURCES:

print "Building FermiEventLocations3DKDTree..."
print "   FermiEventLocations3D.shape ", FermiEventLocations3D.shape
FermiEventLocations3DKDTree = scipy.spatial.KDTree( FermiEventLocations3D )

print "Querying FermiEventLocations3DKDTree for photons from galaxy groups... "
IndicesOfPhotonsFromPointSources = []
BatchSize = 500
k = 0
while ( k < PointSourcesCount):
    if (k % BatchSize == 0):
        print '   ' , datetime.datetime.utcnow(), "PointSources " , k, " to ", min(k + BatchSize, PointSourcesCount)

    PointSourceLocation = SurfaceProjectedPointSourceLocations3D[k] 
    PointSourceRadius   = SurfaceProjectedPointSourceRadii[k]

    IndicesOfPhotonsFromPointSources += FermiEventLocations3DKDTree.query_ball_point(PointSourceLocation, PointSourceRadius  )
    k = k + 1


"""
print "Building FermiEventLocations KDTree...", 'FermiEventLocations.shape', FermiEventLocations.shape
PhotonKDTree = scipy.spatial.KDTree( FermiEventLocations )
IndicesOfPhotonsFromPointSources = []
k = 0
while( k < PointSourcesCount):
    if (k %100 == 0):
        print datetime.datetime.utcnow(), k, " to ", min(k + 100, PointSourcesCount)
    PointSource = PointSourceLocations[k] #numpy.array([180.0, 0.0])
    PointSourceRadius = PointSourceRadii[k]
    IndicesOfPhotonsFromPointSource = PhotonKDTree.query_ball_point(PointSource, PointSourceRadius  )
    IndicesOfPhotonsFromPointSources = IndicesOfPhotonsFromPointSources + IndicesOfPhotonsFromPointSource
    k = k + 1
"""


#From point sources
IndicesOfPhotonsFromPointSourcesUnique = list( set(IndicesOfPhotonsFromPointSources) )
PhotonLocationsFromPointSources = FermiEventLocations[IndicesOfPhotonsFromPointSourcesUnique]
PhotonEnergiesFromPointSources = EventEnergies[IndicesOfPhotonsFromPointSourcesUnique]
Log10PhotonEnergiesFromPointSources = numpy.log10(PhotonEnergiesFromPointSources)
Library_PrintDatasetStatistics.Main(PhotonEnergiesFromPointSources, "PhotonEnergiesFromPointSources", 1)


#RELATIVE COMPLEMENT EVENTS && POINTSOURCES
#Not from point sources
IndicesOfPhotonsNotFromPointSourcesUnique = list(set(range(EventsCount)) - set(IndicesOfPhotonsFromPointSourcesUnique) )
PhotonLocationsNotFromPointSources = FermiEventLocations[IndicesOfPhotonsNotFromPointSourcesUnique]
PhotonEnergiesNotFromPointSources = EventEnergies[IndicesOfPhotonsNotFromPointSourcesUnique]
Log10PhotonEnergiesNotFromPointSources = numpy.log10(PhotonEnergiesNotFromPointSources)
Library_PrintDatasetStatistics.Main(PhotonEnergiesNotFromPointSources, "PhotonEnergiesNotFromPointSources", 1)


#GRAPHS:
DirectoryGeneratedGraphs = Const_LocalDirectoriesFermiFiles.FermiEventsSkyMapPointSourcesMask

#define directories
DirectoryGeneratedGraphsCurrentRun = DirectoryGeneratedGraphs + "/" + Library_DateStringNowGMT.Main()
if not os.path.exists(DirectoryGeneratedGraphsCurrentRun):
    os.makedirs(DirectoryGeneratedGraphsCurrentRun)
GraphFileNamePrefix = Library_DateStringNowGMT.Main()[0:11]

#size the graphs
#   Default to common monitor size:  
#   1920pixels by 1080 pixels
Inch_in_Pixels = 80.0
MonitorSize = (1920.0/Inch_in_Pixels,1080.0/Inch_in_Pixels)

#sky map point sources
Library_GraphSkyMap.Main(
    Longitudes                  = PhotonLocationsFromPointSources[:,0] , #Lon
    Latitudes                   = PhotonLocationsFromPointSources[:,1] , #Lat
    SaveFigureFilePath          = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'SkyMapEventsPointSources.png'\
    )

#sky map not point sources
Library_GraphSkyMap.Main(
    Longitudes                  = PhotonLocationsNotFromPointSources[:,0] , #Lon
    Latitudes                   = PhotonLocationsNotFromPointSources[:,1] , #Lat
    SaveFigureFilePath          = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'SkyMapEventsNotPointSources.png'\
    )

#energy spectrum from point sources
fig = matplotlib.pyplot.figure(figsize=MonitorSize)
Library_GraphOneDimensionalHistogram.Main(\
    ObservedDataset     = numpy.atleast_2d( Log10PhotonEnergiesFromPointSources ).T,\
    IncludeIntegral     = False, \
    BinCount            = 100,\
    LogCounts           = True,\
    Xlabel              = 'Log10PhotonEnergies',\
    Ylabel              = 'Log10Count',\
    PlotTitle           = 'ENERGY', \
    SaveFigureFilePath  = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10EventEnergiesPointSources.png'\
    )

#energy spectrum not from point sources
fig = matplotlib.pyplot.figure(figsize=MonitorSize)
Library_GraphOneDimensionalHistogram.Main(\
    ObservedDataset     = numpy.atleast_2d( Log10PhotonEnergiesNotFromPointSources ).T,\
    IncludeIntegral     = False, \
    BinCount            = 100,\
    LogCounts           = True,\
    Xlabel              = 'Log10PhotonEnergies',\
    Ylabel              = 'Log10Count',\
    PlotTitle           = 'ENERGY', \
    SaveFigureFilePath  = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10EventEnergiesNotPointSources.png'\
    )




