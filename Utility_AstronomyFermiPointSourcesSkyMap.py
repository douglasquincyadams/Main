"""
DESCRIPTION:

    Gets all the photons gathered by the fermi satilite
    Gets all the fermi identified point sources
    
    Takes the reletive complement (AllEvents, PointSources)
    Thus obtaining all the Events which are NOT from PointSources

    Generates an all sky map of these remaining photons after the Mask

    Additional ColumnNamesDescriptions
        http://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermilpsc.html


"""
import astropy
import astropy.io
import astropy.io.fits
import pyfits
import numpy
import matplotlib.pylab
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------
import Const_LocalDirectoriesFermiFiles

import Library_FitsInfoPrint
import Library_GraphSkyMap


PointSourcesDataFileName = "gll_psc_v14.fit"
PointSourcesDataDirectory = Const_LocalDirectoriesFermiFiles.DataPointSourcesDirectory
PointSourcesDataFilePath = PointSourcesDataDirectory + "/" + PointSourcesDataFileName

#Library_FitsInfoPrint.Main(PointSourcesDataFilePath)

#HDUList = astropy.io.fits.open(PointSourcesDataFilePath)
#PointSources = HDUList[2]
#PointSourceData = PointSources.Data
PointSources = pyfits.getdata(PointSourcesDataFilePath,1)

#    name = 'GLON'; format = 'E'; unit = 'deg'; disp = 'F8.4'
#    name = 'GLAT'; format = 'E'; unit = 'deg'; disp = 'F8.4'
#    name = 'Conf_95_SemiMajor'; format = 'E'; unit = 'deg'; disp = 'F8.4'
#    name = 'Conf_95_SemiMinor'; format = 'E'; unit = 'deg'; disp = 'F8.4'
#    name = 'Conf_95_PosAng'; format = 'E'; unit = 'deg'; disp = 'F8.3'


Longitudes = PointSources['GLON']
print 'Longitudes.shape', Longitudes.shape

Latitudes = PointSources['GLAT']
print 'Latitudes.shape', Latitudes.shape

Radii = numpy.average(numpy.vstack( (PointSources['Conf_95_SemiMajor'], PointSources['Conf_95_SemiMinor']) ), axis = 0 )
print 'Radii.shape', Radii.shape



PointSourcesGeneratedGraphsDirectory = Const_LocalDirectoriesFermiFiles.FermiPointSourcesSkyMap

Library_GraphSkyMap.Main(
    Latitudes   = Latitudes   ,
    Longitudes  = Longitudes  ,
    Zvalues     = Radii,
#    ShapeFunctions =
#    Projection =
    DirectoryGeneratedGraphs = PointSourcesGeneratedGraphsDirectory ,
    )




"""
#Dataget Lines:
_3fgl = pyfits.getdata(PointSourcesFilePath,1)
sigma = numpy.array(_3fgl["Signif_Avg"],dtype=float)
sigma = sigma[numpy.where(numpy.isfinite(sigma))]



#Plt lines:
bins = numpy.linspace(numpy.min(sigma),numpy.max(sigma),100)
fig, ax = plt.subplots(ncols=1,nrows=1)
plt.hist(sigma,bins=bins,log=True)
plt.draw()
plt.show()

"""




