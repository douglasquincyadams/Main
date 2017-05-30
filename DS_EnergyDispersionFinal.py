#!/usr/bin/env python


import pyfits
import numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RectBivariateSpline
from scipy.interpolate import interp1d
from astropy.coordinates import SkyCoord
from scipy.interpolate import InterpolatedUnivariateSpline
import DS_EffectiveArea as EA
import DS_ReadingLiveTimeCube as RLTcube

import DS_SkyExposure as SE

import DS_ReadDispersionFile as RDfile
import pylab as py
from scipy.integrate import quad
from scipy.integrate import dblquad
from scipy.integrate import nquad

def Ave2elements(element1,element2, weight1=1.,weight2=1.):
    return (element1*weight1+element2*weight2)/2.

def log10Ave2elements(element1,element2, weight1=1.,weight2=1.):
    return np.log10((element1*weight1+element2*weight2)/2.)



def SplinesforDispersionEq(
        FileAndDir_ED=None,
        ):
    ENERG_LO_Edisp,ENERG_HI_Edisp,CTHETA_LO_Edisp,CTHETA_HI_Edisp,NORM_Edisp,LS1_Edisp,LS2_Edisp,RS1_Edisp,RS2_Edisp,BIAS_Edisp=RDfile.ReadEnergyDispersionFile(Filename_ED=FileAndDir_ED)
    EnergAVE_EDISP=Ave2elements(ENERG_HI_Edisp,ENERG_LO_Edisp)
    CTHETAAVE_EDISPlog10=np.log10(Ave2elements(CTHETA_HI_Edisp,CTHETA_LO_Edisp))

    x=CTHETAAVE_EDISPlog10[0]
    y=EnergAVE_EDISP[0]
    
    NORMSPLINE=RectBivariateSpline(x=x,y=y,z=NORM_Edisp[0])
    LS1SPLINE=RectBivariateSpline(x=x,y=y,z=LS1_Edisp[0])
    LS2SPLINE=RectBivariateSpline(x=x,y=y,z=LS2_Edisp[0])
    RS1SPLINE=RectBivariateSpline(x=x,y=y,z=RS1_Edisp[0])
    RS2SPLINE=RectBivariateSpline(x=x,y=y,z=RS2_Edisp[0])
    BIASSPLINE=RectBivariateSpline(x=x,y=y,z=BIAS_Edisp[0])

    #PlotofDispersionFunctions(splinefunction=RS1SPLINE,OriginalArray=RS1_Edisp[0],energy=y,Ctheta=x)

    return NORMSPLINE,LS1SPLINE,LS2SPLINE,RS1SPLINE,RS2SPLINE,BIASSPLINE


def findhealpixbyRAandDEC(
        Filename=None,
        ):
    """returns  the index of the elements and their number"""
    RA_LiveTimeCube,DEC_LiveTimeCube=RLTcube.RAandDECofLiveTimeCube(Filename)
    
    c=SkyCoord(RA_LiveTimeCube,DEC_LiveTimeCube,frame='icrs',unit='deg').icrs
    #indxofhealpix=py.find(np.abs(c.galactic.b.deg)>30.)
    indxofhealpix=py.find(np.abs(DEC_LiveTimeCube)<20)
    numofhealpix= len(indxofhealpix)
    return indxofhealpix,numofhealpix

def plotdifferentEsposuresFordifferntenergies(
        SplineEA=None,
        CosAveLTcube=None,
        AveHealpix=None,
        ):
    EnergyScalelog10=4.
    AveExposureFuncofCTheta=SplineEA.ev(CosAveLTcube,EnergyScalelog10)*AveHealpix
    plt.plot(CosAveLTcube,AveExposureFuncofCTheta,c='blue')
    EnergyScalelog10=3.
    AveExposureFuncofCTheta=SplineEA.ev(CosAveLTcube,EnergyScalelog10)*AveHealpix
    plt.plot(CosAveLTcube,AveExposureFuncofCTheta,c='green')
    EnergyScalelog10=5.
    AveExposureFuncofCTheta=SplineEA.ev(CosAveLTcube,EnergyScalelog10)*AveHealpix
    plt.plot(CosAveLTcube,AveExposureFuncofCTheta,c='red')
    plt.show()
    return




