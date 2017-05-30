"""
SOURCE:

    #Fixing minimization functions to work correctly:
        http://stats.stackexchange.com/questions/126251/how-do-i-force-the-l-bfgs-b-to-not-stop-early-projected-gradient-is-zero

    #Cubic Functions:
        Zeros:
        http://www.math.vanderbilt.edu/~schectex/courses/cubic/

        Inverse:
        https://www.physicsforums.com/threads/inverse-of-cubic-functions.47117/

    #Likelihood function:
        https://drive.google.com/file/d/0BzalK-Lkp6OyR3NuM2l0clBnVTA/view?usp=sharing

    #Goal graph1:
        https://drive.google.com/file/d/0BzalK-Lkp6OyOE5lOTNwamtYTHc/view?usp=sharing

    #Goal graph2:
        https://drive.google.com/file/d/0BzalK-Lkp6OydG9IU25Ca0VGNEE/view?usp=sharing


    #Multiple Matplotlib Figures -> Control opening, referencing and closing them:
        http://stackoverflow.com/questions/21884271/warning-about-too-many-open-figures
        http://stackoverflow.com/questions/7986567/matplotlib-how-to-set-the-current-figure

DESCRIPTION:

    Does a likelihood analysis using:
        fermi photons, 
        Galaxy clusters

    Looks for a feature on top of a power law in an energy spectrum


    Currently the only feature that is being searched for is a delta function of `True Emission`

        This is the equivalent of searching for the fermi energy_dispersion function in `Observed Emission`


ARGS:


RETURNS:



"""


import math
import scipy
import scipy.interpolate 

from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.interpolate import UnivariateSpline

import inspect
import os
import pprint
import numpy
import scipy
import scipy.stats
import matplotlib
import matplotlib.pylab
import datetime
import matplotlib.pylab as plt
import numpy as np
#------------------------------------------------------------------------------


import Const_LocalStorageTemp
import Const_LocalDirectoriesFermiFiles
import Const_LocalDirectoriesGalaxyGroupsFiles


import Library_DateStringNowGMT
import Library_DataGetAllGalaxyGroups
import Library_GalaxyGroupDarkMatterModel
import Library_GeneratePolynomial
import Library_GraphOneDimensionalKernelDensity
import Library_GraphOneDimensionalHistogram
import Library_Gaussian
import Library_GaussianIndefiniteIntegral
import Library_OrderOfMagnitudeRatio
import Library_OrderOfMagnitudeRatioSmallCheck
import Library_MaximizeLikelihoodFunction
import Library_LocalStorageSaveVariable
import Library_LocalStorageLoadVariable
import Library_PrintDatasetStatistics
import Library_LeastSquaresLinearFindCoefficients
import Library_EvaluateFunctionsAtNumpyDataPoints
import Library_DatasetGetMaximumDatapoint
import Library_DatasetGetMinimumDatapoint
import Library_ChiSquaredDeltaLogLikelihoodToConfidenceLevel
import Library_ChiSquaredConfidenceLevelToDeltaLogLikelihoodMaximum
import Library_DataGetFermiInstrumentResponseEnergyDispersionFunction


import Library_GenerateLikelihoodFunctionsDarkMatterGroupsFermiPhotons
import Library_FermiEnergySpectrumFeatureSearchConfidence
import Library_FermiEnergySpectrumFeatureSearchWimp

import Library_ParallelLoop



