#!/usr/bin/env python


import pyfits
import numpy
import numpy as np
import matplotlib.pyplot as plt
import pylab as py

from astropy.coordinates import SkyCoord
from scipy.interpolate import RectBivariateSpline
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import interp1d
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.integrate import quad
from scipy.integrate import dblquad
from scipy.integrate import nquad


#------------------------------------------------------------------------------
import Const_LocalDirectoriesFermiFiles

import Library_DataGetFermiInstrumentResponseEffectiveAreaPass7
import Library_DataGetFermiInstrumentResponseSkyExposurePass7

import DS_ReadingLiveTimeCube 
import DS_ReadDispersionFile 

def Ave2elements(element1,element2, weight1=1.,weight2=1.):
    return (element1*weight1+element2*weight2)/2.

def log10Ave2elements(element1,element2, weight1=1.,weight2=1.):
    return np.log10((element1*weight1+element2*weight2)/2.)

def PlotofDispersionFunctions(
        splinefunction=None,
        OriginalArray=None,
        energy=None,
        Ctheta=None,
        ):
    print OriginalArray.shape
    numPoints=40000
    deltaEnergy=energy[-1]-energy[0]
    deltaCtheta=Ctheta[-1]-Ctheta[0]
    Energypoints=numpy.random.rand(numPoints)*(deltaEnergy)+energy[0]
    Cthetapoints=(numpy.random.rand(numPoints)*(deltaCtheta)+Ctheta[0])
    print deltaCtheta,deltaEnergy
    plt.figure(1)
    im=plt.scatter(Energypoints,Cthetapoints,c=(splinefunction.ev(Cthetapoints,Energypoints)),linewidth=0.)
    plt.colorbar(im)
    
    plt.figure(2)
    extent=(energy[0],energy[-1],Ctheta[0],Ctheta[-1])
    print energy.shape, Ctheta.shape
    im=plt.imshow(np.flipud(OriginalArray),extent=extent,aspect='auto')
    plt.colorbar(im)
    plt.show()


def SplinesforDispersionEq(
        FileAndDir_ED=None,
        ):
    ENERG_LO_Edisp,ENERG_HI_Edisp,CTHETA_LO_Edisp,CTHETA_HI_Edisp,NORM_Edisp,LS1_Edisp,LS2_Edisp,RS1_Edisp,RS2_Edisp,BIAS_Edisp=DS_ReadDispersionFile.ReadEnergyDispersionFile(Filename_ED=FileAndDir_ED)
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
    RA_LiveTimeCube,DEC_LiveTimeCube= DS_ReadingLiveTimeCube.RAandDECofLiveTimeCube(Filename)
    
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

def PlotofDispersionFunctions(
        splinefunction=None,
        OriginalArray=None,
        energy=None,
        Ctheta=None,
        ):
    print OriginalArray.shape
    numPoints=40000
    deltaEnergy=energy[-1]-energy[0]
    deltaCtheta=Ctheta[-1]-Ctheta[0]
    Energypoints=numpy.random.rand(numPoints)*(deltaEnergy)+energy[0]
    Cthetapoints=(numpy.random.rand(numPoints)*(deltaCtheta)+Ctheta[0])
    print deltaCtheta,deltaEnergy
    plt.figure(1)
    im=plt.scatter(Energypoints,Cthetapoints,c=(splinefunction.ev(Cthetapoints,Energypoints)),linewidth=0.)
    plt.colorbar(im)
    
    plt.figure(2)
    extent=(energy[0],energy[-1],Ctheta[0],Ctheta[-1])
    print energy.shape, Ctheta.shape
    im=plt.imshow(np.flipud(OriginalArray),extent=extent,aspect='auto')
    plt.colorbar(im)
    plt.show()

    return


