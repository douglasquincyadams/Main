#!/usr/bin/env python



"""
elements in GalaxyDataColumns for which we can select for
['GalaxyCount', 'VelocityInCmPerSec', 'MassInGrams', 'GalacticLongitudeInDegrees', 'GalacticLatitudeInDegrees',
 'DistanceInCm', 'Jsmooth', 'RvirInCm', 'VisualAngleInDegrees', 'IntensityInJPerDegreesSquared', 'Jclumpy']
"""

import pylab as py


def Main(
        GroupSourcesData=None,
        GroupSourcesDataColumnNames=None,
        GroupType=None,
        MaxValue=None,
        MinValue=None,
        IndexOfSelectedElements=None,
        ):


    if GroupType==None:
        print 'No Selection Made'
        return
    elif IndexOfSelectedElements==None:
        GroupTypeElements=GroupSourcesData[:,[GroupSourcesDataColumnNames.index(GroupType)] ].T[0]
        #print ' GroupTypeElements.shape-',GroupTypeElements.shape
        IndexOfSelectedElements=py.find((GroupTypeElements>MinValue)&(GroupTypeElements<MaxValue))
        return IndexOfSelectedElements
    else:
        GroupTypeElements=GroupSourcesData[:,[GroupSourcesDataColumnNames.index(GroupType)]].T[0]
        GroupTypeElements=GroupTypeElements[IndexOfSelectedElements]
        #print ' GroupTypeElements.shape-',GroupTypeElements.shape
        IndexOfSelectedElements2=py.find((GroupTypeElements>MinValue)&(GroupTypeElements<MaxValue))
        return IndexOfSelectedElements2
    













if __name__ == '__main__':
    Main()
    
