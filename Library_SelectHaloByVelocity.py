#!/usr/bin/env python



"""
elements in GalaxyDataColumns
['GalaxyCount', 'VelocityInCmPerSec', 'MassInGrams', 'GalacticLongitudeInDegrees', 'GalacticLatitudeInDegrees', 'DistanceInCm', 'Jsmooth', 'RvirInCm', 'VisualAngleInDegrees', 'IntensityInJPerDegreesSquared', 'Jclumpy']
"""

import pylab as py


def Main(
        GroupSourcesData=None,
        GroupSourcesDataColumnNames=None,
        GroupType=None,
        ):


    if GroupType==None:
        return print 'No Selection Made'
    else
        GroupTypeElements=GroupSourcesData[:,[GroupSourcesDataColumnNames.index(GroupType)] ]
        print GroupTypeElements.shape
        

    print GroupSourcesDataColumnNames













if __name__ == '__main__':
    Main()
    
