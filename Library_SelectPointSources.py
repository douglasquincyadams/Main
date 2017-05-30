#!/usr/bin/env python



import Utility_masterConfig as config
import numpy as np
import scipy
from scipy.integrate import quad
import matplotlib.pyplot as plt
import Const_LocalDirectoriesFermiFiles
import DS_SkyExposure as SE
import healpy as hp
import pylab as py

def DeclRaToIndex(
        decl=None,
        RA=None,
        NSIDE=64
        ):
    """Converts Dec and RA to the index in Healpix with declination equaal to latitude and RA to longitude"""
    return hp.pixelfunc.ang2pix(NSIDE,np.radians(-decl+90.),np.radians(RA),nest=True)


def PowerSpectrumPointSources(SpectrumType=None,
                              Pivot_Energy=None,
                              Flux_Density=None,
                              Spectral_Index=None,
                              beta=None,
                              Cutoff=None,
                              Exp_Index=None,
                              PowerLaw_Index=None,
                             ):
    if SpectrumType=='LogParabola':
        def FunctionUout(Energy=None):
            f1=Flux_Density*np.power(Energy/Pivot_Energy,-Spectral_Index-beta*np.log(Energy/Pivot_Energy))
            return f1
        return FunctionUout
    if SpectrumType=='PLSuperExpCutoff':
        def FunctionUout(Energy=None):            
            f1=Flux_Density*np.power(Energy/Pivot_Energy,-Spectral_Index)
            fcutoff=np.exp((Pivot_Energy/Cutoff)**Exp_Index-(Energy/Cutoff)**Exp_Index)
            return f1*fcutoff
        return FunctionUout
    if SpectrumType=='PLExpCutoff':
        def FunctionUout(Energy=None):            
            f1=Flux_Density*np.power(Energy/Pivot_Energy,-Spectral_Index)
            fcutoff=np.exp((Pivot_Energy/Cutoff)-(Energy/Cutoff))
            return f1*fcutoff
        return FunctionUout
    if SpectrumType=='PowerLaw':
        def FunctionUout(Energy=None):
            f1=Flux_Density*np.power(Energy/Pivot_Energy,-Spectral_Index)
            return f1
        return FunctionUout

def ExposureForPointSources():
    
    directoryofLivetimeCube=Const_LocalDirectoriesFermiFiles.DataFilesLiveTimeCubeDirectory
    FileandDir_livetime=directoryofLivetimeCube+'/exposurecube_filtered_events_10GeV_1TeV_zmax100_GTI_ultraclean.fits'
   
    filenameEffArea='/aeff_P7REP_ULTRACLEAN_V15_back.fits'
    directoryEffectiveArea=Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEffectiveAreaDirectory  
    FileandDir_EA=directoryEffectiveArea+filenameEffArea
   
    Exposure_b=SE.ExposureHP(FileandDir_EA=FileandDir_EA,FileandDir_livetime=FileandDir_livetime,EnergyScalelog10=4.)


    filenameEffArea='/aeff_P7REP_ULTRACLEAN_V15_front.fits'
    directoryEffectiveArea=Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEffectiveAreaDirectory 
    FileandDir_EA=directoryEffectiveArea+filenameEffArea
   
    Exposure_f=SE.ExposureHP(FileandDir_EA=FileandDir_EA,FileandDir_livetime=FileandDir_livetime,EnergyScalelog10=4.)

    Exposure_c=(Exposure_b+Exposure_f)*1.e4

    #hp.mollview(Exposure_c,nest=True)
    #plt.show()

    return Exposure_c

def Main(PointSources=None,
         DMMass=None,
         MaxEnergy=None,
         MinEnergy=None,
         ):

    #determines The Flux from Each Point source
    IntegratedFlux=np.zeros(len(PointSources))
    #determines if the integration has been done before
    try:
        IntegratedFlux=np.load('../TempDataStore/IntegratedFluxDMmass'+str(int(DMMass))+'.npy')
    except:
        print 'Determining Point Source Flux'    
        for elemment in np.arange(len(PointSources)):
            f1=PowerSpectrumPointSources(SpectrumType=PointSources['SpectrumType'][elemment],
                                    Pivot_Energy=PointSources['Pivot_Energy'][elemment],
                                    Flux_Density=PointSources['Flux_Density'][elemment],
                                    Spectral_Index=PointSources['Spectral_Index'][elemment],
                                    beta=PointSources['beta'][elemment],
                                    Cutoff=PointSources['Cutoff'][elemment],
                                    Exp_Index=PointSources['Exp_Index'][elemment],
                                    PowerLaw_Index=PointSources['PowerLaw_Index'][elemment],
                                    )
            IntegratedFlux[elemment]=quad(f1,MinEnergy,MaxEnergy)[0]
            #print IntegratedFlux[elemment]
            np.save('../TempDataStore/IntegratedFluxDMmass'+str(int(DMMass))+'.npy',IntegratedFlux)

    #calcuates the exposere accorss the scky                
    Exposure_c=ExposureForPointSources()
    #position on the sky
    PointSourceLongitudes = PointSources['GLON']
    PointSourceLatitudes = PointSources['GLAT']
    #give the healpix for a given position on the sky
    PointSourceHealpix=DeclRaToIndex(RA=PointSourceLongitudes,decl=PointSourceLatitudes)
    #determines the exposure for each Point sources
    PointSourceExposure=Exposure_c[PointSourceHealpix]
    #determines the number of photons observed at each point in the sky
    PhotonCountPerPointSouce=PointSourceExposure*IntegratedFlux
    
    SortedPhotonCountPerPointSouce=np.sort(PhotonCountPerPointSouce, kind='heapsort')
    IndexNumberFortopSources=int(np.round(len(SortedPhotonCountPerPointSouce)*(1-config.PointSourceCuttoff)))
    IndexAboveCuttoff=py.find(PhotonCountPerPointSouce>SortedPhotonCountPerPointSouce[IndexNumberFortopSources])

    #print 'DM mass', DMMass
    #print 'Min energy' , MinEnergy
    #print 'Max Energy', MaxEnergy
    #print 'total ', np.sum(PhotonCountPerPointSouce), len(PhotonCountPerPointSouce)
    #print 'IndexAbove1 ', np.sum(PhotonCountPerPointSouce[IndexAboveCuttoff]) , len(PhotonCountPerPointSouce[IndexAboveCuttoff])
    #print  'IndexNumberFortopSources', IndexNumberFortopSources
    #print  'Cut off on the PointSources ', SortedPhotonCountPerPointSouce[IndexNumberFortopSources]
    #plt.figure(0)
    #plt.hist(PhotonCountPerPointSouce,bins=100,log=True,range=(0,10))
    
    #plt.figure(1)
    #hp.mollview(Exposure_c,nest=True)
    #plt.show()
    return IndexAboveCuttoff

if __name__ == '__main__':
    Main()
