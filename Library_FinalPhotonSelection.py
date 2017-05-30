#!/usr/bin/env python
"""
Test for selecting down selecting the halos and correct photons
at present remove halos which dont overlap with point sources
"""

import DS_LoadPhotonsForEnergyRange
import Library_MasterSelectPointSources
import Library_MasterHaloSelection
from  scipy.spatial import KDTree
import numpy as np
import matplotlib.pyplot as plt

def Main():

    DMMass=5.e5
    EnergyMin=DMMass/1.3
    EnergyMax=DMMass*1.3

    #import the photons
    FermiEventLocations3D,EventEnergiesSelected,EnergyMaxOut,EnergyMinOut=DS_LoadPhotonsForEnergyRange.Main(EnergyMax=EnergyMax,EnergyMin=EnergyMin)
    print 'photons done'
    
    #import Halos with PSF corrected as well.
    Halo3DPositionOnCelestialSphere,HaloRadiusOnCelestialSphere,GroupSourcesData,GroupSourcesDataColumnNames,HaloIndex=\
    Library_MasterHaloSelection.Main(DMMass=DMMass)
    print 'Halos done'
    
    #import point Sources
    SurfProjPointSourceLoc3D,SurfProjPointSourceLocRadii,PointSourcesData,PointSourceIndex=\
    Library_MasterSelectPointSources.Main(DMMass=DMMass,MaxEnergy=EnergyMaxOut,MinEnergy=EnergyMinOut)
    print 'pointSources Done'

    #point Source KDTree
    pointSourceKDTree=KDTree(SurfProjPointSourceLoc3D[PointSourceIndex])
    print len(SurfProjPointSourceLoc3D[PointSourceIndex])
    print 'SurfProjPointSourceLocRadii'
    print SurfProjPointSourceLocRadii[0]
    PSRadius=SurfProjPointSourceLocRadii[0]
    
    #Subselected Halos and Position
    SelecteHalos3Dposition=Halo3DPositionOnCelestialSphere[HaloIndex]
    SelectedHaloRadii=HaloRadiusOnCelestialSphere[HaloIndex]

    indexOfHalo=0
    listOfHalos=[]
    print 'selecting halos'
    for halo,radii in zip(SelecteHalos3Dposition, SelectedHaloRadii):
        ListofPoints=pointSourceKDTree.query_ball_point(halo,radii+PSRadius)
        #print halo,radii
        #print ListofPoints
        if len(ListofPoints)<1: listOfHalos.append(indexOfHalo)
        indexOfHalo=indexOfHalo+1

    listOfHalos=np.array(listOfHalos)
    FinalHaloIndex=HaloIndex[listOfHalos]
    print 'number of halos', len(FinalHaloIndex)
    #print listOfHalos
    #print len(listOfHalos)
    #print len(SelecteHalos3Dposition)

    #Photon KDTree
    print len(FermiEventLocations3D)
    PhotonKDTRee=KDTree(FermiEventLocations3D)
    print 'Making photon KDTree'

    #SubSetOfHalos
    FinalSelecteHalos3Dposition=Halo3DPositionOnCelestialSphere[FinalHaloIndex]
    FinalSelectedHaloRadii=HaloRadiusOnCelestialSphere[FinalHaloIndex]

    #selecting photons
    setofphtons=[]
    for halo,radii in zip(FinalSelecteHalos3Dposition,FinalSelectedHaloRadii):
        setofphtons+=PhotonKDTRee.query_ball_point(halo,radii)
        
    setofphtons=np.array(list(set(setofphtons)))
    print 'EnergyMaxOut,EnergyMinOut', EnergyMaxOut,EnergyMinOut
    print 'number of photons ',len(setofphtons)
    #print  FermiEventLocations3D.shape
    plt.hist(EventEnergiesSelected[setofphtons]/1.e3,bins=20)
    plt.show()
    GroupTypeElements=GroupSourcesData[:,[GroupSourcesDataColumnNames.index('Jsmooth')] ].T[0]
    print np.sum(GroupTypeElements[FinalHaloIndex])
    return EventEnergiesSelected[setofphtons],GroupSourcesData,GroupSourcesDataColumnNames,FinalHaloIndex  
    
"""
elements in GalaxyDataColumns for which we can select for
['GalaxyCount', 'VelocityInCmPerSec', 'MassInGrams', 'GalacticLongitudeInDegrees', 'GalacticLatitudeInDegrees',
 'DistanceInCm', 'Jsmooth', 'RvirInCm', 'VisualAngleInDegrees', 'IntensityInJPerDegreesSquared', 'Jclumpy']
"""
    



if __name__ == '__main__':
    Main()
