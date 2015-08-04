#!/usr/bin/env python
"""calculates exposure on the sky over a healpix"""

import DS_EffectiveArea as EA
import DS_ReadingLiveTimeCube as RLTcube
import pyfits
from scipy.interpolate import RectBivariateSpline
import matplotlib.pyplot as plt
import numpy as np
import healpy as hp

def calcExposure(
        CosineLiveTimeData=None,
        CosAveLTcube=None,
        SplineEA=None,
        EnergyScalelog10=None,
        
        ):
    """calculates the exposure for a single healpix"""
    numofhealpix=CosineLiveTimeData.shape[0]
    Exposure=np.ones(numofhealpix)
    ExposureTest=CosineLiveTimeData[1]*SplineEA.ev(CosAveLTcube,EnergyScalelog10)
    #plt.plot(CosAveLTcube,ExposureTest)
    #plt.show()
    for i in np.arange(0,numofhealpix):
        Exposure[i]=np.sum(CosineLiveTimeData[i]*SplineEA.ev(CosAveLTcube,EnergyScalelog10))

    
    return Exposure

def CosLTdataAndCTheta(
        filnameAndDir=None,
        FileNumber=2, #"Use the Weighted exposure"
        ):
    """returns the the lifetime data for each healpix and the locations of the average bins for the healpix data FileNumber specifies using the weighted exposure"""
    CosineLiveTimeData,RAdata,DECdata,CThetaMax_LTCube,CThetaMin_LTCube=RLTcube.ReadLiveTimeCubeHealpixFile(filnameAndDir,FileNumber=2)
    CosAveLTcube=(CThetaMax_LTCube+CThetaMin_LTCube)/2.

    return CosAveLTcube,CosineLiveTimeData

def ReturnSplineofEffectiveArea(
        filnameAndDir=None,
        ):
    """Spline of Effective Area as a function of Energy and CTheta. Energy is interms of log10 of 1MeV"""
    print pyfits.info( filnameAndDir) 
    CTHETA_LO_EA, CTHETA_HI_EA, energyLow_EA, energyHigh_EA, EFFAREA =EA.importEffectiveArea(filnameAndDir)
    energylogEA, CthetaEA=EA.centeringDataAndConvertingToLog(energyHigh_EA,energyLow_EA,CTHETA_HI_EA,CTHETA_LO_EA)
    SplineEA=RectBivariateSpline(CthetaEA,energylogEA,EFFAREA)
    return SplineEA

def ExposureHP(
        FileandDir_EA=None,
        FileandDir_livetime=None,
        EnergyScalelog10=None,
               ):
    """outputs the exposure on the sky interms of a healpix"""
    CosAveLTcube,CosineLiveTimeData=CosLTdataAndCTheta(filnameAndDir=FileandDir_livetime)
    SplineEA=ReturnSplineofEffectiveArea(filnameAndDir=FileandDir_EA)
    return calcExposure(CosineLiveTimeData=CosineLiveTimeData, CosAveLTcube=CosAveLTcube,SplineEA=SplineEA,EnergyScalelog10=EnergyScalelog10)
    
def main():
    directoryofLivetimeCube='../TestIRFs/LiveTimeCube/'
    FileandDir_livetime=directoryofLivetimeCube+'exposurecube_filtered_events_10GeV_1TeV_zmax100_GTI_ultraclean.fits'
   
    filenameEffArea='aeff_P7REP_ULTRACLEAN_V15_back.fits'
    directoryEffectiveArea='../TestIRFs/EffectiveArea/'  
    FileandDir_EA=directoryEffectiveArea+filenameEffArea
   
    Exposure_b=ExposureHP(FileandDir_EA=FileandDir_EA,FileandDir_livetime=FileandDir_livetime,EnergyScalelog10=4.)


    filenameEffArea='aeff_P7REP_ULTRACLEAN_V15_front.fits'
    directoryEffectiveArea='../TestIRFs/EffectiveArea/'  
    FileandDir_EA=directoryEffectiveArea+filenameEffArea
   
    Exposure_f=ExposureHP(FileandDir_EA=FileandDir_EA,FileandDir_livetime=FileandDir_livetime,EnergyScalelog10=4.)

    Exposure_c=(Exposure_b+Exposure_f)*1.e4

    hp.mollview(Exposure_c,nest=True)
    plt.show()
    
    
    

    


if __name__ == '__main__':
    main()
