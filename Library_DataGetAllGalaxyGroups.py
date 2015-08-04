"""
DESCRIPTION:
    Get all the data clusters from the following sources:
        HIFLUCGS
        MCXC
        2MASS { z < 0.01  &&  N > 1}
        2MASS { Velocities between 3,000 and 10,000 km/s  &&  N>=1 }

        To Add:
            2Mass { z < 0.01 && N == 1}
            CMB Catalog

ARGS:
    DatasetNames:
        [
        "DataHIFLUCGS",           
        "DataMCXC",               
        "Data2MassTullyNorth",    
        "Data2MassTullySouth",    
        "Data2MassMakarov", 
        ]
RETURNS:
    FullClusterFloatPart
        Type: `Type_TwoDimensionalNumpyArray`
        Description: Contains all the data we need about Galaxy clusters to make graphs

    FullClusterFloatPartColumnNames
        Type: Python List
        Description:
            [
            "GalaxyCount"
            "VelocityInCmPerSec"
            "MassInGrams"
            "GalacticLongitudeInDegrees"
            "GalacticLatitudeInDegrees"
            "DistanceInCm"
            "Jsmooth"
            "RvirInCm"
            "VisualAngleInDegrees"           #-> assumes that the sun is in the same place as the fermi telescope
            "IntensityInJPerDegreesSquared"
            "Jclumpy"
            ]

"""
from astropy.cosmology import FlatLambdaCDM
from scipy import stats
import matplotlib.pyplot as plt
import numpy
import collections
import os

#------------------------------------------------------------------------------

import Library_FileReadAsTable
import Library_FileReadAsTwoDimensionalNumpyDataset
import Library_ArrayOfStringsStripTrailingWhiteSpace
import Library_PrintDatasetStatistics

import Config_AstronomyConstants as astroconst
import Library_AstronomyVisualAngleDegreeEstimation
import Library_AstronomyJsmoothIntensity

import Library_DataGetHIFLUCGS
import Library_DataGetMCXC
import Library_DataGet2MassTully
import Library_DataGet2MassMakarov



