"""
DESCRIPTION:
    Aggregates Galaxy Cluster && Galaxy Catalogs
        HIFLUCGS
        MCXC
        2MASS { z < 0.01  &&  N > 1}
        2MASS { Velocities between 3,000 and 10,000 km/s  &&  N>=1 }

        To Add:
            2Mass { z < 0.01 && N == 1}
            CMB Catalog

    Calculates Jfactor from:
        Mass
        Z <~OR~> Radial Velocity
        
    Makes Plots Of:
        Mass
        Distance 
        SkyLocation
        VisualRadius* (which we calculate to be a function of of Mass && Distance)
        GroupGalaxyCount

"""


#------------------------------------------------------------------------------
import Const_LocalDirectoriesGalaxyGroupsFiles
import Library_DataGetAllGalaxyGroups 
import Library_GraphGalaxyGroupData
import Library_MemoryLimit

#SET MEMORY LIMIT TO N-GIGABYTES (Avoid Crashing Computer):
Library_MemoryLimit.Main(Bytes = 4*1000000000) 

#Define constants:
DirectorySourceDataFiles = Const_LocalDirectoriesGalaxyGroupsFiles.SourceDataFiles
DirectoryGeneratedGraphs = Const_LocalDirectoriesGalaxyGroupsFiles.GeneratedGraphs

print "====================RUN START======================="

"""
DatasetNameSets = [             
    ["DataHIFLUCGS"],           
    ["DataMCXC"],               
    ["Data2MassTullyNorth"],    
    ["Data2MassTullySouth"],    
    ["Data2MassMakarov"],       
    ]
"""

DatasetNameSets = [["Data2MassTullyNorth", "Data2MassTullySouth"]] 

for DatasetNames in DatasetNameSets:
    print "====DatasetNames: ", 
    print DatasetNames
    print "=================="
    FullClusterFloatPart, FullClusterFloatPartColumnNames = Library_DataGetAllGalaxyGroups.Main(DatasetNames = DatasetNames, DirectorySourceDataFiles = DirectorySourceDataFiles)
    Library_GraphGalaxyGroupData.Main( FullClusterFloatPart, FullClusterFloatPartColumnNames, DatasetNames , DirectoryGeneratedGraphs )



















