#!/usr/bin/env python 

import pyfits
import numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RectBivariateSpline
import DS_SkyExposure as SE
from scipy.interpolate import UnivariateSpline
from scipy.optimize import brentq
import JCluster as jc
from scipy.integrate import quad
import JclusterChris as jcluster

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
    CosAveLTcube,CosineLiveTimeData=SE.CosLTdataAndCTheta(filenameLTC,FileNumber=2)
    
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

    #print DicAve    
    return DicAve
    
def SplineFractionofsignalgivenR(
                                 r200=None,
                                 sigma=None,
                                ):

    frac=np.linspace(0.001,.99999,200)
    Dist=np.ones(200)
    for i, fraci in enumerate(frac):
        Dist[i]=jc.JClusterRadius(r200=r200,sigma=sigma,cl=fraci)
        #print Dist[i], fraci
    
    #print Dist, frac
    #distAddOn=np.linspace(Dist[-1]+.5,10*Dist[-1],5)
    #FracAddOn=np.ones(5)*1.0
    #Dist1=np.concatenate((Dist,distAddOn))
    #frac1=np.concatenate((frac,FracAddOn))
    func1=UnivariateSpline(Dist,frac,s=0,ext=3)
    #print 'Dist',Dist
    #plt.plot(Dist,frac)
    #plt.plot(Dist,func1(Dist))
    #plt.show()
    #amountofsignal=.95
    #print 'amountofsignal', amountofsignal
    #print 'Jcluster Angle', jc.JClusterRadius(r200=r200,sigma=sigma,cl=amountofsignal)
    return func1,Dist[-1]

def combinedRadius(r200=None,
                   sigmaCore=None,
                   sigmaTail=None,
                   fcore=None,
                   PhotonFrac=None,
                   ):
    #print 'sigmaCore',sigmaCore
    #print 'sigmaTail',sigmaTail
    SpCore,SpCoreRMax=SplineFractionofsignalgivenR(r200=r200,sigma=sigmaCore)
    SpTail,SpTailRMax=SplineFractionofsignalgivenR(r200=r200,sigma=sigmaTail)
    f1=lambda dist:fcore*SpCore(dist)+(1-fcore)*SpTail(dist)-PhotonFrac
    #distEl=np.linspace(0,100,1)
    #print 'distEl,f1(distEl)',distEl,f1(distEl)
    #plt.plot(distEl,f1(distEl))
    #plt.show()
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
           Position=None,
           ScalingParam=None,
           cl=None,
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
    if cl==.95:
        if ScalingParam=='Back':
             return SpE1*sig/np.sqrt(np.abs(1-1.57/gamma))*2**.5*.8
        return SpE1*sig/np.sqrt(np.abs(1-1.57/gamma))*2**.5*.9
    else:
        if ScalingParam=='Back':
            return SpE1*sig/np.sqrt(np.abs(1-1.66/gamma))*2**.5*.75
        return SpE1*sig/np.sqrt(np.abs(1-1.5/gamma))*2**.5*.7

