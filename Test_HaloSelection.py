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

def HistOfdifferentValues(
                          IndexOfSelectedElements=None,
                          GroupSourcesData=None,
                          GroupSourcesDataColumnNames=None,
                          ):
    GroupType='Jsmooth'
    plt.figure(0)
    GroupTypeElements=GroupSourcesData[:,[GroupSourcesDataColumnNames.index(GroupType)] ].T[0]
    GroupTypeElementsSelected=GroupTypeElements[IndexOfSelectedElements]
    totalJsmooth_All=np.sum(GroupTypeElements)
    totalJsmooth=np.sum(GroupTypeElementsSelected)
    print 'totalJsmooth',totalJsmooth
    print 'totalJsmooth_All',totalJsmooth_All
    print 'number of elements', len(GroupTypeElements)
    print 'number of selected elements', len(GroupTypeElementsSelected)
    plt.hist(GroupTypeElementsSelected,bins=100,log=True)
    plt.title(GroupType)
    plt.show()
    return

    
def Main():

    DMMass=1.e5  #DM mass in MeV


    
    #Spline to determine radius
    HaloPSFSpline=Library_PSF.Main(DMMass=DMMass,ConfidenceLevel=config.ConfidenceLevel)
    #Propeties of the halo 1)position on sky 2)radius, 3)Data for each halo 4) the index for the columns of 3)
    HaloPosition,HaloRadius,GroupSourcesData,GroupSourcesDataColumnNames=Library_LoadSelectedGalaxyGroups.Main(PSFfunct=HaloPSFSpline)
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
    print 'IndexOfSelectedElements',  len(IndexOfSelectedElements)
    print 'IndexOfSelectedElements1', len(IndexOfSelectedElements1)
    #sub selection of elements 
    FinalIndexOfElements=IndexOfSelectedElements[IndexOfSelectedElements1]

    HistOfdifferentValues(IndexOfSelectedElements=FinalIndexOfElements,
                          GroupSourcesData=GroupSourcesData,
                          GroupSourcesDataColumnNames=GroupSourcesDataColumnNames,
                          )
    return
                          

if __name__ == '__main__':
    Main()
