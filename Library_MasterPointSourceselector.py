#!/usr/bin/env python
"""
Different fields for the Point Source library
ColDefs(
    name = 'Source_Name'; format = '18A'
    name = 'RAJ2000'; format = 'E'; unit = 'deg'; disp = 'F8.4'
    name = 'DEJ2000'; format = 'E'; unit = 'deg'; disp = 'F8.4'
    name = 'GLON'; format = 'E'; unit = 'deg'; disp = 'F8.4'
    name = 'GLAT'; format = 'E'; unit = 'deg'; disp = 'F8.4'
    name = 'Conf_68_SemiMajor'; format = 'E'; unit = 'deg'; disp = 'F8.4'
    name = 'Conf_68_SemiMinor'; format = 'E'; unit = 'deg'; disp = 'F8.4'
    name = 'Conf_68_PosAng'; format = 'E'; unit = 'deg'; disp = 'F8.3'
    name = 'Conf_95_SemiMajor'; format = 'E'; unit = 'deg'; disp = 'F8.4'
    name = 'Conf_95_SemiMinor'; format = 'E'; unit = 'deg'; disp = 'F8.4'
    name = 'Conf_95_PosAng'; format = 'E'; unit = 'deg'; disp = 'F8.3'
    name = 'ROI_num'; format = 'I'
    name = 'Signif_Avg'; format = 'E'; disp = 'F8.3'
    name = 'Pivot_Energy'; format = 'E'; unit = 'MeV'; disp = 'F10.2'
    name = 'Flux_Density'; format = 'E'; unit = 'photon/cm**2/MeV/s'; disp = 'E10.4'
    name = 'Unc_Flux_Density'; format = 'E'; unit = 'photon/cm**2/MeV/s'; disp = 'E10.4'
    name = 'Flux1000'; format = 'E'; unit = 'photon/cm**2/s'; disp = 'E10.4'
    name = 'Unc_Flux1000'; format = 'E'; unit = 'photon/cm**2/s'
    name = 'Energy_Flux100'; format = 'E'; unit = 'erg/cm**2/s'; disp = 'E10.4'
    name = 'Unc_Energy_Flux100'; format = 'E'; unit = 'erg/cm**2/s'; disp = 'E10.4'
    name = 'Signif_Curve'; format = 'E'; disp = 'F10.2'
    name = 'SpectrumType'; format = '16A'
    name = 'Spectral_Index'; format = 'E'; disp = 'F8.4'
    name = 'Unc_Spectral_Index'; format = 'E'; disp = 'F8.4'
    name = 'beta'; format = 'E'; disp = 'F8.4'
    name = 'Unc_beta'; format = 'E'; disp = 'F8.4'
    name = 'Cutoff'; format = 'E'; unit = 'MeV'; disp = 'F10.2'
    name = 'Unc_Cutoff'; format = 'E'; unit = 'MeV'; disp = 'F10.2'
    name = 'Exp_Index'; format = 'E'; disp = 'F8.4'
    name = 'Unc_Exp_Index'; format = 'E'; disp = 'F8.4'
    name = 'PowerLaw_Index'; format = 'E'; disp = 'F8.4'
    name = 'Flux30_100'; format = 'E'; unit = 'photon/cm**2/s'
    name = 'Unc_Flux30_100'; format = 'E'; unit = 'photon/cm**2/s'
    name = 'nuFnu30_100'; format = 'E'; unit = 'erg/cm**2/s'
    name = 'Sqrt_TS30_100'; format = 'E'; disp = 'F8.3'
    name = 'Flux100_300'; format = 'E'; unit = 'photon/cm**2/s'
    name = 'Unc_Flux100_300'; format = '2E'; unit = 'photon/cm**2/s'
    name = 'nuFnu100_300'; format = 'E'; unit = 'erg/cm**2/s'
    name = 'Sqrt_TS100_300'; format = 'E'; disp = 'F8.3'
    name = 'Flux300_1000'; format = 'E'; unit = 'photon/cm**2/s'
    name = 'Unc_Flux300_1000'; format = '2E'; unit = 'photon/cm**2/s'
    name = 'nuFnu300_1000'; format = 'E'; unit = 'erg/cm**2/s'
    name = 'Sqrt_TS300_1000'; format = 'E'; disp = 'F8.3'
    name = 'Flux1000_3000'; format = 'E'; unit = 'photon/cm**2/s'
    name = 'Unc_Flux1000_3000'; format = '2E'; unit = 'photon/cm**2/s'
    name = 'nuFnu1000_3000'; format = 'E'; unit = 'erg/cm**2/s'
    name = 'Sqrt_TS1000_3000'; format = 'E'; disp = 'F8.3'
    name = 'Flux3000_10000'; format = 'E'; unit = 'photon/cm**2/s'
    name = 'Unc_Flux3000_10000'; format = '2E'; unit = 'photon/cm**2/s'
    name = 'nuFnu3000_10000'; format = 'E'; unit = 'erg/cm**2/s'
    name = 'Sqrt_TS3000_10000'; format = 'E'; disp = 'F8.3'
    name = 'Flux10000_100000'; format = 'E'; unit = 'photon/cm**2/s'
    name = 'Unc_Flux10000_100000'; format = '2E'; unit = 'photon/cm**2/s'
    name = 'nuFnu10000_100000'; format = 'E'; unit = 'erg/cm**2/s'
    name = 'Sqrt_TS10000_100000'; format = 'E'; disp = 'F8.3'
    name = 'Variability_Index'; format = 'E'
    name = 'Signif_Peak'; format = 'E'
    name = 'Flux_Peak'; format = 'E'; unit = 'photon/cm**2/s'
    name = 'Unc_Flux_Peak'; format = 'E'; unit = 'photon/cm**2/s'
    name = 'Time_Peak'; format = 'D'; unit = 's'
    name = 'Peak_Interval'; format = 'E'; unit = 's'
    name = 'Flux_History'; format = '48E'; unit = 'photon/cm**2/s'
    name = 'Unc_Flux_History'; format = '96E'; unit = 'photon/cm**2/s'; dim = '( 2, 48)'
    name = 'Extended_Source_Name'; format = '18A'
    name = '0FGL_Name'; format = '17A'
    name = '1FGL_Name'; format = '18A'
    name = '2FGL_Name'; format = '18A'
    name = '1FHL_Name'; format = '18A'
    name = 'ASSOC_GAM1'; format = '15A'
    name = 'ASSOC_GAM2'; format = '14A'
    name = 'ASSOC_GAM3'; format = '15A'
    name = 'TEVCAT_FLAG'; format = 'A'
    name = 'ASSOC_TEV'; format = '21A'
    name = 'CLASS1'; format = '5A'
    name = 'ASSOC1'; format = '26A'
    name = 'ASSOC2'; format = '26A'
    name = 'Flags'; format = 'I'
)
"""



import Library_LoadPointSources
import Library_PSF

import Utility_masterConfig as config
import Library_LoadPointSources
import Library_SelectPointSources

def Main(DMMass=None):
    
    if DMMass==None:
        DMMass=1.e5

    #Spline to determine radius
    PS_Spline=Library_PSF.Main(DMMass=DMMass,ConfidenceLevel=config.ConfidenceLevel)
    PSF=PS_Spline(0.)
    print PSF
    print config.ConfidenceLevel

    #Load PointSources
    PointSourcesData,SurfProjPointSourceLoc3D,SurfProjPointSourceLocRadii=Library_LoadPointSources.Main(PSF=PSF)
    print PointSourcesData.columns

    Library_SelectPointSources.Main(PointSources=PointSourcesData,DMMass=DMMass,MaxEnergy=DMMass*1.3,
         MinEnergy=DMMass/1.3,  )
    
    return 


if __name__ == '__main__':
    Main()


    