def PlotofDispersionFunctions(
        splinefunction=None,
        OriginalArray=None,
        energy=None,
        Ctheta=None,
        ):
    print OriginalArray.shape
    numPoints=40000
    deltaEnergy=energy[-1]-energy[0]
    deltaCtheta=Ctheta[-1]-Ctheta[0]
    Energypoints=numpy.random.rand(numPoints)*(deltaEnergy)+energy[0]
    Cthetapoints=(numpy.random.rand(numPoints)*(deltaCtheta)+Ctheta[0])
    print deltaCtheta,deltaEnergy
    plt.figure(1)
    im=plt.scatter(Energypoints,Cthetapoints,c=(splinefunction.ev(Cthetapoints,Energypoints)),linewidth=0.)
    plt.colorbar(im)
    
    plt.figure(2)
    extent=(energy[0],energy[-1],Ctheta[0],Ctheta[-1])
    print energy.shape, Ctheta.shape
    im=plt.imshow(np.flipud(OriginalArray),extent=extent,aspect='auto')
    plt.colorbar(im)
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
        Mchi=None,
        Norm=None,
        LS1=None,
        LS2=None,
        RS1=None,
        RS2=None,
        Bias=None,
        WhicArray=None,
        CTheta=None,
        ):
    """Energy Dispersion function"""
    NormLeft=Norm*np.exp(-np.abs((1.5-Bias)/LS1)**1.6/2.)*np.exp(np.abs((1.5-Bias)/LS2)**0.6/2.)
    NormRight=Norm*np.exp(-np.abs((1.5-Bias)/RS1)**1.6/2.)*np.exp(np.abs((1.5-Bias)/RS2)**0.6/2.)
    Xboundary=1.5
    x=(DeltaE-Mchi)/Mchi/Snorm_EnergyDispersion(logEnergy=np.log10(Mchi),CTheta=CTheta,WhicArray=WhicArray)
    if((x-Bias)<-Xboundary):
        N=NormLeft
        sig=LS2
        gamma=0.6
        return N*np.exp(-0.5*np.abs((x-Bias)/sig)**gamma)
    if((x-Bias)>Xboundary):
        N=NormRight
        sig=RS2
        gamma=0.6
        return N*np.exp(-0.5*np.abs((x-Bias)/sig)**gamma)
    if((x-Bias)<0):
        N=Norm
        sig=LS1
        gamma=1.6
        return N*np.exp(-0.5*np.abs((x-Bias)/sig)**gamma)
    if((x-Bias)>0):
        N=Norm
        sig=RS1
        gamma=1.6
        return N*np.exp(-0.5*np.abs((x-Bias)/sig)**gamma)

#def EnergyDispersion2(DeltaE=None,
#                      Mchi=None,
#                      cth=None,
#                      WhicArray=None,
#                      ):
#    x=cth
#    y=np.log10(Mchi)
#    Norm=NORMSPLINE(x=x,y=y)
#    LS1=LS1SPLINE(x=x,y=y)
#    LS2=LS2SPLINE(x=x,y=y)
#    RS1=RS1SPLINE(x=x,y=y)
#    RS2=RS2SPLINE(x=x,y=y)
#    Bias=BIASSPLINE(x=x,y=y)
#    f=EnergyDisperison(DeltaE=DeltaE,CTheta=cth,Mchi=Mchi,Norm=Norm,LS1=LS1,LS2=LS2,RS1=RS1,RS2=RS2,Bias=Bias,WhicArray=WhicArray)
#    return f