def Snorm_EnergyDispersion(
        CTheta=None,
        logEnergy=None,
        WhicArray=None,
        ):
    """plotted in logbase 10 with a norm of MeV"""
    if(WhicArray=='Front'):
        Celements=np.array([0.021,0.058,-0.207,-0.213,0.042,0.564])
        #print 'Front'
    else: #back arrray
        Celements=np.array([0.0215,0.0507,-0.220,-0.243,0.065,0.584])
        #print 'Back'
    S1=Celements[0]*logEnergy**2+Celements[1]*CTheta**2+Celements[2]*logEnergy+Celements[3]*CTheta
    return S1+Celements[4]*CTheta*logEnergy+Celements[5]


def EnergyDisperison(
                    DeltaE=None,
                    CTheta=None,
                    Dic=None,
                    y=None,
                    ):
    cth=CTheta    
    Mchi=Dic['Mchi']
    Norm=Dic['Norm'].ev(cth,y)
    LS1=Dic['LS1'].ev(cth,y)
    LS2=Dic['LS2'].ev(cth,y)
    RS1=Dic['RS1'].ev(cth,y)
    RS2=Dic['RS2'].ev(cth,y)
    Bias=Dic['Bias'].ev(cth,y)
    WhicArray=Dic['WhicArray']
    """Energy Dispersion function"""
    NormLeft=Norm*np.exp(-np.abs((1.5)/LS1)**1.6/2.)*np.exp(np.abs((1.5)/LS2)**0.6/2.)
    NormRight=Norm*np.exp(-np.abs((1.5)/RS1)**1.6/2.)*np.exp(np.abs((1.5)/RS2)**0.6/2.)
    Xboundary=1.5
    x=(DeltaE-Mchi)/Mchi/Snorm_EnergyDispersion(logEnergy=np.log10(Mchi),CTheta=CTheta,WhicArray=WhicArray)
    if((x-Bias)<=-Xboundary):
        N=NormLeft
        sig=LS2
        gamma=0.6
        return N*np.exp(-0.5*np.abs((x-Bias)/sig)**gamma)
    if((x-Bias)>=Xboundary):
        N=NormRight
        sig=RS2
        gamma=0.6
        return N*np.exp(-0.5*np.abs((x-Bias)/sig)**gamma)
    if((x-Bias)<0&(x-Bias)>-Xboundary):
        N=Norm
        sig=LS1
        gamma=1.6
        return N*np.exp(-0.5*np.abs((x-Bias)/sig)**gamma)
    if((x-Bias)>0 & (x-Bias)<Xboundary):
        N=Norm
        sig=RS1
        gamma=1.6
        return N*np.exp(-0.5*np.abs((x-Bias)/sig)**gamma)



