#!/usr/bin/env python


"""
Used by the DispersionFile
"""

"""Reads in the Dispersion file"""

import pyfits


#Main Function
def ReadEnergyDispersionFile(
    Filename_ED=None,
    ):

    hdulist_Edisp=pyfits.open(Filename_ED)

    print pyfits.info(Filename_ED)
    print hdulist_Edisp[2].data['EDISPSCALE'].shape
    print hdulist_Edisp[1].data['LS1']
    print hdulist_Edisp[1].columns
    
    ENERG_LO_Edisp=hdulist_Edisp[1].data['ENERG_LO']
    ENERG_HI_Edisp=hdulist_Edisp[1].data['ENERG_HI']
    CTHETA_LO_Edisp=hdulist_Edisp[1].data['CTHETA_LO']
    CTHETA_HI_Edisp=hdulist_Edisp[1].data['CTHETA_HI']
    NORM_Edisp=hdulist_Edisp[1].data['NORM']
    LS1_Edisp=hdulist_Edisp[1].data['LS1']
    LS2_Edisp=hdulist_Edisp[1].data['LS2']
    RS1_Edisp=hdulist_Edisp[1].data['RS1']
    RS2_Edisp=hdulist_Edisp[1].data['RS2']
    BIAS_Edisp=hdulist_Edisp[1].data['BIAS']

    return ENERG_LO_Edisp, ENERG_HI_Edisp, CTHETA_LO_Edisp,CTHETA_HI_Edisp,NORM_Edisp,LS1_Edisp,LS2_Edisp, RS1_Edisp,RS2_Edisp,BIAS_Edisp
    


def main():
    file_energyDispersion='edisp_P7REP_ULTRACLEAN_V15_back.fits'
    dir_Energydispersion= Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEnergyDispersionDirectory
    FileAndDir=dir_Energydispersion+'/'+file_energyDispersion

    ENERG_LO_Edisp,ENERG_HI_Edisp,CTHETA_LO_Edisp,CTHETA_HI_Edisp,NORM_Edisp,LS1_Edisp,LS2_Edisp, RS1_Edisp,RS2_Edisp,BIAS_Edisp=ReadEnergyDispersionFile(Filename_ED=FileAndDir)


    print ENERG_LO_Edisp, 
    print ENERG_HI_Edisp,
    print CTHETA_LO_Edisp,
    print CTHETA_HI_Edisp,
    print NORM_Edisp,
    print LS1_Edisp,
    print LS2_Edisp,
    print RS1_Edisp,
    print RS2_Edisp,
    print BIAS_Edisp

    return



if __name__ == '__main__':
    main()
