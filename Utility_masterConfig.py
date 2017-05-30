"""
Setst the parameters to be run in the Program
such as the Drk matter Mass (in MeV), The boost factor

as well as selecting on the the Halos of Interest



"""

import Config_AstronomyConstants as AstroCnst
import numpy as np

#set Range of annihilation Cross section
PossibleAnnihilationCrossSections=[1e-16]
NumberPerDecade=6
NumberDecades=11

#Confidence Level to Search for For the different galaxies.
ConfidenceLevel=0.95
PointSourceConfidenceLevel=0.95

#selection of Galaxy Groups
#subselection 1

GroupType0='VelocityInCmPerSec'
MaxValue0=3.e4*AstroCnst.Km_in_cm
MinValue0=.5e3*AstroCnst.Km_in_cm

#subselection 2
GroupType1='MassInGrams'
MaxValue1=5e16*AstroCnst.MassSolar_in_grams
MinValue1=1e13*AstroCnst.MassSolar_in_grams

#variance of GalaxyGroup
GalaxyGroupVariance=None # can put in indiviudal variances for different groups allow for includding uncertainties in the paramters of the group

#boost factor for Halos
BoostFactor=10.  #Boost due to substructure Follwing Han et al 2012 from Miguel Sanchez reasonable Boost factor between 200 and 5 with best guess at around 40


#storage of Data Directory

Directory = '../TempDataStore/'

#storage of Images

GeneratedGraphs='../GeneratedGraphs'
GeneratedGraphsGalaxyGroup =GeneratedGraphs+'/GalaxyGroupsSkyMap'




#Pointsources Constraints-The cut off of elements
#at 20 perecnt eliminates nearly 80 percent of the possible photons.
#elimnating the Brightest []percent of Sources
#if .2 then the 20 percent brightest sources are elimnated.

PointSourceCuttoff=0.1

#determines the number of photons 
NumberOfPhotons=3000


#Masses to  search over

PossibleWimpMassCount=2

MinMassRange=2.1e5
MaxMassRange=3.1e5
