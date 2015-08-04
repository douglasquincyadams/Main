
"""
Returns:
    Table:
        Columns are:
            Group 
                -> Name of brightest group member

            N   
                -> Number of group members with known radial velocities

            VLG 
                -> Velocity in km/s
                    Mean radial velocity of the group relative 
                    to the centroid of the Local Group
                    Includes both the motion relative to us,
                    AND it includes the local bulk motion 
            logM 
                -> log10( Mass ) in SolarMasses
            _Glon
                -> Galactic coordinates in degrees 

            _Glat
                -> Galactic coordinates in degrees

            ########################################################
            NOT REQUIRED:
            Rh -> Mean harmonic radius
                -> is defined as the inverse of the mean distance 
                    between all pairs of particles in the halo:
                -> at its computation the distance to the group 
                    <D> was determined from the mean radial velocity 
                    with the Hubble parameter H0=73km/s/Mpc.
                -> dbUnit:	kiloparsec = 3.0857*10 + 19m
            RAJ2000 
                -> Equatorial Coordinates
                -> Right ascension of group's main member
                -> Type:   real value, representing a sexagesimal right ascension
                -> dbUnit: milli-second of arc = 7.71605*10-10
            DEJ2000
                -> Equatorial Coordinates
                -> Declination of the group's main member 
                -> Type:   real value, possibly sexagesimal
                -> dbUnit: milli-second of arc = 7.71605*10-10
"""

import numpy
import collections
#------------------------------------------------------------------------------
import Library_FileReadAsTwoDimensionalNumpyDataset
import Library_ArrayOfStringsStripTrailingWhiteSpace

import Config_AstronomyConstants as astroconst


def Main(Filepath = None):
    #DEFINE A UNIT TRANSFORMATION
    def RawDataset_395_RowUnitTransform(row, HeaderRow):
        VelocityIndex = HeaderRow.index('VLG')
        MassIndex = HeaderRow.index('logM')

        #Convert Velocity from km/s to cm/s
        ClusterVelocity_in_km_per_sec = float(row[VelocityIndex])
        ClusterVelocity_in_cm_per_sec = ClusterVelocity_in_km_per_sec * astroconst.Km_in_cm

        #Convert Mass from SolarMasses to grams
        Log10_ClusterMass_Over_SolarMass = float(row[MassIndex])
        ClusterMass_Over_SolarMass = 10.0**Log10_ClusterMass_Over_SolarMass
        ClusterMass_in_grams = ClusterMass_Over_SolarMass * astroconst.MassSolar_in_grams

        row[VelocityIndex] = ClusterVelocity_in_cm_per_sec 
        row[MassIndex] = ClusterMass_in_grams
        return row

    #EXTRACT THE DATA
    Delimeter = ";"
    FirstDataLineNumber = 72    #number on gedit - 1
    HeaderLineNumber = 69       #number on gedit - 1
    ColumnNames = ['Group', 'N', 'VLG', 'logM', '_Glon', '_Glat'] 
    ColumnNamesCastFloat = ['N', 'VLG', 'logM', '_Glon', '_Glat']

    Dataset_395_FloatPart, Dataset_StringPart = \
        Library_FileReadAsTwoDimensionalNumpyDataset.Main(\
            Filepath = Filepath, \
            Delimeter = Delimeter, \
            FirstDataLineNumber = FirstDataLineNumber,\
            HeaderLineNumber = HeaderLineNumber,\
            ColumnNames = ColumnNames,\
            ColumnNamesCastFloat = ColumnNamesCastFloat,\
            RowUnitTransformFunction = RawDataset_395_RowUnitTransform, \
        )

    #Get the group names:
    GroupNameColumnNumber = 0
    Dataset_Names = numpy.atleast_2d( numpy.array( Library_ArrayOfStringsStripTrailingWhiteSpace.Main( Dataset_StringPart.T[GroupNameColumnNumber].tolist() ) ) ).T

    #Save the data in a dictionary to return
    Info =  collections.OrderedDict()
    Info["ColumnNames"] = ColumnNames
    Info["ColumnNamesCastFloat"] = ColumnNamesCastFloat
    Info["FloatPart"] =  Dataset_395_FloatPart
    Info["StringPart"] = Dataset_StringPart
    Info["Names"] = Dataset_Names
    return Info



