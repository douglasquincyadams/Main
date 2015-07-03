#MainDirectory = '/media/doug/DATADISK/Doug/FermiData'
MainDirectory = '/home/douglas/Desktop/LocalDataCopies/FermiData'

DataFilesWeeklyDirectory = MainDirectory + '/extended'

DataFilesCutsDirectory = MainDirectory + '/extended_cuts'

DataPointSourcesDirectory = MainDirectory + '/pointsources'

#IRF 
DataFilesLiveTimeCubeDirectory = MainDirectory + '/LiveTimeCube'

DataFilesInstrumentResponseDirectory = MainDirectory + '/InstrumentResponse'

#   UltraClean
DataFilesInstrumentResponse4UltraDirectory = DataFilesInstrumentResponseDirectory + '/4Ultra'
DataFilesInstrumentResponse4UltraEffectiveAreaDirectory = \
    DataFilesInstrumentResponse4UltraDirectory + '/EffectiveArea'
DataFilesInstrumentResponse4UltraEnergyDispersionDirectory = \
    DataFilesInstrumentResponse4UltraDirectory + '/EnergyDispersion'
DataFilesInstrumentResponse4UltraPointSpreadFunctionDirectory = \
    DataFilesInstrumentResponse4UltraDirectory+'/PointSpreadFunction'




#GRAPHS:
GeneratedGraphsDirectory = '../GeneratedGraphs'

FermiEventsSkyMap                   = GeneratedGraphsDirectory + '/FermiEventsSkyMap'

FermiEventsSkyMapGalaxyGroupsMask    = GeneratedGraphsDirectory + '/FermiEventsSkyMapGalaxyGroupsMask'

FermiEventsSkyMapPointSourcesMask   = GeneratedGraphsDirectory + '/FermiEventsSkyMapPointSourcesMask'

FermiEventsSkyMapGalaxyGroupsAndPointSourcesMask = \
    GeneratedGraphsDirectory + '/FermiEventsSkyMapGalaxyGroupsAndPointSourcesMask'

FermiPointSourcesSkyMap             = GeneratedGraphsDirectory + '/FermiPointSourcesSkyMap'

FermiGalaxyGroupLikelihoodFits      = GeneratedGraphsDirectory + '/FermiGalaxyGroupLikelihoodFits'
