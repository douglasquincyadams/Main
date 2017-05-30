"""
SOURCE:

    Written by Douglas Spolyar

    #energy dispersion Function
    def DispersionFuctionFermiSat(

        ):   



DESCRIPTION:

    This is integrated 
        over the whole sky 
        over the whole time the telescope has been looking at the sky, 
    so it is a represenation of the 'on average' energy spectrum at a random point at a random time

    However - you do feed it a 
        -> which represents the energy of which you are looking for a source photon

    The Dispersion function represents 
        the photon energy specturm you would observe with the istrument
        If ALL the photons observed with NO INSTRUMENT ERROR had exact real energy == 'SourceEnergy'

    As a general rule, the higher the energy Center, the smaller the variace becomes up to 1TeV




ARGS:
    SourceEnergy
        Type: Float
        Description:
            The 'real' energy of the photons observed
    
    WindowMinimumEnergy=None,
        Type: Float
        Description:
            The absolute minimum possible observed(with error) energy 

    WindowMaximumEnergy=None,
        Type: Float
        Description:
            The absolute maximum possible observed(with error) energy 

RETURNS:
    EnergyDispersionFunction
        DESCRIPTION:
            Similar to a 1-d Gaussian, but is instead a peicewise interpolated thing from FERMI Fits files
            
            ARGS:
                Energy
                    Type: Python Float
                    
                    Desciption:
                        1-D pdf 
                        The probability density function of seeing  photons at arbitrary energies, 
                        once you have decided that a source energy is producing all of them
                        
                        Position on Sky, and Instrument Angle have been integrated away.
            RETURNS:
                ProbabilityDensityValue
                    Type: Python Float

TESTS:


"""


import numpy
import astropy
import astropy.io.fits
#------------------------------------------------------------------------------
import Const_LocalDirectoriesFermiFiles

import Library_AstropyFitsTablePrettyPrint

import DS_EnergyDispersion as EnDisp


def Main(
    SourceEnergy=None,
    WindowMinimumEnergy=None,
    WindowMaximumEnergy=None,
    PrintExtra = False,
    ):

    print '\n\n STARTING GENERATING ENERGY DISPERION FUNCTION\n\n'

    # energy Dispersion Files to be loaded


    #loadlivetime cube
    directoryofLivetimeCube = Const_LocalDirectoriesFermiFiles.DataFilesLiveTimeCubeDirectory
    LiveTimefile=directoryofLivetimeCube+'/exposurecube_filtered_events_10GeV_1TeV_zmax100_GTI_ultraclean.fits'


    #load effective area Front
    filenameEffArea_f='aeff_P7REP_ULTRACLEAN_V15_front.fits'
    directoryEffectiveArea= Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEffectiveAreaDirectory
    EAFile_f=directoryEffectiveArea+'/'+filenameEffArea_f
    
    #load dispersion function Front
    file_energyDispersion_f='edisp_P7REP_ULTRACLEAN_V15_front.fits'
    dir_Energydispersion=Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEnergyDispersionDirectory
    DispersonFile_f=dir_Energydispersion+'/'+file_energyDispersion_f

    #load effective area Back
    filenameEffArea_b='aeff_P7REP_ULTRACLEAN_V15_back.fits'
    directoryEffectiveArea=Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEffectiveAreaDirectory
    EAFile_b=directoryEffectiveArea+'/'+filenameEffArea_b

    #load dispersion function Back
    file_energyDispersion_b='edisp_P7REP_ULTRACLEAN_V15_back.fits'
    dir_Energydispersion=Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEnergyDispersionDirectory
    DispersonFile_b=dir_Energydispersion+'/'+file_energyDispersion_b
    
                 
    minEnergy=WindowMinimumEnergy/2.
    MaxEnergy=WindowMaximumEnergy*2.
    NumberOfEnergyDivisions=100	
    
    #Front of the Detector dispersion grid:
    SplineArray_f,Spline_ED_f = EnDisp.DataForSpline(
        LivetimeFile=LiveTimefile,
        EAFile=EAFile_f,
        DispersonFile=DispersonFile_f,
        Mchi=SourceEnergy,
        WindowEMIN=minEnergy,
        WindowEMAX=MaxEnergy,
        NumofInt_Divisions=10,
        NumberOfEnergyDivisions=NumberOfEnergyDivisions,
        WhicArray='Front',
        )


    #Back of the Detector dispersion grid:
    SplineArray_b,Spline_ED_b = EnDisp.DataForSpline(
        LivetimeFile=LiveTimefile,
        EAFile=EAFile_b,        
        DispersonFile=DispersonFile_b,
        Mchi=SourceEnergy,
        WindowEMIN=minEnergy,
        WindowEMAX=MaxEnergy,
        NumofInt_Divisions=10,
        NumberOfEnergyDivisions=NumberOfEnergyDivisions,
        WhicArray='back',
        )

 
    def EnergyDispersionFunction(
        Energy = None,
        ):
        #Average over the front and back detector
        ProbabilityDensityValue = 0.5*numpy.power(10,Spline_ED_b(Energy))+0.5*numpy.power(10,Spline_ED_f(Energy))           
        return ProbabilityDensityValue

    print '\n\n DONE GENERATING ENERGY DISPERION FUNCTION\n\n'


    return EnergyDispersionFunction

