def ED_array(
        DeltaE=None,
        CTheta=None,
        Dic=None,
        y=None
        ):
    cth=CTheta    
    Mchi=Dic['Mchi']
    Norm=Dic['Norm'].ev(cth,y)
    LS1=Dic['LS1'].ev(cth,y)
    LS2=Dic['LS2'].ev(cth,y)
    RS1=Dic['RS1'].ev(cth,y)
    RS2=Dic['RS2'].ev(cth,y)
    Bias=Dic['Bias'].ev(cth,y)
    WhicArray=Dic['WhicArray']


    """Energy Dispersion function"""
    NormLeft=Norm*np.exp(-0.5*np.abs((-1.5)/LS1)**1.6)*np.exp(0.5*np.abs((-1.5)/LS2)**0.6)
    NormRight=Norm*np.exp(-0.5*np.abs((-1.5)/RS1)**1.6)*np.exp(0.5*np.abs((-1.5)/RS2)**0.6)
    Xboundary=1.5
    x=np.array((DeltaE-Mchi)/Mchi/Snorm_EnergyDispersion(logEnergy=np.log10(Mchi),CTheta=CTheta,WhicArray=WhicArray))
    cond1= x-Bias<= -Xboundary
    def f1(x):
        N=NormLeft
        sig=LS2
        gamma=0.6
        return N*np.exp(-0.5*np.abs((x-Bias)/sig)**gamma)
    cond2=x-Bias>= Xboundary
    def f2(x):    
        N=NormRight
        sig=RS2
        gamma=0.6
        return N*np.exp(-0.5*np.abs((x-Bias)/sig)**gamma)
    cond3=(x<Bias)&(x-Bias>-Xboundary)
    def f3(x):
        N=Norm
        sig=LS1
        gamma=1.6
        return N*np.exp(-0.5*np.abs((x-Bias)/sig)**gamma)
    cond4=(x>Bias)&(x-Bias<Xboundary)
    def f4(x):    
        N=Norm
        sig=RS1
        gamma=1.6
        return N*np.exp(-0.5*np.abs((x-Bias)/sig)**gamma)
    return np.piecewise(x,[cond1,cond2,cond3,cond4],[f1,f2,f3,f4])


def WeightedExposure(LivetimeFile=None,
                    EAFile=None,
                    y=None,
                    ):
    """main console. reads in Data, and gives back the dispersion function as a interpolating function"""
    #livetimedata 
    CosAveLTcube,CosineLiveTimeData=SE.CosLTdataAndCTheta(LivetimeFile,FileNumber=2)

    #generate an averaged livetime Cube.
    numofhealpix= CosineLiveTimeData.shape[0]
    AveHealpix=CosineLiveTimeData[0]
    for i in np.arange(1,numofhealpix):
        AveHealpix=AveHealpix+CosineLiveTimeData[i]

    #Effective Area


    SplineEA=SE.ReturnSplineofEffectiveArea(EAFile)
    EffArea=SplineEA.ev(CosAveLTcube,y)#arrea of the effective area
    for i,el in enumerate(EffArea):
        if EffArea[i]<0.: EffArea[i]=1.0e-6
    TotalExposure=np.sum(EffArea*AveHealpix)
    WeightedEffArea=EffArea*AveHealpix/TotalExposure
    
    #plt.plot(CosAveLTcube,WeightedEffArea)
    #plt.show()
    #print 'AveEffArea',WeightedEffArea, np.sum(WeightedEffArea)

    return WeightedEffArea,CosAveLTcube,TotalExposure
                    