def ChrisGauss(PSFel=None,
                Position=None,
                ScalingParam=None,
                cl=None,
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
   
    return SpE1*sig*np.sqrt(gamma/np.abs(gamma-1.5))
        
    
def King(x=None,
         sigma=None,
         gamma=None,
         Sp=None,
         ):
    return (sigma**2*Sp**2)**-1*(1-1/gamma)*(1+x**2/(2*gamma*sigma**2*Sp**2))**-gamma/2.

def intKing(x=None,
            sigma=None,
            gamma=None,
            Sp=None,
            ):
    gammaPower=-gamma+1
    return 1-(1.+(2*sigma**2*gamma*Sp**2)**-1*x**2)**gammaPower
            


def CombinedPSF(PSFel=None,
                ScalingParam=None,
                PhotonFrac=None,
                r200=None,
                ):
    """Returns the Radius of the Combined PSF"""
    CoreGauss=SGauss(PSFel=PSFel,Position='Core',ScalingParam=ScalingParam,cl=PhotonFrac)
    TailGauss= SGauss(PSFel=PSFel,Position='Tail',ScalingParam=ScalingParam,cl=PhotonFrac)
    Ntail=PSFel['NTAIL_AVE']
    Stail=PSFel['STAIL_AVE']
    Score=PSFel['SCOREL_AVE']
    fcore=1/(1+Ntail*Stail**2/Score**2)
    #fcore=1.
    #print 'fcore',fcore
    #print 'PhotonFrac',PhotonFrac
    RadiusOut=combinedRadius(r200=r200,sigmaTail=TailGauss,sigmaCore=CoreGauss,fcore=fcore,PhotonFrac=PhotonFrac)
    #print RadiusOut
    #print PSFel
    return RadiusOut

def ChrisDoubleGaussPSF(PSFel=None,
                        ScalingParam=None,
                        nsigma=None,
                        r200=None,
                        cl=None,
                        ):
    """Returns the Radius of the Combined PSF For Chris's function"""
    CoreGauss=ChrisGauss(PSFel=PSFel,Position='Core',ScalingParam=ScalingParam,cl=cl)
    TailGauss= ChrisGauss(PSFel=PSFel,Position='Tail',ScalingParam=ScalingParam,cl=cl)
    Ntail=PSFel['NTAIL_AVE']
    Stail=PSFel['STAIL_AVE']
    Score=PSFel['SCOREL_AVE']
    fcore=1/(1+Ntail*Stail**2/Score**2)
    return jcluster.JClusterRadius(r200=r200,sigma=[CoreGauss,TailGauss],w=[fcore,1-fcore],cl=cl)
                        

def CombinedKingRadius(PSFel=None,
                       cl=None,
                       DMmass=None,
                       ScalingParam=None,
                       ):
    Ntail=PSFel['NTAIL_AVE']
    Stail=PSFel['STAIL_AVE']
    Score=PSFel['SCOREL_AVE']
    Gcore=PSFel['GCORE_AVE']
    Gtail=PSFel['GTAIL_AVE']
    fcore=1/(1+Ntail*Stail**2/Score**2)
    SpEEvaluated=SpE(En=DMmass,ScalingParam=ScalingParam)

    IntKingCore=lambda x: intKing(x=x,sigma=Score,gamma=Gcore,Sp=SpEEvaluated)
    IntKingTail=lambda x: intKing(x=x,sigma=Stail,gamma=Gtail,Sp=SpEEvaluated)
    CoreMax=1000.*2*Score**2*Gcore
    TailMax=1000.*2*Stail**2*Gtail
   
    combIntKing=lambda x: fcore*IntKingCore(x)+(1-fcore)*IntKingTail(x)-cl

    return brentq(combIntKing,0.,np.max((CoreMax,TailMax)))             
                
def TestFitForDifferentMasses(SpDicfront=None,SpDicback=None,filenameLTC=None,):
    """
    shows the relative error for the different cases as a function of Mass
    """
    r200=.0
    
    DMmassRange=np.power(10,np.linspace(3,6,30))
    CombinedElementsDoug=np.ones(len(DMmassRange))
    KingElements=np.ones(len(DMmassRange))
    ChrisPSFelements=np.ones(len(DMmassRange))
 
    cl=.68
    ScalingParam='Back'
 
    for i,DMmass in enumerate(DMmassRange):
        print 'DMmass  ',DMmass
        PSFel=AvePSFelments(DMMass=DMmass,SpDic=SpDicback, filenameLTC=filenameLTC,)
        CombinedElementsDoug[i]=CombinedPSF(r200=r200,PSFel=PSFel,ScalingParam=ScalingParam,PhotonFrac=cl, )
        KingElements[i]=CombinedKingRadius(PSFel=PSFel,cl=cl,DMmass=DMmass,ScalingParam=ScalingParam)
        ChrisPSFelements[i]=ChrisDoubleGaussPSF(PSFel=PSFel,ScalingParam=ScalingParam,r200=r200,cl=cl)
        
    plt.figure(0)
    plt.loglog(DMmassRange,CombinedElementsDoug,c='blue',label='Dougs-Front')
    plt.loglog(DMmassRange,KingElements,c='red',label='KingsFunction-Front')
    plt.loglog(DMmassRange,ChrisPSFelements,c='black',label='Chris-Front')

    variation=np.abs(CombinedElementsDoug-KingElements)*2/(CombinedElementsDoug+KingElements)
    plt.loglog(DMmassRange,variation,c='green',ls='--',label='pecent Front')
    #plt.legend(loc=3)
    #plt.show()
           
    ScalingParam='Front'
    for i,DMmass in enumerate(DMmassRange):
        print 'DMmass  ',DMmass
        PSFel=AvePSFelments(DMMass=DMmass,SpDic=SpDicfront, filenameLTC=filenameLTC,)
        CombinedElementsDoug[i]=CombinedPSF(r200=r200,PSFel=PSFel,ScalingParam=ScalingParam,PhotonFrac=cl, )
        KingElements[i]=CombinedKingRadius(PSFel=PSFel,cl=cl,DMmass=DMmass,ScalingParam=ScalingParam)
        ChrisPSFelements[i]=ChrisDoubleGaussPSF(PSFel=PSFel,ScalingParam=ScalingParam,r200=r200,cl=cl)
        
    plt.loglog(DMmassRange,CombinedElementsDoug,c='blue',label='Dougs-Back')
    plt.loglog(DMmassRange,KingElements,c='red',label='KingsFunction-Back')
    plt.loglog(DMmassRange,ChrisPSFelements,c='black',label='Chris-Back')
    
    variation=np.abs(CombinedElementsDoug-KingElements)*2/(CombinedElementsDoug+KingElements)
    plt.loglog(DMmassRange,variation,c='green',ls=':',label='pecent Back')

    plt.title('68 percentile Confidence')
    plt.legend(loc=3)
    plt.xlabel('DM mass (MeV)')
    plt.ylabel('Degrees or percent')
   

    plt.figure(1)
    cl=0.95
    ScalingParam='Front'
    for i,DMmass in enumerate(DMmassRange):
        print 'DMmass  ',DMmass
        PSFel=AvePSFelments(DMMass=DMmass,SpDic=SpDicfront, filenameLTC=filenameLTC,)
        CombinedElementsDoug[i]=CombinedPSF(r200=r200,PSFel=PSFel,ScalingParam=ScalingParam,PhotonFrac=cl, )
        KingElements[i]=CombinedKingRadius(PSFel=PSFel,cl=cl,DMmass=DMmass,ScalingParam=ScalingParam)
        ChrisPSFelements[i]=ChrisDoubleGaussPSF(PSFel=PSFel,ScalingParam=ScalingParam,r200=r200,cl=cl)

    plt.loglog(DMmassRange,ChrisPSFelements,c='black',label='Chris-Front')
    plt.loglog(DMmassRange,CombinedElementsDoug,c='blue',label='Dougs-Front')
    plt.loglog(DMmassRange,KingElements,c='red',label='KingsFunction-Front')

    variation=np.abs(CombinedElementsDoug-KingElements)*2/(CombinedElementsDoug+KingElements)
    plt.loglog(DMmassRange,variation,c='green',ls='--',label='pecent Front')
    
    ScalingParam='Back'
    for i,DMmass in enumerate(DMmassRange):
        print 'DMmass  ',DMmass
        PSFel=AvePSFelments(DMMass=DMmass,SpDic=SpDicback, filenameLTC=filenameLTC,)
        CombinedElementsDoug[i]=CombinedPSF(r200=r200,PSFel=PSFel,ScalingParam=ScalingParam,PhotonFrac=cl, )
        KingElements[i]=CombinedKingRadius(PSFel=PSFel,cl=cl,DMmass=DMmass,ScalingParam=ScalingParam)
        ChrisPSFelements[i]=ChrisDoubleGaussPSF(PSFel=PSFel,ScalingParam=ScalingParam,r200=r200,cl=cl)

    plt.loglog(DMmassRange,CombinedElementsDoug,c='blue',label='Dougs-Back')
    plt.loglog(DMmassRange,KingElements,c='red',label='KingsFunction-Back')
    plt.loglog(DMmassRange,ChrisPSFelements,c='black',label='Chris-Back')

    variation=np.abs(CombinedElementsDoug-KingElements)*2/(CombinedElementsDoug+KingElements)
    plt.loglog(DMmassRange,variation,c='green',ls=':',label='pecent Back')

    plt.title('95 percentile Confidence')
    plt.legend(loc=3)
    plt.xlabel('DM mass (MeV)')
    plt.ylabel('Degrees or percent')




    plt.show()
    return           

def main():

    filenamePSFfront=Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraPointSpreadFunctionDirectory + '/psf_P7REP_ULTRACLEAN_V15_front.fits'
    filenamePSFback=Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraPointSpreadFunctionDirectory + '/psf_P7REP_ULTRACLEAN_V15_back.fits'
    
    filenameLTC=Const_LocalDirectoriesFermiFiles.DataFilesLiveTimeCubeDirectory+'/exposurecube_filtered_events_10GeV_1TeV_zmax100_GTI_ultraclean.fits'

    SpDicfront=SplineFits_PSF(filenamePSF=filenamePSFfront)
    SpDicback=SplineFits_PSF(filenamePSF=filenamePSFback)


    TestFitForDifferentMasses(SpDicfront=SpDicfront,SpDicback=SpDicback,filenameLTC=filenameLTC,)

    



if __name__ == '__main__':
    main()
