#!/usr/bin/env python 

import pyfits
import numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RectBivariateSpline

from scipy.interpolate import UnivariateSpline
from scipy.optimize import brentq
from scipy.integrate import quad

import Trash_JCluster
import Library_DataGetFermiInstrumentResponseSkyExposurePass7
import Const_LocalDirectoriesFermiFiles

def SplineFits_PSF(filenamePSF=None):
    hdulist=pyfits.open(filenamePSF)
    
    energyLow=hdulist[1].data['ENERG_LO'][0]
    energyHigh=hdulist[1].data['ENERG_HI'][0]
    CTHETA_LO=hdulist[1].data['CTHETA_LO'][0]
    CTHETA_HI=hdulist[1].data['CTHETA_HI'][0]
    EnergyAve=np.log10(energyLow*.5+energyHigh*.5)
    CTHETA_AVE=CTHETA_HI*.5+CTHETA_LO*.5

    Spl_NCORE=RectBivariateSpline(EnergyAve,CTHETA_AVE,hdulist[1].data['NCORE'][0].T)
    Spl_NTAIL=RectBivariateSpline(EnergyAve,CTHETA_AVE,hdulist[1].data['NTAIL'][0].T)
    Spl_SCORE=RectBivariateSpline(EnergyAve,CTHETA_AVE,hdulist[1].data['SCORE'][0].T)
    Spl_STAIL=RectBivariateSpline(EnergyAve,CTHETA_AVE,hdulist[1].data['STAIL'][0].T)
    Spl_GCORE=RectBivariateSpline(EnergyAve,CTHETA_AVE,hdulist[1].data['GCORE'][0].T)
    Spl_GTAIL=RectBivariateSpline(EnergyAve,CTHETA_AVE,hdulist[1].data['GTAIL'][0].T)


    splineDictionary={'Spl_NCORE':Spl_NCORE,
                      'Spl_NTAIL':Spl_NTAIL,
                      'Spl_SCORE':Spl_SCORE,
                      'Spl_STAIL':Spl_STAIL,
                      'Spl_GCORE':Spl_GCORE,
                      'Spl_GTAIL':Spl_GTAIL,
                      'energyLow':energyLow,
                      'energyHigh':energyHigh,
                      'CTHETA_LO':CTHETA_LO,
                      'CTHETA_HI':CTHETA_HI,
                      'EnergyAve':EnergyAve,
                      'CTHETA_AVE':CTHETA_AVE,
                      }
                      

    return splineDictionary

def plot_SPF_Test(Filename=None,
                  Dictionary=None,
                  SpName=None,
                  ):
    """plot the output for the different splines"""
    SpDic=Dictionary
    filenamePSF=Filename
    
    EnergyAve=SpDic['EnergyAve']
    CTHETA_AVE=SpDic['CTHETA_AVE']
    numPoints=40000
    deltaEnergy=EnergyAve[-1]-EnergyAve[0]
    deltaCtheta=CTHETA_AVE[-1]-CTHETA_AVE[0]
    Energypoints=numpy.random.rand(numPoints)*(deltaEnergy)+EnergyAve.T[0]
    Cthetapoints=numpy.random.rand(numPoints)*(deltaCtheta)+CTHETA_AVE.T[0]

    Spl=SpDic[SpName]
    hdulist=pyfits.open(filenamePSF)
    plt.subplot(121)
    plt.scatter(Energypoints,Cthetapoints,c=Spl.ev(Energypoints,Cthetapoints),linewidth=0.)
    plt.subplot(122)
    plt.imshow(np.flipud(hdulist[1].data['NCORE'][0]),aspect='auto')
    plt.show()

    return

