
import Const_LocalDirectoriesFermiFiles
import Library_PrintDatasetStatistics
import Library_GeometrySphericalToCartesianCoordinates

import numpy
from numpy import pi
import pyfits
import numpy as np


def Main(PSF=None):

    
    
    #POINT SOURCES
    PointSourcesDataFileName = "gll_psc_v14.fit"
    PointSourcesDataDirectory = Const_LocalDirectoriesFermiFiles.DataPointSourcesDirectory
    PointSourcesDataFilePath = PointSourcesDataDirectory + "/" + PointSourcesDataFileName
    PointSources = pyfits.getdata(PointSourcesDataFilePath,1)

    PointSourcesCount = len(PointSources)
    PointSourceLongitudes = PointSources['GLON']
    PointSourceLatitudes = PointSources['GLAT']
    PointSourceLocations = numpy.vstack((PointSources['GLON'], PointSources['GLAT']) ).T #[Longitude, Latitude]
    #Library_PrintDatasetStatistics.Main(PointSourceLocations, "PointSourceLocations", 1)

    #PointSourceAngularRadii = numpy.average(numpy.vstack( (PointSources['Conf_95_SemiMajor'], PointSources['Conf_95_SemiMinor']) ), axis = 0 )
    PointSourceAngularRadii = numpy.ones(PointSourcesCount)

    #Library_PrintDatasetStatistics.Main(PointSourceAngularRadii, "PointSourceAngularRadii", 1)

    #Point Source Locations 3d projected coordinates on unit sphere (these have centers on the unit sphere):
    PointSourceDistances = numpy.ones(PointSourcesCount)
    if PSF==None:
        SurfaceProjectedPointSourceRadii = PointSourceAngularRadii *numpy.tan(1*np.pi/180.)
    else:
        SurfaceProjectedPointSourceRadii = PointSourceAngularRadii *numpy.tan(PSF*np.pi/180.)
        
    SurfaceProjectedPointSourceCenterLocations3DTupleTranspose = \
        Library_GeometrySphericalToCartesianCoordinates.Main(
            Radius          = numpy.sqrt(1.0+SurfaceProjectedPointSourceRadii**2),
            Inclination     = PointSourceLatitudes * pi/180  + pi/2,  #needs to be in radians and transformed from latitude to inclination
            Azimuth         = PointSourceLongitudes * pi/180,         #needs to be in radians
        )
    SurfaceProjectedPointSourceLocations3D = numpy.array( SurfaceProjectedPointSourceCenterLocations3DTupleTranspose ).T #This is a 3D cartesian `Type_TwoDimensionalNumpyDataset`
    #Library_PrintDatasetStatistics.Main( SurfaceProjectedPointSourceLocations3D , 'SurfaceProjectedPointSourceLocations3D', 1)


    #Library_PrintDatasetStatistics.Main(SurfaceProjectedPointSourceRadii, "SurfaceProjectedPointSourceRadii", 1)

    return PointSources,SurfaceProjectedPointSourceLocations3D,SurfaceProjectedPointSourceRadii

if __name__ == '__main__':
    Main()