"""
Main Function

"""
def DataForSpline(LivetimeFile=None,
                    EAFile=None,
                    DispersonFile=None,
                    Mchi=None,
                    WindowEMIN=None,
                    WindowEMAX=None,
                    NumofInt_Divisions=5,
                    WhicArray='Front',
                    NumberOfEnergyDivisions=100,
                    ):
                    
    """main console. reads in Data, and gives back the dispersion function as a interpolating function"""
    #livetimedata 
    CosAveLTcube,CosineLiveTimeData=Library_DataGetFermiInstrumentResponseSkyExposurePass7.CosLTdataAndCTheta(LivetimeFile,FileNumber=2)

    #generate an averaged livetime Cube.
    numofhealpix= CosineLiveTimeData.shape[0]
    AveHealpix=CosineLiveTimeData[0]
    for i in np.arange(1,numofhealpix):
        AveHealpix=AveHealpix+CosineLiveTimeData[i]

    #Effective Area    
    SplineEA = Library_DataGetFermiInstrumentResponseEffectiveAreaPass7.Main(EAFile)

    #dispersion
    #plotdifferentEsposuresFordifferntenergies(SplineEA=SplineEA,CosAveLTcube=CosAveLTcube,AveHealpix=AveHealpix)
    NORMSPLINE,LS1SPLINE,LS2SPLINE,RS1SPLINE,RS2SPLINE,BIASSPLINE=SplinesforDispersionEq(DispersonFile)

    y=np.log10(Mchi) #note mass is in logspace
    
    Norm=NORMSPLINE
    LS1=LS1SPLINE
    LS2=LS2SPLINE
    RS1=RS1SPLINE
    RS2=RS2SPLINE
    Bias=BIASSPLINE
    #dispersionfuction with the Averaged Effective area
    #f_ED=lambda DeltaE, cth :SplineEA(cth,y)*EnergyDisperison(DeltaE=DeltaE,
    #                                                          CTheta=cth,
    #                                                          Mchi=Mchi,
    #                                                          Norm=Norm(cth,y),
    #                                                          LS1=LS1(cth,y),
    #                                                          LS2=LS2(cth,y),
    #                                                          RS1=RS1(cth,y),
    #                                                          RS2=RS2(cth,y),
    #                                                          Bias=Bias(cth,y),
    #                                                          WhicArray=WhicArray
    #                                                          )

    #NormDispersion=NormofDispersion(f_ED=f_ED,
    #                                WindowEMIN=WindowEMIN,
    #                                WindowEMAX=WindowEMAX,
    #                                NumofInt_Divisions=NumofInt_Divisions
    #                                )

    #Spline_Array
    cthi=0.6
    f_NormalongTheta=lambda DeltaE,cth :SplineEA(cth,y)*EnergyDisperison(DeltaE=DeltaE,
                                                                    CTheta=cth,
                                                                    Mchi=Mchi,
                                                                    Norm=Norm(cth,y),
                                                                    LS1=LS1(cth,y),
                                                                    LS2=LS2(cth,y),
                                                                    RS1=RS1(cth,y),
                                                                    RS2=RS2(cth,y),
                                                                    Bias=Bias(cth,y),
                                                                    WhicArray=WhicArray,
                                                                    )
    NumberOfThetaDivisions=15
    SplineArray=NormFunctionofEnergyDisperisonAsAFucntionofTheta(f_NormalongTheta=f_NormalongTheta,
                     WindowEMIN=WindowEMIN,
                     WindowEMAX=WindowEMAX,
                     NumberOfThetaDivisions=NumberOfThetaDivisions,
                     )
    xpoints=np.linspace(0.2,1,NumberOfThetaDivisions)
    ypoints=np.log10(SplineArray)
    F_normThetaSpline=UnivariateSpline(xpoints,ypoints)
    
    f_FxdDeltaE=lambda cth, DeltaE :SplineEA(cth,y)/np.power(10,F_normThetaSpline(cth))*EnergyDisperison(DeltaE=DeltaE,
                                                                                                            CTheta=cth,
                                                                                                            Mchi=Mchi,
                                                                                                            Norm=Norm(cth,y),
                                                                                                            LS1=LS1(cth,y),
                                                                                                            LS2=LS2(cth,y),
                                                                                                            RS1=RS1(cth,y),
                                                                                                            RS2=RS2(cth,y),
                                                                                                            Bias=Bias(cth,y),
                                                                                                            WhicArray=WhicArray,
                                                                                                        )

    
    SplineArray=FunctionofSpline(f_FxdDeltaE=f_FxdDeltaE,
                     WindowEMIN=WindowEMIN,
                     WindowEMAX=WindowEMAX,
                     NumberOfEnergyDivisions=NumberOfEnergyDivisions
                     )
    
    xpoints=np.linspace(WindowEMIN,WindowEMAX,NumberOfEnergyDivisions)
    ypoints=np.log10(SplineArray)
    #InterDispersionFunction=InterpolatedUnivariateSpline(xpoints,ypoints,k=3,ext='extrapolate')
    InterDispersionFunction=UnivariateSpline(xpoints,ypoints)
    f=lambda x:np.power(10,InterDispersionFunction(x))
    norm=quad(f,WindowEMIN,WindowEMAX)[0]
    ypoints=np.log10(SplineArray/norm)
    #InterDispersionFunction=InterpolatedUnivariateSpline(xpoints,ypoints,k=3,ext='extrapolate')
    InterDispersionFunction=UnivariateSpline(xpoints,ypoints)
    
    return SplineArray,InterDispersionFunction 

