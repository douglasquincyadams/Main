"""
DESCRIPTION:
    Gets all the fermi photons
    Gets all the galaxy groups
    Filters ALL the fermi photons using a mask of the galaxy groups

    Graphs the remaining photons after the mask
"""
import matplotlib
import matplotlib.pyplot
import numpy
import scipy
from scipy import spatial
import datetime
import os
import collections
#------------------------------------------------------------------------------
import Const_LocalDirectoriesFermiFiles
import Const_LocalDirectoriesGalaxyGroupsFiles

import Library_DataGetAllGalaxyGroups 
import Library_DataGetFermiEvents
import Library_DateStringNowGMT
import Library_GraphSkyMap
import Library_GraphOneDimensionalHistogram
import Library_GraphBarChartOccurrenceCounts
import Library_MemoryLimit
import Library_PrintDatasetStatistics
import Library_GeometrySphericalToCartesianCoordinates
import Library_GeometrySphereSurfaceProjectExternalSphere

pi = numpy.pi
#SET MEMORY LIMIT TO N-GIGABYTES (Avoid Crashing Computer):
Library_MemoryLimit.Main(Bytes = 4*1000000000) 


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



#GALAXY GROUPS
#extract data
GroupSourcesDirectorySourceDataFiles = Const_LocalDirectoriesGalaxyGroupsFiles.SourceDataFiles
GroupSourcesCatalogs            = ["Data2MassTullyNorth", "Data2MassTullySouth"] ##all together now
GroupSourcesData, GroupSourcesDataColumnNames = Library_DataGetAllGalaxyGroups.Main(DatasetNames = GroupSourcesCatalogs, DirectorySourceDataFiles = GroupSourcesDirectorySourceDataFiles)
GalaxyGroupCount = len(GroupSourcesData)

#Group sphere center locations 
GalaxyGroupGalacticLongitudes   = GroupSourcesData[:,[GroupSourcesDataColumnNames.index("GalacticLongitudeInDegrees")] ]
GalaxyGroupGalacticLatitudes    = GroupSourcesData[:,[GroupSourcesDataColumnNames.index("GalacticLatitudeInDegrees")] ]
GalaxyGroupLocations            = numpy.concatenate( (GalaxyGroupGalacticLongitudes, GalaxyGroupGalacticLatitudes), axis = 1 )
Library_PrintDatasetStatistics.Main(GalaxyGroupLocations, "GalaxyGroupLocations", 1)

GalaxyGroupDistances            = GroupSourcesData[:,[GroupSourcesDataColumnNames.index("DistanceInCm")] ]
GalaxyGroupRadii                = GroupSourcesData[:,[GroupSourcesDataColumnNames.index("RvirInCm")] ]
Library_PrintDatasetStatistics.Main(GalaxyGroupRadii, "GalaxyGroupRadii", 1)

#Group sphere center locations scaled onto unit sphere:
SurfaceProjectedGroupRadiiAndCenterDistances = \
    Library_GeometrySphereSurfaceProjectExternalSphere.Main(
        ExternalSphereCenterDistance    = GalaxyGroupDistances, 
        ExternalSphereRadius            = GalaxyGroupRadii, 
        SphereSurfaceRadius             = 1.,#unit sphere has radius 1  
                                            #-> in this case the radius is 1 cm 
                                            #but it doesn't matter, 
                                            #because as long as the radii and distances
                                            #are of the same units, the 
                                            #sphere surface radius could now be in any unit
    )
SurfaceProjectedGroupRadii = SurfaceProjectedGroupRadiiAndCenterDistances['ProjectedSphereRadius']
SurfaceProjectedGroupRadii1D = SurfaceProjectedGroupRadii.T[0]
Library_PrintDatasetStatistics.Main( SurfaceProjectedGroupRadii, 'SurfaceProjectedGroupRadii', 1)
SurfaceProjectedGroupCenterDistances = SurfaceProjectedGroupRadiiAndCenterDistances['ProjectedSphereCenterDistance']
Library_PrintDatasetStatistics.Main( SurfaceProjectedGroupCenterDistances, 'SurfaceProjectedGroupCenterDistances', 1)

#Group sphere center locations cartesian onto unit sphere:
SurfaceProjectedGroupCenterLocations3DTupleTranspose = \
    Library_GeometrySphericalToCartesianCoordinates.Main(
        Radius          = SurfaceProjectedGroupCenterDistances.T[0],
        Inclination     = GalaxyGroupGalacticLatitudes.T[0] * pi/180. + pi/2, #needs to be in radians and transformed from latitude to inclination
        Azimuth         = GalaxyGroupGalacticLongitudes.T[0] * pi/180., #needs to be in radians
    )
SurfaceProjectedGroupCenterLocations3D = numpy.array(SurfaceProjectedGroupCenterLocations3DTupleTranspose).T
Library_PrintDatasetStatistics.Main( SurfaceProjectedGroupCenterLocations3D , 'SurfaceProjectedGroupCenterLocations3D', 1)




#INTERSECT EVENTS && GALAXY GROUPS:

print "Building FermiEventLocations3DKDTree..."
print "   FermiEventLocations3D.shape ", FermiEventLocations3D.shape
FermiEventLocations3DKDTree = scipy.spatial.KDTree( FermiEventLocations3D )

print "Querying FermiEventLocations3DKDTree for photons from galaxy groups... "
IndicesOfPhotonsFromGalaxyGroups = []
BatchSize = 500
k = 0
while ( k < GalaxyGroupCount):
    if (k % BatchSize == 0):
        print '   ' , datetime.datetime.utcnow(), "GalaxyGroups " , k, " to ", min(k + BatchSize, GalaxyGroupCount)

    GalaxyGroupLocation = SurfaceProjectedGroupCenterLocations3D[k] 
    GalaxyGroupRadius   = SurfaceProjectedGroupRadii1D[k]

    IndicesOfPhotonsFromGalaxyGroups += FermiEventLocations3DKDTree.query_ball_point(GalaxyGroupLocation, GalaxyGroupRadius  )
    k = k + 1



#All photons from galaxy groups:
IndicesOfPhotonsFromGalaxyGroupsUnique = list( set(IndicesOfPhotonsFromGalaxyGroups) )
PhotonLocationsFromGalaxyGroups = FermiEventLocations[IndicesOfPhotonsFromGalaxyGroupsUnique]
Library_PrintDatasetStatistics.Main(PhotonLocationsFromGalaxyGroups, "PhotonLocationsFromGalaxyGroups", 1)

PhotonEnergiesFromGalaxyGroups = EventEnergies[IndicesOfPhotonsFromGalaxyGroupsUnique]
Library_PrintDatasetStatistics.Main(PhotonEnergiesFromGalaxyGroups, "PhotonEnergiesFromGalaxyGroups", 1)

Log10PhotonEnergiesFromGalaxyGroups = numpy.log10(PhotonEnergiesFromGalaxyGroups)




#GRAPH:
DirectoryGeneratedGraphs = Const_LocalDirectoriesFermiFiles.FermiEventsSkyMapGalaxyGroupsMask

DirectoryGeneratedGraphsCurrentRun = DirectoryGeneratedGraphs + "/" + Library_DateStringNowGMT.Main()
if not os.path.exists(DirectoryGeneratedGraphsCurrentRun):
    os.makedirs(DirectoryGeneratedGraphsCurrentRun)
GraphFileNamePrefix = Library_DateStringNowGMT.Main()[0:11]

#size the graphs
#   Default to common monitor size:  
#   1920pixels by 1080 pixels
Inch_in_Pixels = 80.0
MonitorSize = (1920.0/Inch_in_Pixels,1080.0/Inch_in_Pixels)

#sky map
Library_GraphSkyMap.Main(
    Longitudes                  = PhotonLocationsFromGalaxyGroups[:,0] , #Lon
    Latitudes                   = PhotonLocationsFromGalaxyGroups[:,1] , #Lat
    SaveFigureFilePath          = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'PhotonLocationsFromGalaxyGroups.png'\
    )

#energies:
fig = matplotlib.pyplot.figure(figsize=MonitorSize)
Library_GraphOneDimensionalHistogram.Main(\
    ObservedDataset     = numpy.atleast_2d( Log10PhotonEnergiesFromGalaxyGroups ).T,\
    IncludeIntegral     = False, \
    BinCount            = 100,\
    LogCounts           = True,\
    Xlabel              = 'Log10PhotonEnergies',\
    Ylabel              = 'Log10Count',\
    PlotTitle           = 'ENERGY', \
    SaveFigureFilePath  = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'Log10PhotonEnergiesFromGalaxyGroups.png'\
    )


#hist intersection counts:
fig = matplotlib.pyplot.figure(figsize=MonitorSize)
Library_GraphBarChartOccurrenceCounts.Main(
    PythonList = IndicesOfPhotonsFromGalaxyGroups ,
    SaveFigureFilePath  = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'IndicesOfPhotonsFromGalaxyGroupsCountCounts.png' ,
    )









#FermiEventLocations3D
#SurfaceProjectedGroupCenterLocations3D
#SurfaceProjectedGroupRadii1D

"""
print "Building FermiEventLocationsKDTree..."
print "   FermiEventLocations.shape ", FermiEventLocations.shape
FermiEventLocationsKDTree = scipy.spatial.KDTree( FermiEventLocations )

print "Querying FermiEventLocationsKDTree for photons from galaxy groups... "
IndicesOfPhotonsFromGalaxyGroups = []
BatchSize = 500
k = 0
while ( k < GalaxyGroupCount):
    if (k % BatchSize == 0):
        print '   ' , datetime.datetime.utcnow(), "GalaxyGroups " , k, " to ", min(k + BatchSize, GalaxyGroupCount)
    GalaxyGroupLocation = GalaxyGroupLocations[k] 
    GalaxyGroupRadius   = GalaxyGroupRadii[k]

    IndicesOfPhotonsFromGalaxyGroups += FermiEventLocationsKDTree.query_ball_point(GalaxyGroupLocation, GalaxyGroupRadius  )
    k = k + 1
"""