def Main(    
    SelectedPhotonEnergies = None,
    DirectoryGeneratedGraphs = None,
    GroupSourcesData = None, 
    GroupSourcesDataColumnNames = None,
    ):

    DatasetEnergyDomainMin = numpy.min(SelectedPhotonEnergies)
    DatasetEnergyDomainMax = numpy.max(SelectedPhotonEnergies)
    DataWindowLinSpaceInputs = numpy.linspace(DatasetEnergyDomainMin, DatasetEnergyDomainMax, 1000)

    #GRAPHS:
    #Setup the directories
    if (True):#DirectoryGeneratedGraphsCurrentRun == None):
        DirectoryGeneratedGraphsCurrentRun = DirectoryGeneratedGraphs + "/" + Library_DateStringNowGMT.Main()
        if not os.path.exists(DirectoryGeneratedGraphsCurrentRun):
            os.makedirs(DirectoryGeneratedGraphsCurrentRun)
        GraphFileNamePrefix = Library_DateStringNowGMT.Main()[0:11]

    #size the graphs
    #   Default to common monitor size:  
    #   1920pixels by 1080 pixels
    print 'Sizing the graphs...'
    Inch_in_Pixels = 80.0
    MonitorSize = (1920.0/Inch_in_Pixels,1080.0/Inch_in_Pixels)

    print 'Making Graphs...'
    matplotlib.pylab.figure("MainHistogram" , figsize = MonitorSize)


    #Energies Histogram:
    print '   Making Histogram...'
    matplotlib.pylab.figure("MainHistogram")
    BinCount = 50
    Library_GraphOneDimensionalHistogram.Main(
        ObservedDataset = SelectedPhotonEnergies, 
        BinCount = BinCount,
        LogCounts = True,
        LogX = True,
        NormalizeToBinWidths = True,
        BinMin = DatasetEnergyDomainMin,
        BinMax = DatasetEnergyDomainMax,
        Xlabel = 'Energy',
        PlotTitle = 'Probability',
        )

    matplotlib.pylab.figure("MainHistogram")
    matplotlib.pylab.savefig( DirectoryGeneratedGraphsCurrentRun + '/PhotonEnergies.png' )

    #Possible Wimp Masses
    #Try wimp masses equal to the energies we expect to see
    print 'Determining PossibleWimpMasses...'
    PossibleWimpMassCount = 2
    PossibleWimpMasses = numpy.linspace( 250000 ,300000, PossibleWimpMassCount)# DatasetEnergyDomainMax/2., 2)
    PossibleWimpMassCount = len(PossibleWimpMasses)
    print 'PossibleWimpMasses'
    pprint.pprint(PossibleWimpMasses.tolist())


    print 'Determining PossibleAnnihilationCrossSections...'
    PossibleAnnihilationCrossSections = [10**(-25)]
    NumberPerDecade = 3
    NumberDecades = 6	
    Divisor = math.log( 10, NumberPerDecade)
    PossibleExp = range(NumberPerDecade * NumberDecades)
    for k in  PossibleExp :
        PossibleAnnihilationCrossSections.append(PossibleAnnihilationCrossSections[-1]/Divisor)
    PossibleAnnihilationCrossSections.append(0.)
    PossibleAnnihilationCrossSections = numpy.array(PossibleAnnihilationCrossSections)
    print 'PossibleAnnihilationCrossSections'
    pprint.pprint(PossibleAnnihilationCrossSections.tolist())


    #Maximum Parameters Per Mass Per Annihilation Cross Section:
    print 'Finding Maximal Parameters per WimpMass && Annihilation Cross Section Combination...'



    
    WimpMassArgSets = []
    for PossibleWimpMass in PossibleWimpMasses:

        #Check if we have already done the work on this wimp mass:
        WimpMassMultiAnnihilationCrossSectionLikelihoodCubeStorageName = 'WimpMassMultiAnnihilationCrossSectionLikelihoodCube_' + str(PossibleWimpMass)
        WimpMassMultiAnnihilationCrossSectionLikelihoodCube = Library_LocalStorageLoadVariable.Main(
            VariableName = WimpMassMultiAnnihilationCrossSectionLikelihoodCubeStorageName,
            )
        PossibleWimpMassAlreadyDone = (WimpMassMultiAnnihilationCrossSectionLikelihoodCube != None)
        #print ' PossibleWimpMass', PossibleWimpMass
        #print ' PossibleWimpMassAlreadyDone', PossibleWimpMassAlreadyDone

        if (not PossibleWimpMassAlreadyDone):
            WimpMassArgSets.append(
                    {
                        "PossibleWimpMass"  :  PossibleWimpMass , 
                        "DatasetEnergyDomainMin" : DatasetEnergyDomainMin,
                        "SelectedPhotonEnergies" : SelectedPhotonEnergies,
                        "GroupSourcesData"  : GroupSourcesData,
                        "GroupSourcesDataColumnNames" : GroupSourcesDataColumnNames,
                        "PossibleAnnihilationCrossSections" : PossibleAnnihilationCrossSections,
                        "WimpMassMultiAnnihilationCrossSectionLikelihoodCubeStorageName" : WimpMassMultiAnnihilationCrossSectionLikelihoodCubeStorageName,
                    }
                )

    print 'Running the following set of ARGS:'
    #pprint.pprint( WimpMassArgSets )
    for ArgSet in WimpMassArgSets:
        print  'WimpMassArgSets["PossibleWimpMass"]', ArgSet["PossibleWimpMass"]



    ResultList = Library_ParallelLoop.Main(
        Function = Library_FermiEnergySpectrumFeatureSearchWimp.Main,
        ListOfArgSets = WimpMassArgSets,
        Algorithm = 'pp',
        )


    Library_FermiEnergySpectrumFeatureSearchConfidence.Main(
        PossibleWimpMasses = PossibleWimpMasses,
        PossibleAnnihilationCrossSections = PossibleAnnihilationCrossSections,
        DirectoryGeneratedGraphsCurrentRun = DirectoryGeneratedGraphsCurrentRun
        )






































