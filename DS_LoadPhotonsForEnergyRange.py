#!/usr/bin/env python 
"""
designed to load
Photons of a fixed energy range
returns array read from a fits file

"""
import numpy
import pylab as py
from  numpy import pi
import Const_LocalDirectoriesFermiFiles

import Library_DataGetFermiEvents
import Library_PrintDatasetStatistics
import Library_GeometrySphericalToCartesianCoordinates

import Utility_masterConfig as config

def Main(EnergyMax=None,EnergyMin=None,):
    #EVENTS
    #extract
    EventsDataSourceFilename = 'filtered_events_10GeV_1TeV_zmax100_GTI_ultraclean.fits'
    EventsDirectorySourceDataFile = Const_LocalDirectoriesFermiFiles.DataFilesCutsDirectory + '/' + EventsDataSourceFilename
    EventsNumpyArray, EventsColumnNames = Library_DataGetFermiEvents.Main(\
        Filepath = EventsDirectorySourceDataFile,\
        PrintExtra = False,\
        )
    

    #Event Engergies
    EventEnergies = EventsNumpyArray["ENERGY"]
    #Library_PrintDatasetStatistics.Main(EventEnergies, "EventEnergies", 1)

    #Select the Events
    EventsCount=0.
    EnergyMinIncriment=EnergyMin
    EnergyMaxIncriment=EnergyMax
    while(EventsCount<config.NumberOfPhotons):        
        EnergyIndex=py.find((EventEnergies<EnergyMaxIncriment)&(EventEnergies>EnergyMinIncriment))
        EventsCount=len(EnergyIndex)
        EnergyMaxOut=EnergyMaxIncriment
        EnergyMinOut=EnergyMinIncriment
        EnergyMinIncriment=EnergyMinIncriment-0.03*(EnergyMin+EnergyMax)/2.
        EnergyMaxIncriment=EnergyMaxIncriment+0.03*(EnergyMin+EnergyMax)/2.
        
    print 'EnergyMaxOut', EnergyMaxOut
    print 'EnergyMinOut',EnergyMinOut
    EventEnergiesSelected=EventEnergies[EnergyIndex]

    #Event Locations
    EventGalacticLongitudes = EventsNumpyArray["L"][EnergyIndex]
    EventGalacticLatitudes = EventsNumpyArray["B"][EnergyIndex]
    FermiEventLocations = numpy.vstack((EventGalacticLongitudes, EventGalacticLatitudes) ).T #[Longitude, Latitude]
    #Library_PrintDatasetStatistics.Main(FermiEventLocations, "FermiEventLocations", 1)

    #Event Locations 3d projected coordinates on unit sphere:
    FermiEventLocations3DTupleTranspose = \
        Library_GeometrySphericalToCartesianCoordinates.Main(
            Radius          = numpy.ones(shape = (EventsCount,)),
            Inclination     = EventGalacticLatitudes * pi/180  + pi/2,  #needs to be in radians and transformed from latitude to inclination
            Azimuth         = EventGalacticLongitudes * pi/180,         #needs to be in radians
        )
    FermiEventLocations3D = numpy.array( FermiEventLocations3DTupleTranspose ).T #This is a 3D cartesian `Type_TwoDimensionalNumpyDataset`
    #Library_PrintDatasetStatistics.Main( FermiEventLocations3D , 'FermiEventLocations3D', 1)

    return FermiEventLocations3D,EventEnergiesSelected,EnergyMaxOut,EnergyMinOut










if __name__ == '__main__':
    Main()
