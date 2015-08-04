"""
ENERGY DISPERSION
"""
import numpy
import matplotlib
import matplotlib.pyplot
#------------------------------------------------------------------------------
import Const_LocalDirectoriesFermiFiles
import Library_DataGetFermiInstrumentResponseEnergyDispersion
import Library_GraphTwoDimensionDensityColorMap
#Get the filepath we want to look at:
#EnergyDispersionFile:
ExampleFilename0 = 'edisp_P7REP_ULTRACLEAN_V15_back.fits'
ExampleFilename1 = 'edisp_P7REP_ULTRACLEAN_V15_front.fits'
ExampleFilepath = Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponseDirectory + '/4Ultra/EnergyDispersion/' + ExampleFilename0 
print 'ExampleFilepath', ExampleFilepath


#Get a funciton which is defined by a file:
EnergyDispersionFunction = Library_DataGetFermiInstrumentResponseEnergyDispersion.Main(
    Filepath = ExampleFilepath,
    PrintExtra = True,
    )


Value = EnergyDispersionFunction(
    DeltaEnergy = 0,
    )