def AvePSFelments(DMMass=None,
                  SpDic=None,
                  filenameLTC=None,
                  ):

    #livetimedata 
    CosAveLTcube,CosineLiveTimeData=\
        Library_DataGetFermiInstrumentResponseSkyExposurePass7.CosLTdataAndCTheta(
            filenameLTC,
            FileNumber=2
            )
    
    #generate an averaged livetime Cube.
    numofhealpix= CosineLiveTimeData.shape[0]
    AveHealpix=CosineLiveTimeData[0]
    for i in np.arange(1,numofhealpix):
        AveHealpix=AveHealpix+CosineLiveTimeData[i]
    NormHealpix=np.sum(AveHealpix)
    WeightedHealpix=AveHealpix/NormHealpix

    
    log10DMmass=np.log10(DMMass)
    NCORE_AVE=np.average(SpDic['Spl_NCORE'].ev(log10DMmass,CosAveLTcube),weights=WeightedHealpix)
    NTAIL_AVE=np.average(SpDic['Spl_NTAIL'].ev(log10DMmass,CosAveLTcube),weights=WeightedHealpix)
    SCOREL_AVE=np.average(SpDic['Spl_SCORE'].ev(log10DMmass,CosAveLTcube),weights=WeightedHealpix)
    STAIL_AVE=np.average(SpDic['Spl_STAIL'].ev(log10DMmass,CosAveLTcube),weights=WeightedHealpix)
    GCORE_AVE=np.average(SpDic['Spl_GCORE'].ev(log10DMmass,CosAveLTcube),weights=WeightedHealpix)
    GTAIL_AVE=np.average(SpDic['Spl_GTAIL'].ev(log10DMmass,CosAveLTcube),weights=WeightedHealpix)
    """
    #print NCORE_AVE,NTAIL_AVE
    testAngle=.6
    NCORE_AVE=np.average(SpDic['Spl_NCORE'].ev(log10DMmass,testAngle))
    NTAIL_AVE=np.average(SpDic['Spl_NTAIL'].ev(log10DMmass,testAngle))
    SCOREL_AVE=np.average(SpDic['Spl_SCORE'].ev(log10DMmass,testAngle))
    STAIL_AVE=np.average(SpDic['Spl_STAIL'].ev(log10DMmass,testAngle))
    GCORE_AVE=np.average(SpDic['Spl_GCORE'].ev(log10DMmass,testAngle))
    GTAIL_AVE=np.average(SpDic['Spl_GTAIL'].ev(log10DMmass,testAngle))
    """
    
    DicAve={'NCORE_AVE':NCORE_AVE,
            'NTAIL_AVE':NTAIL_AVE,
            'SCOREL_AVE':SCOREL_AVE,
            'STAIL_AVE':STAIL_AVE,
            'GCORE_AVE':GCORE_AVE,
            'GTAIL_AVE':GTAIL_AVE,
            'DMMass':DMMass,
            }

    print DicAve    
    return DicAve
    
def SplineFractionofsignalgivenR(
                                 r200=None,
                                 sigma=None,
                                ):

    frac=np.linspace(0.001,.99999,200)
    Dist=np.ones(200)
    for i, fraci in enumerate(frac):
        Dist[i]=Trash_JCluster.JClusterRadius(r200=r200,sigma=sigma,cl=fraci)
        #print Dist[i], fraci
    
    #print Dist, frac
    #distAddOn=np.linspace(Dist[-1]+.5,10*Dist[-1],5)
    #FracAddOn=np.ones(5)*1.0
    #Dist1=np.concatenate((Dist,distAddOn))
    #frac1=np.concatenate((frac,FracAddOn))
    func1=UnivariateSpline(Dist,frac,s=0,ext=3)
    #print Dist1
    #plt.plot(Dist,frac)
    #plt.plot(Dist,func1(Dist))
    #plt.show()
    amountofsignal=.95
    print 'amountofsignal', amountofsignal
    print 'Jcluster Angle', Trash_JCluster.JClusterRadius(r200=r200,sigma=sigma,cl=amountofsignal)
    return func1,Dist[-1]

def combinedRadius(r200=None,
                   sigmaCore=None,
                   sigmaTail=None,
                   fcore=None,
                   PhotonFrac=None,
                   ):
    SpCore,SpCoreRMax=SplineFractionofsignalgivenR(r200=r200,sigma=sigmaCore)
    SpTail,SpTailRMax=SplineFractionofsignalgivenR(r200=r200,sigma=sigmaTail)
    f1=lambda dist:fcore*SpCore(dist)+(1-fcore)*SpTail(dist)-PhotonFrac
    if PhotonFrac>.99999: print 'exceed limit'
    return brentq(f1,0.,np.max((SpCoreRMax,SpTailRMax)))                      

