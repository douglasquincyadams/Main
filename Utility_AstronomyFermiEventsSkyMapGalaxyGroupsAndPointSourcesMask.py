"""
DESCRIPTION:
    Graphs a sky map of all the fermi events which are:
        NOT from point sources
        ARE from galaxy groups
        
    Models Likelihood of PowerLaw + Dispersion
    

"""
import datetime
import numpy
import pprint
import pyfits
import astropy
import scipy
import matplotlib.pyplot
#------------------------------------------------------------------------------
import Const_LocalDirectoriesFermiFiles
import Const_LocalDirectoriesGalaxyGroupsFiles

import Library_DataGetFermiEvents
import Library_DataGetAllGalaxyGroups
import Library_GeometrySphericalToCartesianCoordinates
import Library_GeometrySphereSurfaceProjectExternalSphere
import Library_GraphFermiEnergySpectrum
import Library_LocalStorageSaveVariable
import Library_LocalStorageLoadVariable
import Library_MemoryLimit
import Library_PrintDatasetStatistics
import Library_ArraySparseSubset
import Library_FermiEnergySpectrumFeatureSearch


#DEFINE CONSTANTS:
pi = numpy.pi

#SET MEMORY LIMIT TO N-GIGABYTES (Avoid Crashing Computer):
Library_MemoryLimit.Main(Bytes = 4*1000000000) 



#Attempt to load the locations and energies from local storage: (Cache to prevent duplicating work) 
PhotonLocationsNotFromPointSourcesFromGalaxyGroups = Library_LocalStorageLoadVariable.Main(
    VariableName = 'PhotonLocationsNotFromPointSourcesFromGalaxyGroups',
    )
PhotonEnergiesNotFromPointSourcesFromGalaxyGroups = Library_LocalStorageLoadVariable.Main(
    VariableName = 'PhotonEnergiesNotFromPointSourcesFromGalaxyGroups',
    )
GroupSourcesDataColumnNames = Library_LocalStorageLoadVariable.Main(
    VariableName = 'GroupSourcesDataColumnNames',
    )
GroupSourcesData = Library_LocalStorageLoadVariable.Main(
    VariableName = 'GroupSourcesData',
    )


