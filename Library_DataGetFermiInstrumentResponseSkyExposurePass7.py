"""
SOURCE:
    DS_SkyExposure.ExposureHP()

DESCRIPTION:
    calculates exposure on the sky over a healpix


ARGS:

RETURNS:


"""


import pyfits
from scipy.interpolate import RectBivariateSpline

import numpy as np

import numpy 


import Library_DataGetFermiInstrumentResponseEffectiveAreaPass7
import DS_ReadingLiveTimeCube 


def CosLTdataAndCTheta(
        filnameAndDir=None,
        FileNumber=2, #"Use the Weighted exposure"
        ):
    #returns the the lifetime data for each healpix 
    #and the locations of the average bins for the healpix data
    CosineLiveTimeData,RAdata,DECdata,CThetaMax_LTCube,CThetaMin_LTCube=\
        DS_ReadingLiveTimeCube.ReadLiveTimeCubeHealpixFile(
        filnameAndDir,
        FileNumber=2
        )

    CosAveLTcube=(CThetaMax_LTCube+CThetaMin_LTCube)/2.
    
    return CosAveLTcube,CosineLiveTimeData


def Main(
        FileandDir_EA=None,
        FileandDir_livetime=None,
        EnergyScalelog10=None,
        ):


    def calcExposure(
            CosineLiveTimeData=None,
            CosAveLTcube=None,
            SplineEA=None,
            EnergyScalelog10=None,
            ):
        """calculates the exposure for a single healpix"""
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


    #outputs the exposure on the sky in terms of a healpix
    CosAveLTcube,CosineLiveTimeData=CosLTdataAndCTheta(filnameAndDir=FileandDir_livetime)
    SplineEA=Library_DataGetFermiInstrumentResponseEffectiveAreaPass7.Main(Filepath=FileandDir_EA)
    return calcExposure(CosineLiveTimeData=CosineLiveTimeData, CosAveLTcube=CosAveLTcube,SplineEA=SplineEA,EnergyScalelog10=EnergyScalelog10)



