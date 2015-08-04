
#!/usr/bin/env python


"""
Description:
    Tests the main spline function getter


"""
import pyfits
import numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RectBivariateSpline


import Const_LocalDirectoriesFermiFiles
import Library_DataGetFermiInstrumentResponseEffectiveAreaPass7



#Main Function -> called elsewhere
def importEffectiveArea(
        filenameEffArea=None,
        ):
    #reads out the energy angle and effective area
    hdulist=pyfits.open(filenameEffArea)
    print hdulist[1].columns


    energyLow=hdulist[1].data['ENERG_LO']
    energyHigh=hdulist[1].data['ENERG_HI']
    CTHETA_LO=hdulist[1].data['CTHETA_LO']
    CTHETA_HI=hdulist[1].data['CTHETA_HI']
    EFFAREA=hdulist[1].data['EFFAREA']
    energyLow=energyLow[0]
    energyHigh=energyHigh[0]
    EFFAREA=EFFAREA[0]
    CTHETA_LO=CTHETA_LO[0]
    CTHETA_HI=CTHETA_HI[0]
    return CTHETA_LO, CTHETA_HI, energyLow, energyHigh, EFFAREA




def centeringDataAndConvertingToLog(
        energyHigh=None,
        energyLow=None,
        CTHETA_HI=None,
        CTHETA_LO=None
        ):
    energylog=numpy.log10((energyHigh+energyLow)/2.)
    Ctheta=(CTHETA_HI+CTHETA_LO)/2. 
    return energylog, Ctheta



def ReturnThefitingFunction(energy,Ctheta,EFFAREA):
    return RectBivariateSpline(Ctheta,energy,EFFAREA)


def plotofEffectiveArea(
        splineforfit=None,
        effectivearea=None,
        energy=None,
        Ctheta=None,
        ):
    
    numPoints=50000
    deltaEnergy=energy[-1]-energy[0]
    deltaCtheta=Ctheta[-1]-Ctheta[0]
    Energypoints=numpy.random.rand(numPoints)*(deltaEnergy)+energy[0]
    Cthetapoints=(numpy.random.rand(numPoints)*(deltaCtheta)+Ctheta[0])*.99

    print deltaCtheta,deltaEnergy
    plt.figure(1)
    im=plt.scatter(Energypoints,Cthetapoints,c=splineforfit.ev(Cthetapoints,Energypoints),linewidth=0.)
    plt.colorbar(im)



    plt.figure(2)
    extent=[energy[0],energy[-1],Ctheta[0],Ctheta[-1]]
    im=plt.imshow(np.flipud(effectivearea),extent=extent, shape=1, aspect='auto')
    plt.colorbar(im)

    
    #Shhow all plots
    plt.show()

    return
    
def main():
    
    filenameEffArea='aeff_P7REP_ULTRACLEAN_V15_back.fits'
    directoryEffectiveArea= Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEffectiveAreaDirectory

    filepathEffArea = directoryEffectiveArea+'/'+filenameEffArea

    print pyfits.info( filepathEffArea ) 


    CTHETA_LO, CTHETA_HI, energyLow, energyHigh, EFFAREA = importEffectiveArea(filepathEffArea)
    energylog, Ctheta=centeringDataAndConvertingToLog(energyHigh,energyLow,CTHETA_HI,CTHETA_LO)
    #SplineEffectiveArea=RectBivariateSpline(Ctheta,energylog,EFFAREA)

    SplineEffectiveArea = Library_DataGetFermiInstrumentResponseEffectiveAreaPass7.Main(filepathEffArea)

    plotofEffectiveArea(SplineEffectiveArea,EFFAREA,energylog,Ctheta)


    print SplineEffectiveArea.ev(1.,5.) 
    

    
if __name__ == '__main__':
    main()








"""
#LEFTOVER CODE:

EffectiveAreaEnergyLo = EffectiveAreaTable['ENERG_LO'].T
if (PrintExtra):
    print 'EffectiveAreaEnergyLo', EffectiveAreaEnergyLo
    print EffectiveAreaEnergyLo.shape

EffectiveAreaEnergyHi = EffectiveAreaTable['ENERG_HI'].T
if (PrintExtra):
    print 'EffectiveAreaEnergyHi', EffectiveAreaEnergyHi
    print EffectiveAreaEnergyHi.shape

EffectiveAreaCosInclinationLo = EffectiveAreaTable['CTHETA_LO'].T
if (PrintExtra):
    print 'EffectiveAreaCosInclinationLo', EffectiveAreaCosInclinationLo
    print EffectiveAreaCosInclinationLo.shape

EffectiveAreaCosInclinationHi = EffectiveAreaTable['CTHETA_HI'].T
if (PrintExtra):
    print 'EffectiveAreaCosInclinationHi', EffectiveAreaCosInclinationHi
    print EffectiveAreaCosInclinationHi.shape

EffectiveAreaLookup = numpy.array( EffectiveAreaTable['EFFAREA'] )
if (PrintExtra):
    print 'EffectiveAreaLookup.shape', EffectiveAreaLookup.shape
    print ''
"""


"""
def ReturnSplineofEffectiveArea(
        filnameAndDir=None,
        ):

    #Spline of Effective Area as a function of Energy and CTheta. 
    #Energy is interms of log10 of 1MeV

    #print pyfits.info( filnameAndDir) 
    CTHETA_LO_EA, CTHETA_HI_EA, energyLow_EA, energyHigh_EA, EFFAREA = Main(filnameAndDir)
    energylogEA, CthetaEA= centeringDataAndConvertingToLog(energyHigh_EA,energyLow_EA,CTHETA_HI_EA,CTHETA_LO_EA)
    SplineEA=scipy.interpolate.RectBivariateSpline(CthetaEA,energylogEA,EFFAREA)
    return SplineEA


    #matplotlib.pyplot.imshow(
    #EffectiveAreaLookup
    #)
    #matplotlib.pyplot.show()



    #Could be Binary Searches for indexes -> reduce speed from N to log(N)
    def EffectiveAreaFunction(
        Energy = None,
        CosInclination = None,
        PrintExtra = False,
        ):

        #CosInclination = numpy.cos(Inclination)
        EnergyIndex = Library_FermiInstrumentResponseIndexLookup.Main(
            Value = Energy,
            Los = EffectiveAreaEnergyLo,
            His = EffectiveAreaEnergyHi,
        )
        if (PrintExtra):
            print 'EnergyIndex', EnergyIndex

        CosInclinationIndex = Library_FermiInstrumentResponseIndexLookup.Main(
            Value = CosInclination,
            Los = EffectiveAreaCosInclinationLo,
            His = EffectiveAreaCosInclinationHi,
        )
        if (PrintExtra):
            print 'CosInclinationIndex', CosInclinationIndex
 
        EffectiveArea = EffectiveAreaLookup[CosInclinationIndex][EnergyIndex]

        return EffectiveArea

"""




























