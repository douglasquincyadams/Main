"""


DESCRIPTION:

    Digs through fermi Fits files to get an effective area function

    Uses a spline to fit the data, and get inbetween values


RETURNS:
    SplineFunction
        ARGS:
            logEnergy 
            cosInclination
        RETURNS:


"""
import scipy
import scipy.interpolate
from scipy.interpolate import RectBivariateSpline

import matplotlib
import matplotlib.pyplot

import numpy
import astropy
import astropy.io.fits
#------------------------------------------------------------------------------
import Library_AstropyFitsTablePrettyPrint
import Library_FermiInstrumentResponseIndexLookup




def Main(
    Filepath = None,
    PrintExtra = False,
    ):
    #Astropy uses zero-based indexing
    #Fortran uses FITS bases standard   one-based indexing
    HDUList = astropy.io.fits.open(Filepath)

    NumTables = len(HDUList)
    if (PrintExtra):
        print '\n\nNumTables', NumTables, '\n\n'


    if (PrintExtra):
        print 'FILE INFO: \n'
        HDUList.info()

        k = 0 
        for Table in HDUList:
            print '---------------------'
            print "\n\nTable Number ", k
            Library_AstropyFitsTablePrettyPrint.Main(FitsTable = Table, TableName = "Unknown")
            k = k + 1
    
    EffectiveAreaTable = HDUList[1].data



    energyLow=EffectiveAreaTable['ENERG_LO']
    energyHigh=EffectiveAreaTable['ENERG_HI']
    CTHETA_LO=EffectiveAreaTable['CTHETA_LO']
    CTHETA_HI=EffectiveAreaTable['CTHETA_HI']
    EFFAREA=EffectiveAreaTable['EFFAREA']

    energyLow=energyLow[0]
    energyHigh=energyHigh[0]
    EFFAREA=EFFAREA[0]
    CTHETA_LO=CTHETA_LO[0]
    CTHETA_HI=CTHETA_HI[0]


    #centeringDataAndConvertingToLog
    energylogEA=numpy.log10((energyHigh+energyLow)/2.)
    CthetaEA=(CTHETA_HI+CTHETA_LO)/2. 


    
    #Spline of Effective Area as a function of Energy and CTheta. 
    #   Energy is interms of log10 of 1MeV
    SplineEA=scipy.interpolate.RectBivariateSpline(CthetaEA,energylogEA,EFFAREA)
    return SplineEA











