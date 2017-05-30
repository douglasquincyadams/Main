#!/usr/bin/env python


"""
Description
asdfasdfasdf
"""
import pyfits
import numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RectBivariateSpline


def importEffectiveArea(
        filenameEffArea=None,
        ):
    """reads out the energy angle and effective area"""
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

importEffectiveArea.Description = "Hello Doug"

def centeringDataAndConvertingToLog(
        energyHigh=None,
        energyLow=None,
        CTHETA_HI=None,
        CTHETA_LO=None
        ):
    energylog=np.log10((energyHigh+energyLow)/2.)
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
    plt.show()
    #print 'what is up?'
    return
    
def main():
    
    filenameEffArea='aeff_P7REP_ULTRACLEAN_V15_back.fits'
    directoryEffectiveArea='/Users/dspolyar/Documents/IRF/EffectiveArea/' 
    print pyfits.info( directoryEffectiveArea+filenameEffArea) 
    CTHETA_LO, CTHETA_HI, energyLow, energyHigh, EFFAREA = importEffectiveArea(directoryEffectiveArea+filenameEffArea)
    energylog, Ctheta=centeringDataAndConvertingToLog(energyHigh,energyLow,CTHETA_HI,CTHETA_LO)
    SplineEffectiveArea=RectBivariateSpline(Ctheta,energylog,EFFAREA)
    plotofEffectiveArea(SplineEffectiveArea,EFFAREA,energylog,Ctheta)
    print SplineEffectiveArea.ev(1.,5.)
    

    
if __name__ == '__main__':
    main()

