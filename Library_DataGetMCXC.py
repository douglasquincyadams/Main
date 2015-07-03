"""
DESCRIPTION:

    REFERENCE:
        http://arxiv.org/abs/1007.1916


    FILE COLUMNS:

        MCXC
            -> Name of the group
        z
            -> redshift (which can be used to find distance)

        M500
            -> mass
            -> units of 10^14 solarMasses

        _Glon
            -> Galactic coordinates in degrees 

        _Glat
            -> Galactic coordinates in degrees

        ----------------------------
        Added:
        N
            -> Number of elements in group

RETURNS:
        #Columns Needed: count, velocity, mass, long, lat

"""
import numpy
import collections
#------------------------------------------------------------------------------
import Library_FileReadAsTwoDimensionalNumpyDataset
import Library_ArrayOfStringsStripTrailingWhiteSpace

import Config_AstronomyConstants as astroconst

import Library_AstronomyRedshiftToCentimeters
import Library_AstronomyDistanceFromEarthCmToApparentOutwardVelocityCmPerSec


def Main(Filepath = None):
    def Dataset_MCXC_1700_RowUnitTransform(row, HeaderRow):
        VelocityIndex = HeaderRow.index('z')
        MassIndex = HeaderRow.index('M500')

        #Convert Distance from redshift to cm
        Distance_in_cm = Library_AstronomyRedshiftToCentimeters.Main( Redshift = float(row[VelocityIndex]) )

        #ClusterVelocity_in_cm_per_sec = Velocity_From_Distance(Distance_in_cm)
        ClusterVelocity_in_cm_per_sec = Library_AstronomyDistanceFromEarthCmToApparentOutwardVelocityCmPerSec.Main(Distance_in_cm)

        #Convert Mass from SolarMasses to grams
        ClusterMass_in_10to14_SolarMasses = float(row[MassIndex])
        ClusterMass_in_grams = ClusterMass_in_10to14_SolarMasses * astroconst.MassSolar_in_grams * (10.0**14.0)

        row[VelocityIndex] = ClusterVelocity_in_cm_per_sec 
        row[MassIndex] = ClusterMass_in_grams
        return row

    #EXTRACT DATAFILE:
    Delimeter = ";"
    FirstDataLineNumber = 83    #number on gedit - 1
    HeaderLineNumber = 80       #number on gedit - 1
    ColumnNames = ['MCXC', 'z', 'M500',  '_Glon', '_Glat'] 
    ColumnNamesCastFloat = ['z', 'M500',  '_Glon', '_Glat']

    Dataset_FloatPart, Dataset_StringPart = \
        Library_FileReadAsTwoDimensionalNumpyDataset.Main(\
            Filepath = Filepath, \
            Delimeter = Delimeter, \
            FirstDataLineNumber = FirstDataLineNumber,\
            HeaderLineNumber = HeaderLineNumber,\
            ColumnNames = ColumnNames,\
            ColumnNamesCastFloat = ColumnNamesCastFloat,\
            RowUnitTransformFunction = Dataset_MCXC_1700_RowUnitTransform, \
            )

    #FIX MISSING VALUES: (Cram in a 1 for the group count)
    Dataset_FloatPart_N = numpy.zeros(shape = (Dataset_FloatPart.shape[0] , 1) ) + 1

    #CONCATONETE THE FLOAT DATA:
    #Columns Needed: count, velocity, mass, long, lat
    Dataset_FloatPart = numpy.concatenate( (Dataset_FloatPart_N, Dataset_FloatPart), axis = 1)

    #Get the group names (from Dataset_StringPart):
    GroupNameColumnNumber = 0
    Dataset_Names = numpy.atleast_2d( numpy.array( Library_ArrayOfStringsStripTrailingWhiteSpace.Main( Dataset_StringPart.T[GroupNameColumnNumber].tolist() ) ) ).T

    ColumnNames.insert(1, 'N')
    ColumnNamesCastFloat.insert(0,'N')

    #Save the data in a dictionary to return
    Info =  collections.OrderedDict()
    Info["ColumnNames"] = ColumnNames
    Info["ColumnNamesCastFloat"] = ColumnNamesCastFloat
    Info["FloatPart"] =  Dataset_FloatPart
    Info["StringPart"] = Dataset_StringPart
    Info["Names"] = Dataset_Names
    return Info