def DataForSpline(LivetimeFile=None,
                    EAFile=None,
                    DispersonFile=None,
                    Mchi=None,
                    WindowEMIN=None,
                    WindowEMAX=None,
                    WhicArray='Front',
                    ):
                    

    #log of the DM mass
    y=np.log10(Mchi)

    
    #returns 1) an Array of the  The Weighted Exposure ie( livetime times EffectiveArea) for An average Healpix given the log of the DMMass ie y
    #as a function of instrument angle
    #2) the instrument angle
    WeightedEffArea,CosAveLTcube,TotalExposure=WeightedExposure(LivetimeFile=LivetimeFile,EAFile=EAFile,y=y)


    
    #dispersion
    #plotdifferentEsposuresFordifferntenergies(SplineEA=SplineEA,CosAveLTcube=CosAveLTcube,AveHealpix=AveHealpix)
    Norm,LS1,LS2,RS1,RS2,BIAS=SplinesforDispersionEq(DispersonFile)

    Dic={
        'Mchi':Mchi,
        'Norm':Norm,
        'LS1':LS1,
        'LS2':LS2,
        'RS1':RS1,
        'RS2':RS2,
        'Bias':BIAS,
        'WhicArray':WhicArray,
        }

    #returns an array of the Energy dispersion Given a range of observed energy (DeltaE) and a given instrument incination angle cth
    #passes a dictions of the elemments from the Dispersion function (Dic) and also the log of the DM mass (y)        
    def fsum(x=None,cth=None):
        return ED_array(DeltaE=x,CTheta=cth,Dic=Dic,y=y)
    
    x=np.linspace(WindowEMIN/3.,WindowEMAX*3,1600)
    fsumTheta=np.zeros(len(x))

    #average over the instrument angle weighted by the Effective Exposure as a function of instrument angle
    for i,cth in enumerate(CosAveLTcube):
        fsumTheta=fsumTheta+fsum(x=x,cth=cth)*WeightedEffArea[i]

    #normalize the Averaged dispersion function.
    fsumTheta=fsumTheta/np.trapz(y=fsumTheta,x=x)
    print 'integration over the dispersion function', np.trapz(y=fsumTheta,x=x)  
        
        
    #generate Pline of the averaged dispersion fucnito.
    Spline_fsumTheta=InterpolatedUnivariateSpline(x,fsumTheta)
    print 'integral of Spline', Spline_fsumTheta.integral(WindowEMIN/2.,WindowEMAX*2)

   
   
    
    return fsum,fsumTheta,Spline_fsumTheta,x,TotalExposure



def FrontAndBackDispersion(LivetimeFile=None,
                            EAFileFront=None,
                            EAFileBack=None,
                            DispersonFileFront=None,
                            DispersonFileBack=None,
                            Mchi=None,
                            minEnergy=None,
                            MaxEnergy=None,
                            ):
    fsumFront,fsumThetaFront,Spline_fsumThetaFront,x1Front,TotalExposureFront=DataForSpline(LivetimeFile=LivetimeFile,
                                                                                EAFile=EAFileFront,
                                                                                DispersonFile=DispersonFileFront,
                                                                                Mchi=Mchi,
                                                                                WindowEMIN=minEnergy,
                                                                                WindowEMAX=MaxEnergy,
                                                                                WhicArray='Front', #'Front'
                                                                            )

    fsumBack,fsumThetaBack,Spline_fsumThetaBack,x1Back,TotalExposureBack=DataForSpline(LivetimeFile=LivetimeFile,
                                                                                EAFile=EAFileBack,
                                                                                DispersonFile=DispersonFileBack,
                                                                                Mchi=Mchi,
                                                                                WindowEMIN=minEnergy,
                                                                                WindowEMAX=MaxEnergy,
                                                                                WhicArray='Back', #'Front'
                                                                                )
    WeightBack=TotalExposureBack/(TotalExposureBack+TotalExposureFront)
    WeightFront=TotalExposureFront/(TotalExposureBack+TotalExposureFront)
    print 'WeightBack ',WeightBack
    print 'WeightFront ',WeightFront

    WeightedDispersionArray=WeightBack*fsumThetaBack+WeightFront*fsumThetaFront
    SplineWeightedDispersionArray=InterpolatedUnivariateSpline(x1Back,WeightedDispersionArray)
    
    print 'Integral of Dispersion', np.trapz(y=WeightedDispersionArray,x=x1Back)

    FsumFrontBack=lambda x,cth: WeightFront*fsumFront(x,cth)+WeightBack*fsumBack(x,cth)

    Dic={'FsumFrontBack':FsumFrontBack,
         'WeightedDispersionArray':WeightedDispersionArray,
         'SplineWeightedDispersionArray':SplineWeightedDispersionArray,
         'x':x1Back,
        }
    
   
    return Dic

