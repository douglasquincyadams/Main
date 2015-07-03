import Library_DataGetAllGalaxyGroups
import Const_LocalDirectoriesGalaxyGroupsFiles
import Library_PrintDatasetStatistics
import Config_AstronomyConstants


#Get the groups:
GroupSourcesDirectorySourceDataFiles = Const_LocalDirectoriesGalaxyGroupsFiles.SourceDataFiles
GroupSourcesCatalogs            = ["Data2MassTullyNorth", "Data2MassTullySouth"] ##all together now
GroupSourcesData, GroupSourcesDataColumnNames = Library_DataGetAllGalaxyGroups.Main(DatasetNames = GroupSourcesCatalogs, DirectorySourceDataFiles = GroupSourcesDirectorySourceDataFiles)


#Print Mass Information
GalaxyGroupMasses   = GroupSourcesData[:,[GroupSourcesDataColumnNames.index("MassInGrams")] ]
GalaxyGroupMasses = GalaxyGroupMasses / Config_AstronomyConstants.MassSolar_in_grams
Library_PrintDatasetStatistics.Main(GalaxyGroupMasses, "GalaxyGroupMasses", 1)


#ERROR HANDLING:
#Library_DataGetAllGalaxyGroups.Main(DatasetNames = "asdf" )
#Library_DataGetAllGalaxyGroups.Main(DatasetNames = [] )
#Library_DataGetAllGalaxyGroups.Main(DatasetNames = [4] )
#Library_DataGetAllGalaxyGroups.Main(DatasetNames = [4,5] )
#Library_DataGetAllGalaxyGroups.Main(DatasetNames = ["",5] )
#Library_DataGetAllGalaxyGroups.Main(DatasetNames = [["asdf"],["asdf1"]] )