def SpE(En=None,
        ScalingParam=None,
        ):
    if ScalingParam=='Front':
        c0=5.53e-2
        c1=5.90e-4
        beta=0.8
    else:
        c0=9.29e-2
        c1=1.68e-3
        beta=0.8
    return np.degrees(np.sqrt((c0*(En/100)**-beta)**2+c1**2)) #Energy in units of MeV

def SGauss(PSFel=None,
           Position='Core',
           ScalingParam='Front',
           ):
    DMMass=PSFel['DMMass']
    #print 'DMMass',DMMass
    SpE1=SpE(En=DMMass,ScalingParam=ScalingParam)
    if Position=='Core':
        gamma=PSFel['GCORE_AVE']
        sig=PSFel['SCOREL_AVE']
    else:
        gamma=PSFel['GTAIL_AVE']
        sig=PSFel['STAIL_AVE']
    #print 'gamma',gamma
    #print 'sig',sig
    #return np.sqrt(gamma/(gamma-0.5))*SpE1*sig*1.65
    #return .68**(1/(1-gamma))*np.sqrt(2*gamma)*SpE1*sig
    #return np.sqrt(gamma)*SpE1*sig
    return SpE1*sig/np.sqrt(1-1/gamma)*np.sqrt(2.)

def King(x=None,
         sigma=None,
         gamma=None,
         Sp=None,
         ):
    return (sigma**2*Sp**2)**-1*(1-1/gamma)*(1+x**2/(2*gamma*sigma**2*Sp**2))**-gamma/2.


def InVertCLandRadius(function=None,
                      Parms=None,
                      ):
    return

def CombinedPSF(PSFel=None,
                ScalingParam=None,
                PhotonFrac=None,
                ):
    """Returns the Radius of the Combined PSF"""
    CoreGauss=SGauss(PSFel=PSFel,Position='Core',ScalingParam=ScalingParam)
    TailGauss= SGauss(PSFel=PSFel,Position='Tail',ScalingParam=ScalingParam)
    Ntail=PSFel['NTAIL_AVE']
    Stail=PSFel['STAIL_AVE']
    Score=PSFel['SCOREL_AVE']
    fcore=1/(1+Ntail*Stail**2/Score**2)
    #fcore=1.
    print 'fcore',fcore
    print 'PhotonFrac',PhotonFrac
    RadiusOut=combinedRadius(r200=0.0,sigmaTail=TailGauss,sigmaCore=CoreGauss,fcore=fcore,PhotonFrac=PhotonFrac)
    print RadiusOut
    print PSFel
    return RadiusOut

             
                
             
def main():
    PSFdir = Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraPointSpreadFunctionDirectory
    LTCdir = Const_LocalDirectoriesFermiFiles.DataFilesLiveTimeCubeDirectory

    filenamePSF=PSFdir+ '/psf_P7REP_ULTRACLEAN_V15_back.fits'
    
    filenameLTC=LTCdir + '/exposurecube_filtered_events_10GeV_1TeV_zmax100_GTI_ultraclean.fits'

    SpDic=SplineFits_PSF(filenamePSF=filenamePSF)

    #plot_SPF_Test(Filename=filenamePSF, Dictionary=SpDic, SpName='Spl_NCORE',)

    PSFel=AvePSFelments(DMMass=1.e4,SpDic=SpDic, filenameLTC=filenameLTC,)
    #print 'SpE'
    #print SpE(En=1e5,ScalingParam='Front'), SpE(En=1e5,ScalingParam='Back')
    #print 'guass'
    #print SGauss(PSFel=PSFel,Position='Core',ScalingParam='Front'), SGauss(PSFel=PSFel,Position='Tail',ScalingParam='Front')

    CombinedPSF(PSFel=PSFel,ScalingParam='Back',PhotonFrac=.95, )
    
    

if __name__ == '__main__':
    main()
