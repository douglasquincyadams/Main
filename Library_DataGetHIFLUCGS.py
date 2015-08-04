
"""
DESCRIPTION:


ARGS:
    Filepath1
        Type: Python String
        Description: Location of a highflux datafile
        

    Filepath2:
        Type: Python String
        Description: Location of a highflux datafile

    


    **Information About the 2 Files:
        NOTES:
            Each of the 2 files is formatted differently. 
        SOURCE:
            


        Filename1 && Filename2:
            Cname
                -> Name of the group

        Filename1:



            z
                -> distance

            RAdeg + DEdeg
                -> Galactic Longitude
                -> Galactic Latitude


        Filename2:

            M500
                -> Mass

    -----------------------------------
    Added:
    N
        -> Number of elements in the Group


RETURNS:
    Cluster Data Object:



"""
import numpy
import collections
#------------------------------------------------------------------------------
import Library_FileReadAsTwoDimensionalNumpyDataset
import Library_ArrayOfStringsStripTrailingWhiteSpace

import Config_AstronomyConstants as astroconst

import Library_AstronomyEquitoralDegreesToGalacticDegrees
import Library_AstronomyRedshiftToCentimeters
import Library_AstronomyDistanceFromEarthCmToApparentOutwardVelocityCmPerSec



def Main(Filepath1, Filepath2):
    #CREATE FILE SPECIFIC UNIT TRANSFORMATIONS:
    def HIFLUCGS_Filename1_RowUnitsTransform(row, HeaderRow):
        zIndex = HeaderRow.index('z')
        RAdegIndex = HeaderRow.index('RAdeg')
        DEdegIndex = HeaderRow.index('DEdeg')

        z = float(row[zIndex]  )
        RA = float(row[RAdegIndex] )
        DE = float(row[DEdegIndex] )

        l, b = Library_AstronomyEquitoralDegreesToGalacticDegrees.Main(RA, DE)

        Distance_in_cm = Library_AstronomyRedshiftToCentimeters.Main( float(row[zIndex]) )
        ClusterVelocity_in_cm_per_sec = Library_AstronomyDistanceFromEarthCmToApparentOutwardVelocityCmPerSec.Main(Distance_in_cm)

        row[zIndex] = ClusterVelocity_in_cm_per_sec
        row[RAdegIndex] = l
        row[DEdegIndex] = b
        return row

    def HIFLUCGS_Filename2_RowUnitsTransform(row, HeaderRow):
        Mass500Index = HeaderRow.index('M500')
        Mass_in_point7_times10tothe14_SolarMasses = float(row[Mass500Index])
        Mass_in_grams = Mass_in_point7_times10tothe14_SolarMasses * 0.7*(10.0**14.0)*astroconst.MassSolar_in_grams
        row[Mass500Index] =  Mass_in_grams
        return row


    #EXTRACT DATAFILE2:
    Delimeter = " "
    FirstDataLineNumber = 77    #number on gedit - 1
    HeaderLineNumber = 75       #number on gedit - 1
    ColumnNames             = ['M500'] 
    ColumnNamesCastFloat    = ['M500'] 

    Dataset1, Dataset1_StringPart = Library_FileReadAsTwoDimensionalNumpyDataset.Main(\
        Filepath = Filepath2, \
        Delimeter = Delimeter, \
        FirstDataLineNumber = FirstDataLineNumber,\
        HeaderLineNumber = HeaderLineNumber,\
        ColumnNames = ColumnNames,\
        ColumnNamesCastFloat = ColumnNamesCastFloat,\
        RowUnitTransformFunction = HIFLUCGS_Filename2_RowUnitsTransform,\
        FilterNone = True,\
        )

    #EXTRACT DATAFILE1
    Delimeter = " "
    FirstDataLineNumber = 82    #number on gedit - 1
    HeaderLineNumber = 80       #number on gedit - 1
    ColumnNames             = ['Cname', 'z', 'RAdeg', 'DEdeg'] 
    ColumnNamesCastFloat    = [         'z', 'RAdeg', 'DEdeg'] 

    Dataset2, Dataset2_StringPart = \
        Library_FileReadAsTwoDimensionalNumpyDataset.Main(\
            Filepath = Filepath1, \
            Delimeter = Delimeter, \
            FirstDataLineNumber = FirstDataLineNumber,\
            HeaderLineNumber = HeaderLineNumber,\
            ColumnNames = ColumnNames,\
            ColumnNamesCastFloat = ColumnNamesCastFloat,\
            RowUnitTransformFunction = HIFLUCGS_Filename1_RowUnitsTransform,\
            FilterNone = True,\
        )
 
    #FIX MISSING VALUES:
    Dataset_FloatPart_N = numpy.zeros(shape = (Dataset1.shape[0] , 1) ) + 1 #Assume 1 Galaxy per group
 

    #CONCATONETE THE FLOAT DATA:
    #Columns Needed: count, velocity, mass, long, lat
    N_array = Dataset_FloatPart_N
    Velocity_array = numpy.atleast_2d( Dataset2.T[0] ).T
    Mass_array = Dataset1
    Long_array = numpy.atleast_2d( Dataset2.T[1] ).T
    Lat_array = numpy.atleast_2d( Dataset2.T[2] ).T

    Dataset_FloatPart = numpy.concatenate( (N_array, Velocity_array, Mass_array, Long_array, Lat_array), axis = 1)


    #Get the group names (from dataset2 string part):
    GroupNameColumnNumber = 0
    Dataset_Names = numpy.atleast_2d( numpy.array( Library_ArrayOfStringsStripTrailingWhiteSpace.Main( Dataset2_StringPart.T[GroupNameColumnNumber].tolist() ) ) ).T

    #Save the data in a dictionary to return
    Info =  collections.OrderedDict()
    Info["ColumnNames"] = ['Cname', 'N', 'zVel', 'Mass500', 'Glong', 'Glat'] 
    Info["ColumnNamesCastFloat"] = ['N', 'zVel', 'Mass500', 'Glong', 'Glat'] 
    Info["FloatPart"] =  Dataset_FloatPart
    Info["StringPart"] = Dataset2_StringPart
    Info["Names"] = Dataset_Names
    return Info














