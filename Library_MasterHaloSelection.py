#!/usr/bin/env python
"""
elements in GalaxyDataColumns
['GalaxyCount', 'VelocityInCmPerSec', 'MassInGrams', 'GalacticLongitudeInDegrees', 'GalacticLatitudeInDegrees', 'DistanceInCm', 'Jsmooth', 'RvirInCm', 'VisualAngleInDegrees', 'IntensityInJPerDegreesSquared', 'Jclumpy']
"""

import Config_AstronomyConstants as AstroCnst

import matplotlib.pyplot as plt
import numpy as np

import Library_LoadSelectedGalaxyGroups
import Library_PSF
import Library_SelectHalo
import Utility_masterConfig as config



def Main(DMMass=None):


    if DMMass==None: DMMass=1.e5


    #Spline to determine radius
    HaloPSFSpline=Library_PSF.Main(DMMass=DMMass,ConfidenceLevel=config.ConfidenceLevel)
    #Propeties of the halo 1)position on sky 2)radius, 3)Data for each halo 4) the index for the columns of 3)
    Halo3DPositionOnCelestialSphere,HaloRadiusOnCelestialSphere,GroupSourcesData,GroupSourcesDataColumnNames=\
    Library_LoadSelectedGalaxyGroups.Main(PSFfunct=HaloPSFSpline)
    #finding the index for the subselected halos
    IndexOfSelectedElements=Library_SelectHalo.Main(GroupSourcesData=GroupSourcesData,
                                                    GroupSourcesDataColumnNames=GroupSourcesDataColumnNames,
                                                    GroupType=config.GroupType0,
                                                    MaxValue=config.MaxValue0,
                                                    MinValue=config.MinValue0,
                                                    )
    #finding a further subselection of the halos
    IndexOfSelectedElements1=Library_SelectHalo.Main(GroupSourcesData=GroupSourcesData,
                                                    GroupSourcesDataColumnNames=GroupSourcesDataColumnNames,
                                                    GroupType=config.GroupType1,
                                                    MaxValue=config.MaxValue1,
                                                    MinValue=config.MinValue1,
                                                    IndexOfSelectedElements=IndexOfSelectedElements,
                                                    )
    #print 'IndexOfSelectedElements',  len(IndexOfSelectedElements)
    #print 'IndexOfSelectedElements1', len(IndexOfSelectedElements1)
    #sub selection of elements 
    FinalIndexOfElements=IndexOfSelectedElements[IndexOfSelectedElements1]

    
    return  Halo3DPositionOnCelestialSphere,HaloRadiusOnCelestialSphere,GroupSourcesData,GroupSourcesDataColumnNames,FinalIndexOfElements


if __name__ == '__main__':
    Main()
        







        




        
        
    