def NormFunctionofEnergyDisperisonAsAFucntionofTheta(f_NormalongTheta=None,
                     WindowEMIN=None,
                     WindowEMAX=None,
                     NumberOfThetaDivisions=None,
                     ):

    SplineArray=np.ones(NumberOfThetaDivisions)
    i=0
    xelements=np.linspace(0.2,1.0,NumberOfThetaDivisions)
    for ThetaElement in xelements:
        output=quad(f_NormalongTheta,WindowEMIN,WindowEMAX,args=(ThetaElement),limit=100)
        SplineArray[i]=np.abs(output[0])
        print i, output
        i=i+1
    #plt.plot(xelements,SplineArray)
    #plt.show()
    return SplineArray


def FunctionofSpline(f_FxdDeltaE=None,
                     WindowEMIN=None,
                     WindowEMAX=None,
                     NumberOfEnergyDivisions=None,
                     ):
        
    SplineArray=np.ones(NumberOfEnergyDivisions)
    Splineerror=np.ones(NumberOfEnergyDivisions)
    i=0
    for EnergyElement in np.linspace(WindowEMIN,WindowEMAX,NumberOfEnergyDivisions):
        output=quad(f_FxdDeltaE,0.2,1.,args=(EnergyElement))
        SplineArray[i]=output[0]
        print i, output[0], EnergyElement
        Splineerror[i]=output[1]
        i=i+1
    print SplineArray
    print NumberOfEnergyDivisions,WindowEMIN,WindowEMAX
    
    return SplineArray

    
        
def NormofDispersion(f_ED=None,
                     WindowEMIN=None,
                     WindowEMAX=None,
                     NumofInt_Divisions=None,
                    ):
    EMIN=WindowEMIN
    EMAX=WindowEMAX
    CTHMAX=1.0
    CTHMIN=0.2
    NUM_DIV=NumofInt_Divisions
    NUM_DIV=NUM_DIV+1
    EnergyMIN_integration=np.linspace(EMIN,EMAX,NUM_DIV)[:-1]
    EnergyMAX_integration=np.linspace(EMIN,EMAX,NUM_DIV)[1:]
    CthetaMIN_integration=np.linspace(CTHMIN,CTHMAX,NUM_DIV)[:-1]
    CthetaMAX_integration=np.linspace(CTHMIN,CTHMAX,NUM_DIV)[1:]

    NormDispersion=0.
    stepNorm=0.
    for i in np.arange(len(EnergyMAX_integration)):
        for j in np.arange(len(CthetaMIN_integration)):
            print (i+1)*(j+1)
            print 'EnergyMIN_integration',EnergyMIN_integration[i],'EnergyMAX_integration',EnergyMAX_integration[i]
            print 'CthetaMIN_integration',CthetaMIN_integration[j],'CthetaMAX_integration',CthetaMAX_integration[j]
            gmin=lambda DeltaE:f_ED(DeltaE,cth=CthetaMIN_integration[j])
            gmax=lambda DeltaE:f_ED(DeltaE,cth=CthetaMAX_integration[j])
            stepNorm= dblquad(f_ED,EnergyMIN_integration[i],EnergyMAX_integration[i],gfun=gmin,hfun=gmax)
            NormDispersion=NormDispersion+stepNorm[0]
            print stepNorm, NormDispersion
  


    return NormDispersion

