#!/usr/bin/env python 

import pyfits
import numpy
import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
import Const_LocalDirectoriesFermiFiles


#This is the main function:
def ReadLiveTimeCubeHealpixFile(
        filename=None,
        FileNumber=1
        ):
    """Returns the heapix of the RA, DEC, and livetime in seconds spent at a given cosine on the sky"""
    hdulist=pyfits.open(filename)
    #print pyfits.info(filename)
    #print 'columns of the first data file',hdulist[1].columns
    CosineLiveTimeData=hdulist[FileNumber].data['COSBINS']
    RAdata=hdulist[FileNumber].data['RA']
    DECdata=hdulist[FileNumber].data['DEC']
    CThetaMax=hdulist[3].data['CTHETA_MAX']
    CThetaMin=hdulist[3].data['CTHETA_MIN']
    hdulist.close()
    return CosineLiveTimeData,RAdata,DECdata,CThetaMax,CThetaMin

def RAandDECofLiveTimeCube(
        FileandDir_livetime=None,
        FileNumber=1
        ):
    """Returns RA and DECdata"""
    hdulist=pyfits.open(FileandDir_livetime)
    RAdata=hdulist[FileNumber].data['RA']
    DECdata=hdulist[FileNumber].data['DEC']
    hdulist.close()
    return RAdata,DECdata
        
def IndexToDeclRa(
        index=None,
        NSIDE=64,
        ):
    """converts Index back to Dec and RA"""
    theta,phi=hp.pixelfunc.pix2ang(NSIDE,index,nest=True)
    return -np.degrees(theta-np.pi/2.),np.degrees(phi)

def DeclRaToIndex(
        decl=None,
        RA=None,
        NSIDE=64
        ):
    """Converts Dec and RA to the index in Healpix"""
    return hp.pixelfunc.ang2pix(NSIDE,np.radians(-decl+90.),np.radians(RA),nest=True)



def Cosine_liveTime(
        CosineLiveTimeData=None,
        Dec=None,
        RA=None,
        Nside=64,
        ):
    """Returns the livetime data as a function CTheta for a give Dec, and RA on the Sky"""
    indexofhealpix=DeclRaToIndex(Dec,RA,Nside)
    return CosineLiveTimeData[indexofhealpix]



def TestFigures_LiveTimeCube(
                CosineLiveTimeData=None,
                RAdata=None,
                DECdata=None
                ):
    """plots output of livetime data for a few different angles of the the instrument over the sky"""
    plt.figure(1)
    plt.hist(RAdata)
    plt.figure(2)
    plt.hist(DECdata)
    hp.mollview(RAdata,nest=True,title='RA')
    hp.mollview(DECdata,nest=True,title='DEC')
    hp.mollview(CosineLiveTimeData.T[1],nest=True, title="cos($\\theta$)= 0")
    hp.mollview(CosineLiveTimeData.T[15],nest=True, title="cos($\\theta$)= 0.5")
    hp.mollview(CosineLiveTimeData.T[30],nest=True, title="cos($\\theta$)= 1")
    plt.show()
    return

def Test_Angles2index(
        Decl=None,
        RA=None,
        DECdata=None,
        RAdata=None,
        Nside=64,
        ):
    """determines if the RA and DEC are working"""
    indexofhealpix=DeclRaToIndex(Decl,RA,Nside)
    print 'DEC  RA  and passed through again'
    print DECdata[indexofhealpix],RAdata[indexofhealpix],IndexToDeclRa(indexofhealpix,64)
    return



def Test_coslineLiveReading(
                CosineLiveTimeData=None,
                CThetaMin=None,
                Dec=35.,
                RA=10.,
                Nside=64,
                ):
    """Test Reading an element from the LiveTime cube"""
    CosineDataLocal=Cosine_liveTime(CosineLiveTimeData,Dec,RA)
    plt.plot(CThetaMin,CosineDataLocal)
    plt.ylabel('ssecond per angle')
    plt.xlabel('Cosine Theta')
    plt.show()
    return
    
def main():
    filename1='exposurecube_filtered_events_10GeV_1TeV_zmax100_GTI_ultraclean.fits'
    fileDirectory= Const_LocalDirectoriesFermiFiles.DataFilesLiveTimeCubeDirectory
    filename=fileDirectory+'/'+filename1
    CosineLiveTimeData,RAdata,DECdata,CThetaMax,CThetaMin=ReadLiveTimeCubeHealpixFile(filename)
    TestFigures_LiveTimeCube(CosineLiveTimeData,RAdata,DECdata)
    print DeclRaToIndex(35.,10.)
    Test_Angles2index(-25.,35.,DECdata,RAdata)
    Test_coslineLiveReading(CosineLiveTimeData,CThetaMin)
    

if __name__ == '__main__':
    main()