if (
        PhotonLocationsNotFromPointSourcesFromGalaxyGroups == None
    or  PhotonEnergiesNotFromPointSourcesFromGalaxyGroups == None
    or  GroupSourcesDataColumnNames == None
    or  GroupSourcesData == None
    ):

    print 'TempData missing. \n Extracting events, point source, groups from files'

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

    #Group sphere center RadiiAndCenterDistances projected onto unit sphere:
    SurfaceProjectedGroupRadiiAndCenterDistances = \
        Library_GeometrySphereSurfaceProjectExternalSphere.Main(
            ExternalSphereCenterDistance    = GalaxyGroupDistances, 
            ExternalSphereRadius            = GalaxyGroupRadii, 
            SphereSurfaceRadius             = 1.,
            #unit sphere has radius 1  
            #-> in this case the radius is 1 cm 
            #but it doesn't matter, 
            #because as long as the radii and distances
            #are of the same units, the 
            #sphere surface radius could now be in any unit
        )
    SurfaceProjectedGroupRadii = SurfaceProjectedGroupRadiiAndCenterDistances['ProjectedSphereRadius'] # these != 1.0
    SurfaceProjectedGroupRadii1D = SurfaceProjectedGroupRadii.T[0]
    Library_PrintDatasetStatistics.Main( SurfaceProjectedGroupRadii, 'SurfaceProjectedGroupRadii', 1)
    SurfaceProjectedGroupCenterDistances = SurfaceProjectedGroupRadiiAndCenterDistances['ProjectedSphereCenterDistance']
    Library_PrintDatasetStatistics.Main( SurfaceProjectedGroupCenterDistances, 'SurfaceProjectedGroupCenterDistances', 1)

    #Group sphere center location projected onto unit sphere:
    SurfaceProjectedGroupCenterLocations3DTupleTranspose = \
        Library_GeometrySphericalToCartesianCoordinates.Main(
            Radius          = SurfaceProjectedGroupCenterDistances.T[0],
            Inclination     = GalaxyGroupGalacticLatitudes.T[0] * pi/180. + pi/2, #needs to be in radians and transformed from latitude to inclination
            Azimuth         = GalaxyGroupGalacticLongitudes.T[0] * pi/180., #needs to be in radians
        )
    SurfaceProjectedGroupCenterLocations3D = numpy.array(SurfaceProjectedGroupCenterLocations3DTupleTranspose).T
    Library_PrintDatasetStatistics.Main( SurfaceProjectedGroupCenterLocations3D , 'SurfaceProjectedGroupCenterLocations3D', 1)

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
    SurfaceProjectedPointSourceRadii = numpy.ones(PointSourcesCount) *numpy.tan(1*np.pi/180.)

    SurfaceProjectedPointSourceCenterLocations3DTupleTranspose = \
        Library_GeometrySphericalToCartesianCoordinates.Main(
            Radius          = numpy.sqrt(1.0+SurfaceProjectedPointSourceRadii**2),
            Inclination     = PointSourceLatitudes * pi/180  + pi/2,  #needs to be in radians and transformed from latitude to inclination
            Azimuth         = PointSourceLongitudes * pi/180,         #needs to be in radians
        )
    SurfaceProjectedPointSourceLocations3D = numpy.array( SurfaceProjectedPointSourceCenterLocations3DTupleTranspose ).T #This is a 3D cartesian `Type_TwoDimensionalNumpyDataset`
    Library_PrintDatasetStatistics.Main( SurfaceProjectedPointSourceLocations3D , 'SurfaceProjectedPointSourceLocations3D', 1)


    Library_PrintDatasetStatistics.Main(SurfaceProjectedPointSourceRadii, "SurfaceProjectedPointSourceRadii", 1)

    #INTERSECT EVENTS && POINTSOURCES:
    print "Building FermiEventLocations3DKDTree..."
    print "   FermiEventLocations3D.shape ", FermiEventLocations3D.shape
    FermiEventLocations3DKDTree = scipy.spatial.KDTree( FermiEventLocations3D )

    print "Querying FermiEventLocationsKDTree for photons from point sources... "
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

    #all photons From point sources
    IndicesOfPhotonsFromPointSourcesUnique = list( set(IndicesOfPhotonsFromPointSources) )
    PhotonLocationsFromPointSources = FermiEventLocations[IndicesOfPhotonsFromPointSourcesUnique]
    Library_PrintDatasetStatistics.Main(PhotonLocationsFromPointSources, "PhotonLocationsFromPointSources", 1)

    PhotonEnergiesFromPointSources = EventEnergies[IndicesOfPhotonsFromPointSourcesUnique]
    Library_PrintDatasetStatistics.Main(PhotonEnergiesFromPointSources, "PhotonEnergiesFromPointSources", 1)


    #RELATIVE COMPLEMENT EVENTS && POINTSOURCES
    #all photons NOT from point sources
    IndicesOfPhotonsNotFromPointSourcesUnique = list(set(range(EventsCount)) - set(IndicesOfPhotonsFromPointSourcesUnique) )
    PhotonLocationsNotFromPointSources = FermiEventLocations[IndicesOfPhotonsNotFromPointSourcesUnique]
    Library_PrintDatasetStatistics.Main(PhotonLocationsNotFromPointSources, "PhotonLocationsNotFromPointSources", 1)

    PhotonEnergiesNotFromPointSources = EventEnergies[IndicesOfPhotonsNotFromPointSourcesUnique]
    Library_PrintDatasetStatistics.Main(PhotonEnergiesNotFromPointSources, "PhotonEnergiesNotFromPointSources", 1)

    PhotonLocationsNotFromPointSources3DProjectedCartesian = FermiEventLocations3D[IndicesOfPhotonsNotFromPointSourcesUnique]
    Library_PrintDatasetStatistics.Main(PhotonLocationsNotFromPointSources3DProjectedCartesian, "PhotonLocationsNotFromPointSources3DProjectedCartesian", 1)

    #INTERSECT GALAXYGROUPS && (REMAINING EVENTS after RELATIVE COMP POINT SOURCES)

    #for Energy in EnergyAlphaBins:

    print "Building  PhotonLocationsNotFromPointSources3DProjectedCartesianKDTree..."
    print "   PhotonLocationsNotFromPointSources3DProjectedCartesian.shape ", PhotonLocationsNotFromPointSources3DProjectedCartesian.shape
    PhotonLocationsNotFromPointSources3DProjectedCartesianKDTree = scipy.spatial.KDTree( PhotonLocationsNotFromPointSources3DProjectedCartesian )

    print "Querying PhotonLocationsNotFromPointSources3DProjectedCartesianKDTree for photons from each GalaxyGroup... "
    IndicesOfPhotonsNotFromPointSourcesFromGalaxyGroups = []
    k = 0 
    while ( k < GalaxyGroupCount):
        if (k % BatchSize == 0):
            print '   ' , datetime.datetime.utcnow(), "GalaxyGroups " , k, " to ", min(k + BatchSize, GalaxyGroupCount)
        GalaxyGroupLocation = SurfaceProjectedGroupCenterLocations3D[k] #numpy.array([180.0, 0.0])
        GalaxyGroupRadius   = SurfaceProjectedGroupRadii1D[k]
        IndicesOfPhotonsNotFromPointSourcesFromGalaxyGroups += PhotonLocationsNotFromPointSources3DProjectedCartesianKDTree.query_ball_point( GalaxyGroupLocation, GalaxyGroupRadius  )
        k = k + 1

    #All photons NOT From point sources AND from galaxy groups:
    IndicesOfPhotonsNotFromPointSourcesFromGalaxyGroupsUnique = list(set(IndicesOfPhotonsNotFromPointSourcesFromGalaxyGroups))
    PhotonLocationsNotFromPointSourcesFromGalaxyGroups = PhotonLocationsNotFromPointSources[IndicesOfPhotonsNotFromPointSourcesFromGalaxyGroupsUnique]
    Library_PrintDatasetStatistics.Main(PhotonLocationsNotFromPointSourcesFromGalaxyGroups, "PhotonLocationsNotFromPointSourcesFromGalaxyGroups", 1)

    PhotonEnergiesNotFromPointSourcesFromGalaxyGroups = PhotonEnergiesNotFromPointSources[IndicesOfPhotonsNotFromPointSourcesFromGalaxyGroupsUnique]
    Library_PrintDatasetStatistics.Main(PhotonEnergiesNotFromPointSourcesFromGalaxyGroups, "PhotonEnergiesNotFromPointSourcesFromGalaxyGroups", 1)


    #Save the Locations and Energies in local storage for later:
    Library_LocalStorageSaveVariable.Main(
        Variable = PhotonLocationsNotFromPointSourcesFromGalaxyGroups,
        VariableName = 'PhotonLocationsNotFromPointSourcesFromGalaxyGroups',
        Overwrite = True,
        )
    Library_LocalStorageSaveVariable.Main(
        Variable = PhotonEnergiesNotFromPointSourcesFromGalaxyGroups,
        VariableName = 'PhotonEnergiesNotFromPointSourcesFromGalaxyGroups',
        Overwrite = True,
        )

    #Save the galaxy group data as well
    Library_LocalStorageSaveVariable.Main(
        Variable = GroupSourcesDataColumnNames,
        VariableName = 'GroupSourcesDataColumnNames',
        Overwrite = True,
        )
    Library_LocalStorageSaveVariable.Main(
        Variable = GroupSourcesData,
        VariableName = 'GroupSourcesData',
        Overwrite = True,
        )