def main():
    #loadlivetime cube
    directoryofLivetimeCube='../TestIRFs/LiveTimeCube/'
    LivetimeFile=directoryofLivetimeCube+'exposurecube_filtered_events_10GeV_1TeV_zmax100_GTI_ultraclean.fits'
   
    #load effective area Front
    filenameEffArea='aeff_P7REP_ULTRACLEAN_V15_front.fits'
    directoryEffectiveArea='../TestIRFs/EffectiveArea/'  
    EAFileFront=directoryEffectiveArea+filenameEffArea
    
    #load dispersion function Front
    file_energyDispersion='edisp_P7REP_ULTRACLEAN_V15_front.fits'
    dir_Energydispersion='../TestIRFs/EnergyDispersion/'
    DispersonFileFront=dir_Energydispersion+file_energyDispersion

    #load effective area Back
    filenameEffArea='aeff_P7REP_ULTRACLEAN_V15_back.fits'
    directoryEffectiveArea='../TestIRFs/EffectiveArea/'  
    EAFileBack=directoryEffectiveArea+filenameEffArea
    
    #load dispersion function Back
    file_energyDispersion='edisp_P7REP_ULTRACLEAN_V15_back.fits'
    dir_Energydispersion='../TestIRFs/EnergyDispersion/'
    DispersonFileBack=dir_Energydispersion+file_energyDispersion
    
    DMMass=.4e5
    minEnergy=DMMass/1.3
    MaxEnergy=DMMass*1.3
    x=np.linspace(minEnergy/5.,MaxEnergy*4,1600)

    #BAck Array 
    fsum,fsumTheta,Spline_fsumTheta,x1,TotalExposure=DataForSpline(LivetimeFile=LivetimeFile,
                                                                    EAFile=EAFileBack,
                                                                    DispersonFile=DispersonFileBack,
                                                                    Mchi=DMMass,
                                                                    WindowEMIN=minEnergy,
                                                                    WindowEMAX=MaxEnergy,
                                                                    WhicArray='Back', #'Front'
                                                                  )

    

    #Back Array Plots
    plt.loglog(x,fsum(x,.9)/np.trapz(y=fsum(x,.9),x=x),c='red',ls='--',label='Back-ML')    
    plt.loglog(x,Spline_fsumTheta(x),c='blue',ls='--',label='Back-Ave')


    #Front Array
    fsum,fsumTheta,Spline_fsumTheta,x1,TotalExposure=DataForSpline(LivetimeFile=LivetimeFile,
                                                                    EAFile=EAFileFront,
                                                                    DispersonFile=DispersonFileFront,
                                                                    Mchi=DMMass,
                                                                    WindowEMIN=minEnergy,
                                                                    WindowEMAX=MaxEnergy,
                                                                    WhicArray='Front', #'Front'
                                                                  )
    #Front Array Plots
    plt.loglog(x,fsum(x,.9)/np.trapz(y=fsum(x,.9),x=x),c='red',ls=':',label='Front-ML')    
    plt.loglog(x,Spline_fsumTheta(x),c='blue',ls=':',label='Front-Ave')

    #combined Both Fron and Back with Weight given by realtive Exposure of front and back Array
    Dic=FrontAndBackDispersion(LivetimeFile=LivetimeFile,
                                EAFileFront=EAFileFront,
                                EAFileBack=EAFileBack,
                                DispersonFileFront=DispersonFileFront,
                                DispersonFileBack=DispersonFileBack,
                                Mchi=DMMass,
                                minEnergy=minEnergy,
                                MaxEnergy=MaxEnergy,
                                )
    #FrontAndback Plot
    plt.loglog(x,Dic['FsumFrontBack'](x,.9)/np.trapz(y=Dic['FsumFrontBack'](x,.9),x=x),c='red',label='Front&Back-ML')
    plt.loglog(x,Dic['SplineWeightedDispersionArray'](x),c='blue',label='Front&Back-Ave')
    plt.title('Averaged Dispersion(Blue) vs. Most Likely dispersion(Red) at 40 GeV')
    plt.legend()
    plt.show()
    
    return



        

if __name__ == '__main__':
    main()
