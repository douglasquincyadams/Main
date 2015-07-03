"""
DESCRIPTION:
    Generates all sky maps of photons with different energies


    Data we care about:


        #Columns:
        name = 'ENERGY'; format = 'E'; unit = 'MeV'
        name = 'L'; format = 'E'; unit = 'deg'
        name = 'B'; format = 'E'; unit = 'deg'

        #Cards:
        card.rawvalue ENERGY
        card.keyword TTYPE1
        card.comment energy of event
        cardnumber 8

        card.rawvalue L
        card.keyword TTYPE4
        card.comment Galactic longitude of event
        cardnumber 14

        card.rawvalue B
        card.keyword TTYPE5
        card.comment Galactic latitude of event
        cardnumber 16



"""

import numpy
import os
#------------------------------------------------------------------------------
import Const_LocalDirectoriesFermiFiles
import Library_DataGetFermiEvents
import Library_GraphFermiEventsSkyMap
import Library_DateStringNowGMT
import Library_PrintDatasetStatistics

"""
import Const_LocalDirectoriesFermiFiles

#DIRECTORY DEFINING
DirectoryGeneratedGraphs = Const_LocalDirectoriesFermiFiles.GeneratedGraphs
DirectoryGeneratedGraphsCurrentRun = DirectoryGeneratedGraphs  + "/" + Library_DateStringNowGMT.Main()
if not os.path.exists(DirectoryGeneratedGraphsCurrentRun):
    os.makedirs(DirectoryGeneratedGraphsCurrentRun)
"""

print "#Get the filepath we want to look at:"
#ExampleFilename = 'Events_1GeV_1Tev_zmax100_ROCK_ANGLEmax52_LAT_CONFIG1_DATA_QUALmin0.fits'
DataSourceFilename = 'filtered_events_10GeV_1TeV_zmax100_GTI_ultraclean.fits'
DirectorySourceDataFile = Const_LocalDirectoriesFermiFiles.DataFilesCutsDirectory + '/' + DataSourceFilename
DirectoryGeneratedGraphs = Const_LocalDirectoriesFermiFiles.FermiEventsSkyMap 

print "Extracting the Data"
EventsNumpyArray, EventsColumnNames = Library_DataGetFermiEvents.Main(\
    Filepath = DirectorySourceDataFile,\
    PrintExtra = False,\
    )
Library_PrintDatasetStatistics.Main(EventsNumpyArray, "EventsNumpyArray", 1)

EventEnergies = EventsNumpyArray["ENERGY"]
Library_PrintDatasetStatistics.Main(EventEnergies, "EventEnergies", 1)
#EventsNumpyArray = EventsNumpyArray[numpy.where(EventsNumpyArray['ENERGY'] >= 4e4 ) ]


print "Graphing the Data"
Library_GraphFermiEventsSkyMap.Main(EventsNumpyArray = EventsNumpyArray, DirectoryGeneratedGraphs = DirectoryGeneratedGraphs)   