#GRAPH:
print 'Defining directories...'
DirectoryGeneratedGraphs = Const_LocalDirectoriesFermiFiles.FermiEventsSkyMapGalaxyGroupsAndPointSourcesMask
print 'DirectoryGeneratedGraphs', DirectoryGeneratedGraphs



#Take a subset of the Energies for the modeling, to make things faster 
#   (I really should be taking a subset of the galaxy groups to do this instead...):
PhotonEnergiesNotFromPointSourcesFromGalaxyGroupsSubset = Library_ArraySparseSubset.Main(
    Array = PhotonEnergiesNotFromPointSourcesFromGalaxyGroups,
    SubsetFraction = .05
    )
Library_PrintDatasetStatistics.Main(PhotonEnergiesNotFromPointSourcesFromGalaxyGroupsSubset, "PhotonEnergiesNotFromPointSourcesFromGalaxyGroupsSubset", 4)



#Choose which photons to search through (Pick an energy Range):
SelectedPhotonEnergies = []
for PhotonEnergy in PhotonEnergiesNotFromPointSourcesFromGalaxyGroupsSubset:
    if (PhotonEnergy > 20000):
        SelectedPhotonEnergies.append(PhotonEnergy)
SelectedPhotonEnergies = numpy.array(SelectedPhotonEnergies)
SelectedPhotonEnergyMinimum = min(SelectedPhotonEnergies)

print 'PhotonEnergies.shape', SelectedPhotonEnergies.shape
PhotonCount = len(SelectedPhotonEnergies)
SelectedPhotonEnergies = numpy.atleast_2d( numpy.array(sorted(SelectedPhotonEnergies.tolist()) ) ).T
Library_PrintDatasetStatistics.Main(SelectedPhotonEnergies, 'SelectedPhotonEnergies', 1)



#Run the feature search analysis on the photons we have selected:
Library_FermiEnergySpectrumFeatureSearch.Main( 
    DirectoryGeneratedGraphs = DirectoryGeneratedGraphs,
    SelectedPhotonEnergies = SelectedPhotonEnergies,
    #ExpectedSignalDensityFunction = TotalJsmoothExposureFoldProbabilityDensityFunction,
    GroupSourcesData = GroupSourcesData, 
    GroupSourcesDataColumnNames = GroupSourcesDataColumnNames,
    )


print 'End of code'






#matplotlib.pyplot.show()








