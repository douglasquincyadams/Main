#!/usr/bin/env python 

import DS_LoadPhotonsForEnergyRange



def Main():

    EventLocations3D,EventEnergies,EnergyMax,EnergyMin=DS_LoadPhotonsForEnergyRange.Main(EnergyMax=5.e5, EnergyMin=4.8e5)

    #print EventsColumnNames
    #print 'Helo'
    print EventLocations3D.shape
    print EnergyMax/1.e3,EnergyMin/1.e3
    return

if __name__ == '__main__':
    Main()

