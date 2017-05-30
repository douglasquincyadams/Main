#!/usr/bin/env python



import Library_DataGetFermiInstrumentResponseSkyExposurePass7
import Const_LocalDirectoriesFermiFiles
import matplotlib.pyplot as plt
import healpy as hp
"""
def calcExposure(
        CosineLiveTimeData=None,
        CosAveLTcube=None,
        SplineEA=None,
        EnergyScalelog10=None,
        ):
    # calculates the exposure for a single healpix
    numofhealpix=CosineLiveTimeData.shape[0]
    Exposure=np.ones(numofhealpix)


    CubeThing = numpy.array(CosAveLTcube).astype('float')
    print '\n\n'
    print CubeThing
    print '\n\n'
    ExposureTest=CosineLiveTimeData[1]*SplineEA.ev( CubeThing, EnergyScalelog10)
    #plt.plot(CosAveLTcube,ExposureTest)
    #plt.show()
    for i in np.arange(0,numofhealpix):
        Exposure[i]=np.sum(CosineLiveTimeData[i]*SplineEA.ev(CosAveLTcube,EnergyScalelog10)*1.e4)

    return Exposure  #returns Healpix for the whole sky

def CosLTdataAndCTheta(
        filnameAndDir=None,
        FileNumber=2, #"Use the Weighted exposure"
        ):
    #returns the the lifetime data for each healpix and the locations of the average bins for the healpix data
    CosineLiveTimeData,RAdata,DECdata,CThetaMax_LTCube,CThetaMin_LTCube=RLTcube.ReadLiveTimeCubeHealpixFile(filnameAndDir,FileNumber=2)
    CosAveLTcube=(CThetaMax_LTCube+CThetaMin_LTCube)/2.
    
    return CosAveLTcube,CosineLiveTimeData




#Main Function
def ExposureHP(
        FileandDir_EA=None,
        FileandDir_livetime=None,
        EnergyScalelog10=None,
        ):
    #outputs the exposure on the sky in terms of a healpix
    CosAveLTcube,CosineLiveTimeData=CosLTdataAndCTheta(filnameAndDir=FileandDir_livetime)
    SplineEA=Library_DataGetFermiInstrumentResponseEffectiveAreaPass7.Main(Filepath=FileandDir_EA)
    return calcExposure(CosineLiveTimeData=CosineLiveTimeData, CosAveLTcube=CosAveLTcube,SplineEA=SplineEA,EnergyScalelog10=EnergyScalelog10)
"""



def main():

    filenameLivetimeCube = 'exposurecube_filtered_events_10GeV_1TeV_zmax100_GTI_ultraclean.fits'
    directoryofLivetimeCube= Const_LocalDirectoriesFermiFiles.DataFilesLiveTimeCubeDirectory
    FileandDir_livetime=directoryofLivetimeCube+'/'+filenameLivetimeCube
  
    filenameEffArea='aeff_P7REP_ULTRACLEAN_V15_back.fits'
    directoryEffectiveArea= Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEffectiveAreaDirectory
    FileandDir_EA=directoryEffectiveArea+'/'+filenameEffArea
   
    ExposureBack=Library_DataGetFermiInstrumentResponseSkyExposurePass7.Main(
        FileandDir_EA=FileandDir_EA,
        FileandDir_livetime=FileandDir_livetime,
        EnergyScalelog10 = 4. )

    filenameEffArea='aeff_P7REP_ULTRACLEAN_V15_front.fits'
    directoryEffectiveArea= Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEffectiveAreaDirectory
    FileandDir_EA=directoryEffectiveArea+'/'+filenameEffArea
   
    ExposureFront=Library_DataGetFermiInstrumentResponseSkyExposurePass7.Main(
        FileandDir_EA=FileandDir_EA,
        FileandDir_livetime=FileandDir_livetime,
        EnergyScalelog10=4.)
        
    plt.figure(0)
    hp.mollview(ExposureBack,nest=True)
    plt.figure(1)
    hp.mollview(ExposureFront,nest=True)
    plt.figure(2)
    hp.mollview(ExposureFront+ExposureFront,nest=True)
    
    plt.show()    
    
    

    


if __name__ == '__main__':
    main()
