"""
Returns:
    Table:
        Columns are:
            PGC1 
                -> Name of the brightest Galaxy in the group
            Nest 
                -> Name of the Group
            Ng 
                -> Number of members of the group
            Vgp 
                -> Velocity in km /s
            L_Mass12 
                -> Mass in SolarMasses * 10**12 
                -> based on corrected intrinsic luminosity and M/L prescription

            GLong 
                -> Galactic Coordinates
                -> Galactic longitude
                -> Degrees
            GLat 
                -> Galactic Coordinates
                -> Galactic latitude
                -> Degrees

"""
import numpy
import collections
#------------------------------------------------------------------------------
import Library_FileReadAsTwoDimensionalNumpyDataset
import Library_ArrayOfStringsStripTrailingWhiteSpace

import Config_AstronomyConstants as astroconst



def Main(Filepath = None):
    def RawDataset_3461_RowUnitTransform(row, HeaderRow):
        VelocityIndex = HeaderRow.index('Vgp')
        MassIndex = HeaderRow.index('L_Mass12')

        #Convert Velocity to cm/s
        ClusterVelocity_in_km_per_sec = float(row[VelocityIndex])
        ClusterVelocity_in_cm_per_sec = ClusterVelocity_in_km_per_sec * astroconst.Km_in_cm

        #Convert Mass to grams
        ClusterMass_in_solarMasses = float(row[MassIndex])
        ClusterMass_in_grams = ClusterMass_in_solarMasses * astroconst.MassSolar_in_grams * (10**12)

        row[VelocityIndex] = ClusterVelocity_in_cm_per_sec 
        row[MassIndex] = ClusterMass_in_grams
        return row

    Delimeter = ","
    FirstDataLineNumber = 5
    HeaderLineNumber = 1
    ColumnNames = ['Nest', 'Ng', 'Vgp', 'L_Mass12','GLong', 'GLat']
    ColumnNamesCastFloat = ['Ng', 'Vgp', 'L_Mass12','GLong', 'GLat']

    #Get the FloatPart:
    GalaxyDataset_3461_FloatPart, GalaxyDataset_3461_StringPart = \
        Library_FileReadAsTwoDimensionalNumpyDataset.Main(\
            Filepath = Filepath, \
            Delimeter = Delimeter, \
            FirstDataLineNumber = FirstDataLineNumber,\
            HeaderLineNumber = HeaderLineNumber,\
            ColumnNames = ColumnNames,\
            ColumnNamesCastFloat = ColumnNamesCastFloat,\
            RowUnitTransformFunction = RawDataset_3461_RowUnitTransform,\
            )
    
    #Get the group names:
    GroupNameColumnNumber = 0
    GalaxyDataset_3461_GroupNames = Library_ArrayOfStringsStripTrailingWhiteSpace.Main( GalaxyDataset_3461_StringPart.T[GroupNameColumnNumber].tolist() )

    #Need to aggregate rows which are part of the same group or 'Nest'
    GroupIndexes = collections.OrderedDict()
    k = 0
    for GroupName in GalaxyDataset_3461_GroupNames:
        if ( GroupName in GroupIndexes ):
            GroupIndexes[GroupName].append(k)
        else:
            GroupIndexes[GroupName] = [k]
        k = k + 1
    NumUniqueGroups = len(GroupIndexes)
    
    #Define the containers which have the correctly transformed data:
    GroupDataset_FloatPart = numpy.zeros(shape = (NumUniqueGroups ,GalaxyDataset_3461_FloatPart.shape[1]  ))
    GroupDataset_StringPart = numpy.zeros(shape = ( NumUniqueGroups, GalaxyDataset_3461_StringPart.shape[1] ))
    GroupDataset_Names = numpy.atleast_2d( numpy.array(list(GroupIndexes.keys())) ).T

    k = 0
    for GroupName in GroupIndexes:
        Index = GroupIndexes[GroupName][0]
        GroupDataset_FloatPart[k] = GalaxyDataset_3461_FloatPart[Index]
        GroupDataset_StringPart[k] = GalaxyDataset_3461_StringPart[Index]
        k = k + 1

    Info =  collections.OrderedDict()
    Info["ColumnNames"] = ColumnNames
    Info["ColumnNamesCastFloat"] = ColumnNamesCastFloat
    Info["FloatPart"] = GroupDataset_FloatPart
    Info["StringPart"] = GroupDataset_StringPart
    Info["Names"] = GroupDataset_Names
    return Info 