#def spline
   


"""
All calculations done in the tests use the 4Ultra cut on Pass7 data
"""
def main():
    #loadlivetime cube
    directoryofLivetimeCube=  Const_LocalDirectoriesFermiFiles.DataFilesLiveTimeCubeDirectory
    LiveTimefile=directoryofLivetimeCube+'/exposurecube_filtered_events_10GeV_1TeV_zmax100_GTI_ultraclean.fits'
    
      
    #load effective area
    filenameEffArea_f='aeff_P7REP_ULTRACLEAN_V15_front.fits'
    directoryEffectiveArea= Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEffectiveAreaDirectory
    EAFile_f=directoryEffectiveArea+'/'+filenameEffArea_f
    
    #load dispersion function
    file_energyDispersion_f='edisp_P7REP_ULTRACLEAN_V15_front.fits'
    dir_Energydispersion= Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEnergyDispersionDirectory
    DispersonFile_f=dir_Energydispersion+'/'+file_energyDispersion_f

    DMMass=2.e5
    minEnergy=1.5e5
    MaxEnergy=2.5e5
    NumberOfEnergyDivisions=100	
    SplineArray_f,Spline_ED_f =DataForSpline(LivetimeFile=LiveTimefile,
                                                EAFile=EAFile_f,
                                                DispersonFile=DispersonFile_f,
                                                Mchi=DMMass,
                                                WindowEMIN=minEnergy,
                                                WindowEMAX=MaxEnergy,
                                                NumofInt_Divisions=10,
                                                NumberOfEnergyDivisions=NumberOfEnergyDivisions,
                                                WhicArray='Front',
                                                )

    #load effective area
    filenameEffArea_b='aeff_P7REP_ULTRACLEAN_V15_back.fits'
    directoryEffectiveArea= Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEffectiveAreaDirectory
    EAFile_b=directoryEffectiveArea+'/'+filenameEffArea_b
    
    #load dispersion function
    file_energyDispersion_b='edisp_P7REP_ULTRACLEAN_V15_back.fits'
    dir_Energydispersion= Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEnergyDispersionDirectory
    DispersonFile_b=dir_Energydispersion+'/'+file_energyDispersion_b

    SplineArray_b,Spline_ED_b =DataForSpline(LivetimeFile=LiveTimefile,
                                                EAFile=EAFile_b,
                                                DispersonFile=DispersonFile_b,
                                                Mchi=DMMass,
                                                WindowEMIN=minEnergy,
                                                WindowEMAX=MaxEnergy,
                                                NumofInt_Divisions=10,
                                                NumberOfEnergyDivisions=NumberOfEnergyDivisions,
                                                WhicArray='back',
                                                )


    xpoints=np.linspace(minEnergy,MaxEnergy,NumberOfEnergyDivisions)
    ypoints=np.log10((SplineArray_b+SplineArray_f)/2.)
    f=lambda x=None:(np.power(10,Spline_ED_b(x))+np.power(10,Spline_ED_f(x)))/2.
    plt.semilogy(xpoints,f(xpoints),c='red')
    print quad(f,minEnergy,MaxEnergy)
    plt.semilogy(xpoints, (SplineArray_f), c='green')
    plt.semilogy(xpoints, (SplineArray_b), c='blue')
    plt.show()
    return



        

if __name__ == '__main__':
    main()
