#!/usr/bin/env python 
"""
returns selected Galaxies based either on  Jfactor or mass of halo
as well as size 
"""
import numpy
from numpy import pi
import Const_LocalDirectoriesGalaxyGroupsFiles

import Library_DataGetAllGalaxyGroups

import Library_GeometrySphereSurfaceProjectExternalSphere
import Library_GeometrySphericalToCartesianCoordinates
import Library_PSF

def Main(PSFfunct=None,):

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
    #Library_PrintDatasetStatistics.Main(GalaxyGroupLocations, "GalaxyGroupLocations", 1)

    GalaxyGroupDistances            = GroupSourcesData[:,[GroupSourcesDataColumnNames.index("DistanceInCm")] ]
    GalaxyGroupRadii                = GroupSourcesData[:,[GroupSourcesDataColumnNames.index("RvirInCm")] ]
    #Library_PrintDatasetStatistics.Main(GalaxyGroupRadii, "GalaxyGroupRadii", 1)

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
    #Angle on the Sky
    AngleOnSkyOfViralRadius=SurfaceProjectedGroupRadiiAndCenterDistances["ExternalSphereCentralRadialAngle"]
    AngleOnSkyOfViralRadiusinDegrees=numpy.degrees(AngleOnSkyOfViralRadius)
    AngleOnSkyOfViralRadiusinDegrees=AngleOnSkyOfViralRadiusinDegrees.T[0]
    if PSFfunct==None:
        HaloPSFonSky=AngleOnSkyOfViralRadiusinDegrees
    else:
        HaloPSFonSky=PSFfunct(AngleOnSkyOfViralRadiusinDegrees)    
    
    #print 'AngleOnSkyOfViralRadiusinDegrees',AngleOnSkyOfViralRadiusinDegrees.shape
    #print len(AngleOnSkyOfViralRadiusinDegrees)
    DistanceToCenterofProjectedhalo=1/numpy.cos(numpy.radians(HaloPSFonSky))
    ProjectedRadiusofHalo=numpy.sin(numpy.radians(HaloPSFonSky))                                               
 

    #Group sphere center location projected onto unit sphere:
    SurfaceProjectedGroupCenterLocations3DTupleTranspose = \
        Library_GeometrySphericalToCartesianCoordinates.Main(
            Radius          = DistanceToCenterofProjectedhalo,#distance from origin to halo 
            Inclination     = GalaxyGroupGalacticLatitudes.T[0] * pi/180. + pi/2, #needs to be in radians and transformed from latitude to inclination
            Azimuth         = GalaxyGroupGalacticLongitudes.T[0] * pi/180., #needs to be in radians
        )
    SurfaceProjectedGroupCenterLocations3D = numpy.array(SurfaceProjectedGroupCenterLocations3DTupleTranspose).T
    #Library_PrintDatasetStatistics.Main( SurfaceProjectedGroupCenterLocations3D , 'SurfaceProjectedGroupCenterLocations3D', 1)


    return SurfaceProjectedGroupCenterLocations3D,ProjectedRadiusofHalo,GroupSourcesData, GroupSourcesDataColumnNames




if __name__ == '__main__':
    Main()