#def Library_DataGetClusterAll():
def Main( 
    DatasetNames = [], 
    DirectorySourceDataFiles = None, 
    CheckArguments = True,
    PrintExtra = False,
    
    ):

    if (CheckArguments):
        ArgumentErrorMessage = ""
        if ( len(DatasetNames) < 1 ):
            ArgumentErrorMessage +=  "( len(DatasetNames) < 1 )\n"

        if ( str(type( DatasetNames )) !=  "<type 'list'>") :
            ArgumentErrorMessage +=  "str( type(DatasetNames) ) != <type 'list'>\n" 

        for DatasetName in DatasetNames:
            if (str( type(DatasetName) ) != "<type 'str'>" ) :
                ArgumentErrorMessage +=  "Each DatasetName must be of type string: "
                ArgumentErrorMessage +=  "str( type("+str(DatasetName)+") ) != <type 'str'>\n" 
        if (len(ArgumentErrorMessage) > 0 ):
            ArgumentErrorMessage = "\n" + ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)
    

    #Basic Astronomy Equations:
    def Distance_From_Velocity(velocity_in_cm_per_sec):                 #(in_cm) DONE
        velocity_in_km_per_sec = velocity_in_cm_per_sec / astroconst.Km_in_cm      #(in_km)
        distance_in_MegaParsecs =  velocity_in_km_per_sec / astroconst.H0          #(in Mpcs)
        distance_in_cm = distance_in_MegaParsecs * astroconst.MegaParsec_in_cm     #(in cm)
        return distance_in_cm #(in cm)

    def Rvir_From_Mass(MassCluster_in_grams):#(in_cm) DONE
        Rvir_Numerator = ( MassCluster_in_grams * 3.0 ) #(grams)
        Rvir_Denominator = ( 4.0 * numpy.pi * 200.0 * astroconst.RhoCritical_in_grams_per_cm_cubed ) #(grams / cm^3)
        Rvir = ( Rvir_Numerator / Rvir_Denominator ) ** (1.0/3.0) #(in_cm)
        return Rvir #(in_cm)

    #Dark Matter Equations:
    def ConcentrationParameter_From_MassCluster(MassCluster_in_grams): #(no units) DONE 
        ConcentrationParameter_Numerator = (MassCluster_in_grams) #(in_grams)
        ConcentrationParameter_Denominator = (2.0*(10.0**12.0)*(astroconst.h**(-1.0)) * astroconst.MassSolar_in_grams) #(grams)

        ConcentrationParameter = 5.74*( (ConcentrationParameter_Numerator / ConcentrationParameter_Denominator) ** (-0.097) ) #(no units)
        return ConcentrationParameter #(no units)

    def RhoS_From_Mass( MassCluster_in_grams):  #(in_grams_per_cm_cubed) DONE
        ConcentrationParameter = ConcentrationParameter_From_MassCluster(MassCluster_in_grams)  #(no units)

        RhoS_Numerator = (200.0 * (ConcentrationParameter**(3.0) ) * astroconst.RhoCritical_in_grams_per_cm_cubed ) #(grams_per_cm_cubed)
        RhoS_Denominator = 3.0 * ( numpy.log(1.0 + ConcentrationParameter) - (ConcentrationParameter/(1.0 + ConcentrationParameter)) ) #(no units)
        RhoS = RhoS_Numerator / RhoS_Denominator #(grams_per_cm_cubed)
        return RhoS  #(in_grams_per_cm_cubed)

    def Jsmooth_From_MassClusterAndDistanceCluster(MassCluster_in_grams, DistanceCluster_in_cm): #(no units)
        Rvir = Rvir_From_Mass(MassCluster_in_grams) #(in_cm)
        ConcentrationParameter = ConcentrationParameter_From_MassCluster(MassCluster_in_grams)  #(no units)
        Rs = Rvir / ConcentrationParameter #(in_cm)
        RhoS = RhoS_From_Mass( MassCluster_in_grams ) #(in_grams_per_cm_cubed)

        Jsmooth_Numerator = (4.0 * numpy.pi * (RhoS**2.0) * (Rs**3.0) ) #(gm^2 / cm^3 )
        Jsmooth_Denominator = (3.0 * (DistanceCluster_in_cm **2.0) ) # (cm^2)
        Jsmooth = (Jsmooth_Numerator / Jsmooth_Denominator) * astroconst.Jsmooth_NormalizationTerm #(no_units)
        return Jsmooth #(no_units)

    def Jclumpy_From_Jsmooth(Jsmooth):
        Jclumpy = astroconst.JClumpyBoostFactor * Jsmooth #(no_units)
        return Jclumpy #(no_units)

    def TestVirgo():
        #Known Virgo Values:
        Virgo_Distance_in_Mpcs = 16.8 
        Virgo_Mass_in_SolarMass = 7.5 * (10.0**14.0)
        Virgo_RVir_degrees = 6.2
        Virgo_Real_Jsmooth = 1.2 * ( 10**(-3.0) )

        #Virgo Caluclated values
        Virgo_Distance_in_cm = Virgo_Distance_in_Mpcs * MegaParsec_in_cm
        print "Virgo_Distance_in_cm: \n", Virgo_Distance_in_cm , "\n"

        Virgo_Mass_in_grams = Virgo_Mass_in_SolarMass * MassSolar_in_grams
        print "Virgo_Mass_in_grams: \n", Virgo_Mass_in_grams, "\n"

        Virgo_RVir_in_cm = Rvir_From_Mass(Virgo_Mass_in_grams )
        print "Virgo_RVir_in_cm: \n", Virgo_RVir_in_cm, "\n"

        Virgo_ConcentrationParameter = ConcentrationParameter_From_MassCluster( Virgo_Mass_in_grams )   
        print "Virgo_ConcentrationParameter: \n", Virgo_ConcentrationParameter, "\n"

        Virgo_Rs_in_cm = Virgo_RVir_in_cm / Virgo_ConcentrationParameter
        print "Virgo_Rs_in_cm: \n", Virgo_Rs_in_cm, "\n"

        Virgo_RhoS_in_grams_per_cm_cubed = RhoS_From_Mass( Virgo_Mass_in_grams )
        print "Virgo_RhoS_in_grams_per_cm_cubed: \n",  Virgo_RhoS_in_grams_per_cm_cubed, "\n"

        Jsmooth = Jsmooth_From_MassClusterAndDistanceCluster(Virgo_Mass_in_grams, Virgo_Distance_in_cm)
        print "Jsmooth: \n", Jsmooth, "\n"

        #Virgo Sanity Comparisons:
        print "Jsmooth / Virgo_Real_Jsmooth: \n" , Jsmooth / Virgo_Real_Jsmooth, "\n"


    def PrintClusterInfoObject(  \
        ClusterSetInfo = None,   \
        PrintLineHeader = "",  \
        PrintLineBufferSize = 0, \
        ):
        SpaceBuffer = " "*PrintLineBufferSize

        if (len(PrintLineHeader) > 0):
            print PrintLineHeader

        for key in ClusterSetInfo:
            print SpaceBuffer, key, " Count", len(ClusterSetInfo[key])
            #print SpaceBuffer, ClusterSetInfo[key][0:5]

            
        print "ColumnNamesCastFloat: ", ClusterSetInfo["ColumnNamesCastFloat"]
        print ""






    ExtractionFloatPartColumnNames = ["GalaxyCount", "VelocityInCmPerSec", "MassInGrams", "GalacticLongitudeInDegrees", "GalacticLatitudeInDegrees"]
    ListOfDatasets = []

    #EXTRACT
    if ( ( "DataHIFLUCGS" in DatasetNames) or (DatasetNames == []) ):
        print "DataHIFLUCGS..."
        Filepath1 = DirectorySourceDataFiles + '/Hiflucgs_FULL_01.txt'
        Filepath2 = DirectorySourceDataFiles + '/Hiflucgs_FULL_02.txt'
        DataHIFLUCGS = Library_DataGetHIFLUCGS.Main(Filepath1 = Filepath1, Filepath2 = Filepath2)
        PrintClusterInfoObject( DataHIFLUCGS )
        ListOfDatasets.append(DataHIFLUCGS)

    if ( ( "DataMCXC" in DatasetNames) or (DatasetNames == []) ):
        print "DataMCXC..."
        Filepath = DirectorySourceDataFiles + '/MCXC_1700_FULL.tsv'  
        DataMCXC = Library_DataGetMCXC.Main( Filepath = Filepath )
        PrintClusterInfoObject(DataMCXC )
        ListOfDatasets.append(DataMCXC)

    if ( ( "Data2MassTullyNorth" in DatasetNames) or (DatasetNames == []) ):
        print "Data2MassTullyNorth..."
        Filepath = DirectorySourceDataFiles + '/2Mass_3461_North_FULL.txt'
        Data2MassTullyNorth = Library_DataGet2MassTully.Main(Filepath = Filepath)
        PrintClusterInfoObject(Data2MassTullyNorth )
        ListOfDatasets.append(Data2MassTullyNorth)

    if ( ( "Data2MassTullySouth" in DatasetNames) or (DatasetNames == []) ):
        print "Data2MassTullySouth"
        Filepath = DirectorySourceDataFiles + '/2Mass_3461_South_FULL.txt'
        Data2MassTullySouth = Library_DataGet2MassTully.Main(Filepath = Filepath)
        PrintClusterInfoObject(Data2MassTullySouth )
        ListOfDatasets.append(Data2MassTullySouth)

    if ( ( "Data2MassMakarov" in DatasetNames) or (DatasetNames == []) ):
        print "Data2MassMakarov"
        Filepath = DirectorySourceDataFiles + '/2Mass_395_FULL.tsv'
        Data2MassMakarov = Library_DataGet2MassMakarov.Main(Filepath = Filepath)
        PrintClusterInfoObject(Data2MassMakarov)
        ListOfDatasets.append(Data2MassMakarov)

    ListOfFloatParts = []
    ListOfNameParts = []
    for Dataset in ListOfDatasets:
        ListOfFloatParts.append(Dataset["FloatPart"])
        ListOfNameParts.append(Dataset["Names"])


    #CONCAT
    #print "Concatenate FloatParts..."
    AllClusterFloatPart = numpy.concatenate(    \
        tuple(ListOfFloatParts) ,               \
        axis=0                                  \
    )
    #print "AllClusterFloatPart.shape", AllClusterFloatPart.shape

    #print "Concatenate Names..."
    AllClusterNames = numpy.concatenate(        \
        tuple(ListOfNameParts) ,                \
        axis=0                                  \
    )
    #print "AllClusterNames.shape", AllClusterNames.shape

    #FILTER
    #print "Filtering Rows Which Contain 0.0 Values (Clearly Errors): "
    RowIndex = 0
    RemovedIndexes = []
    for Row in AllClusterFloatPart:
        if (0.0 in Row):
            RemovedIndexes.append(RowIndex)
        RowIndex += 1
    AllClusterFloatPartFiltered = numpy.delete(AllClusterFloatPart, RemovedIndexes, 0)
    #print "AllClusterFloatPartFiltered.shape", AllClusterFloatPartFiltered.shape

    AllClusterNamesFiltered = numpy.delete(AllClusterNames, RemovedIndexes, 0)
    #print "AllClusterNamesFiltered.shape", AllClusterNamesFiltered.shape


    #EXTEND (Calculates Jfactor)
    ExtendedFloatPartColumnNames = [ "DistanceInCm", "Jsmooth", "RvirInCm", "VisualAngleInDegrees", "IntensityInJPerDegreesSquared", "Jclumpy"]

    Distance    = Distance_From_Velocity(AllClusterFloatPartFiltered[:,[ExtractionFloatPartColumnNames.index("VelocityInCmPerSec")]])
    Jsmooth     = Jsmooth_From_MassClusterAndDistanceCluster(\
        AllClusterFloatPartFiltered[:,[ExtractionFloatPartColumnNames.index("MassInGrams")]] , \
        Distance \
        )
    Rvir        = Rvir_From_Mass(AllClusterFloatPartFiltered[:,[ExtractionFloatPartColumnNames.index("MassInGrams")]])
    VisualAngle = Library_AstronomyVisualAngleDegreeEstimation.Main(Distance, Rvir) #-> assumes that the sun is in the same place as the fermi telescope
    Intensity   = Library_AstronomyJsmoothIntensity.Main(VisualAngle, Jsmooth)
    Jclumpy     = Jclumpy_From_Jsmooth(Jsmooth)


    FullClusterFloatPartColumnNames = ExtractionFloatPartColumnNames + ExtendedFloatPartColumnNames
    FullClusterFloatPart = numpy.concatenate( (AllClusterFloatPartFiltered, Distance, Jsmooth, Rvir, VisualAngle, Intensity, Jclumpy ), axis = 1 )

    #PRINT STATISTICS ABOUT THE DATA OBTAINED (We do one column at a time for readability):
    #TODO:  Change units for statistics printing:
    #   grams->SolarMasses
    #       MassInGrams
    #   cm/s -> km/s
    #       VelocityInCmPerSec
    #   cm -> MegaParsecs
    #       DistanceInCm
    #       RvirInCm
    if (PrintExtra):
        for ColumnName in FullClusterFloatPartColumnNames:
            Library_PrintDatasetStatistics.Main(FullClusterFloatPart[:,[FullClusterFloatPartColumnNames.index(ColumnName) ]], ColumnName, 4 )


    return FullClusterFloatPart, FullClusterFloatPartColumnNames















