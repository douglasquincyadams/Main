"""
DESCRIPTION:

    Finds the maximum likelihoods of parameters:
        A,
        B,
        Gamma
    
    For a Single Pair of:
        Annihilation CrossSection
        Wimp Mass


"""
import numpy
import datetime
import matplotlib
#------------------------------------------------------------------------------

import scipy
import scipy.interpolate 

import Library_PrintDatasetStatistics
import Library_DataGetFermiInstrumentResponseEnergyDispersionFunction
import Library_GalaxyGroupDarkMatterModel
import Library_GenerateLikelihoodFunctionsDarkMatterGroupsFermiPhotons
import Library_MaximizeLikelihoodFunction
import Library_LocalStorageSaveVariable

import Library_PhotonsForGivenDMMass

import Library_GraphOneDimensionalHistogram
import matplotlib.pyplot as plt
def Main( 
    PossibleWimpMass = None, 
    PossibleAnnihilationCrossSections = None,
    WimpMassMultiAnnihilationCrossSectionLikelihoodCubeStorageName = None,
    DirectoryGeneratedGraphsCurrentRun=None,
    ):

    SelectedPhotonEnergies,GroupSourcesData,GroupSourcesDataColumnNames,FinalHaloIndex,EnergyMaxOut,EnergyMinOut=\
    Library_PhotonsForGivenDMMass.Main(DMMass=PossibleWimpMass)

    SelectedPhotonEnergies = numpy.atleast_2d( numpy.array(sorted(SelectedPhotonEnergies.tolist()) ) ).T
    """
    #size the graphs
    #   Default to common monitor size:  
    #   1920pixels by 1080 pixels
    #print 'Sizing the graphs...'
    #Inch_in_Pixels = 80.0
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
        BinMin = EnergyMinOut,
        BinMax = EnergyMaxOut,
        Xlabel = 'Energy',
        PlotTitle = 'Probability',
        )

    matplotlib.pylab.figure("MainHistogram")
    """
    plt.figure()
    plt.hist(SelectedPhotonEnergies,bins=50,log=True)
    plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/PhotonEnergies'+str(int(PossibleWimpMass))+'.png' )

    #Set photon energies
    WindowMinimumEnergy =EnergyMinOut
    WindowMaximumEnergy = EnergyMaxOut
    WindowPhotonEnergies=SelectedPhotonEnergies 
    WindowPhotonCount = len(WindowPhotonEnergies)
    print ' WindowPhotonCount', WindowPhotonCount




    MaximalParameters = (1.,1.,1.)

    TrialNumber = 0
    WimpMassMultiAnnihilationCrossSectionLikelihoodCube = []

    #Fit for the last few points of the Likelihood function
    SeriesCrossSections=numpy.zeros(5)	
    SeriesMaximalParametersA=numpy.ones(5)
    SeriesMaximalParametersB=numpy.ones(5)
    SeriesMaximalParametersC=numpy.ones(5)
    SeriesofMaxLikelhoods=numpy.ones(5)
    SuccessSeries=numpy.zeros(4,dtype=bool)
    logDelta03=1.0
    TheZeroValue=True
    InterpolateElements=False


    #Generate the dispersion Function for the fermi photons, based on the energy level for:
    EnergyDispersionIntegratedOverInclinationOverRegionOfInterest=\
        Library_DataGetFermiInstrumentResponseEnergyDispersionFunction.Main(
            SourceEnergy=PossibleWimpMass,
            WindowMinimumEnergy=WindowMinimumEnergy,
            WindowMaximumEnergy=WindowMaximumEnergy,
            
            )
    
    #Define a cluster sum dark matter model as a gaussian with a mean and variance 
    TotalJsmoothExposureFoldProbabilityDensityFunction = Library_GalaxyGroupDarkMatterModel.Main(
        GroupSourcesData = GroupSourcesData,
        GroupSourcesDataColumnNames = GroupSourcesDataColumnNames,
        PossibleWimpMass = PossibleWimpMass,
        Halo_index=FinalHaloIndex,
        )
    

    for PossibleAnnihilationCrossSection in PossibleAnnihilationCrossSections:
        print 'datetime.datetime.now()', datetime.datetime.now()
        print 'PossibleAnnihilationCrossSection', PossibleAnnihilationCrossSection

        #Get the functions we need for this combination of wimpmass and cross section:
        WimpMassAnnihilationCrossSectionFunctionInfo = Library_GenerateLikelihoodFunctionsDarkMatterGroupsFermiPhotons.Main(
            SelectedPhotonEnergies = WindowPhotonEnergies, 
            PossibleWimpMass = PossibleWimpMass,
            PossibleAnnihilationCrossSection = PossibleAnnihilationCrossSection,
            WindowStart = WindowMinimumEnergy ,
            WindowEnd = WindowMaximumEnergy ,
            EnergyDispersionFunctionForFermi=EnergyDispersionIntegratedOverInclinationOverRegionOfInterest,
            TotalJsmoothExposureFoldProbabilityDensityFunction=TotalJsmoothExposureFoldProbabilityDensityFunction,
            )
        PowerSpectrumPlusDispersionLogLikelihoodFunction    = WimpMassAnnihilationCrossSectionFunctionInfo["PowerSpectrumPlusDispersionLogLikelihoodFunction"]
        JfactorToSignalNormalization                        = WimpMassAnnihilationCrossSectionFunctionInfo["JfactorToSignalNormalization"]

        InitialGuessParameters = ( WindowPhotonCount, -3., 0.61705414092 * 10**37 )


        if (TrialNumber == 0):
            MaximalParameters = InitialGuessParameters

        ParameterSearchStartTime = datetime.datetime.now()

        if(logDelta03<0.05)&SuccessSeries[3]&TheZeroValue:
            print 'Generating Spline for Interpolation of Maximum Likelihood && Parameters'
            TheZeroValue=False
            InterpolateElements=True
            WimpMassAnnihilationCrossSectionFunctionInfo = Library_GenerateLikelihoodFunctionsDarkMatterGroupsFermiPhotons.Main(
                SelectedPhotonEnergies = WindowPhotonEnergies, 
                PossibleWimpMass = PossibleWimpMass     ,
                PossibleAnnihilationCrossSection = 0.0  ,
                WindowStart = WindowMinimumEnergy       ,
                WindowEnd = WindowMaximumEnergy         ,
                EnergyDispersionFunctionForFermi=EnergyDispersionIntegratedOverInclinationOverRegionOfInterest,
                TotalJsmoothExposureFoldProbabilityDensityFunction=TotalJsmoothExposureFoldProbabilityDensityFunction,                        
                )
            PowerSpectrumPlusDispersionLogLikelihoodFunction    = WimpMassAnnihilationCrossSectionFunctionInfo["PowerSpectrumPlusDispersionLogLikelihoodFunction"]
            JfactorToSignalNormalization                        = WimpMassAnnihilationCrossSectionFunctionInfo["JfactorToSignalNormalization"]

            #Find Max lLikelihood for zero cross section
            MaximalParameters,SuccessParameter = Library_MaximizeLikelihoodFunction.Main(
                LikelihoodFunction = PowerSpectrumPlusDispersionLogLikelihoodFunction, 
                StartParameters = numpy.array(MaximalParameters)*2, #(1600., -2., .01, GaussianMean, .01),
                PrintExtra = True,
                )
            MaximalLogLikelihoodValue = PowerSpectrumPlusDispersionLogLikelihoodFunction(MaximalParameters)
            #update MaxlLikelihoods
            SeriesofMaxLikelhoods=numpy.roll(SeriesofMaxLikelhoods,1)
            SeriesofMaxLikelhoods[0]=MaximalLogLikelihoodValue
            #update the SuccessParameters
            SeriesMaximalParametersA=numpy.roll(SeriesMaximalParametersA,1)
            SeriesMaximalParametersB=numpy.roll(SeriesMaximalParametersB,1)
            SeriesMaximalParametersC=numpy.roll(SeriesMaximalParametersC,1)
            SeriesMaximalParametersA[0]=MaximalParameters[0]
            SeriesMaximalParametersB[0]=MaximalParameters[1]
            SeriesMaximalParametersC[0]=MaximalParameters[2]
            #update Cross sections
            SeriesCrossSections=numpy.roll(SeriesCrossSections,1)
            SeriesCrossSections[0]=PossibleAnnihilationCrossSection
            #percent Change 	
            logDelta03=0.0
            
            print '      SeriesofMaxLikelhoods',SeriesofMaxLikelhoods
            print '      SeriesCrossSections',SeriesCrossSections   

            #generate Spline for Max Parameters and MaxlLikelihoods
            ASpline=scipy.interpolate.UnivariateSpline(SeriesCrossSections,SeriesMaximalParametersA)
            BSpline=scipy.interpolate.UnivariateSpline(SeriesCrossSections,SeriesMaximalParametersB)                       
            CSpline=scipy.interpolate.UnivariateSpline(SeriesCrossSections,SeriesMaximalParametersC)
            MaxLLikelihoodSpline=scipy.interpolate.UnivariateSpline(SeriesCrossSections,SeriesofMaxLikelhoods)
            #Generate updated Values for the parameters and the MaximumLLikelihood Values for the given cross section
            AparameterValue=ASpline(PossibleAnnihilationCrossSection)                    
            BparameterValue=BSpline(PossibleAnnihilationCrossSection)
            CparameterValue=CSpline(PossibleAnnihilationCrossSection)
            MaxLHValue=MaxLLikelihoodSpline(PossibleAnnihilationCrossSection)
            #transfer values to the old parameters
            MaximalParameters=numpy.array([AparameterValue,BparameterValue,CparameterValue])
            MaximalLogLikelihoodValue=MaxLHValue

        elif InterpolateElements:
            #Generate updated Values for the parameters and the MaximumLLikelihood Values for the given cross section
            AparameterValue=ASpline(PossibleAnnihilationCrossSection)                    
            BparameterValue=BSpline(PossibleAnnihilationCrossSection)
            CparameterValue=CSpline(PossibleAnnihilationCrossSection)
            MaxLHValue=MaxLLikelihoodSpline(PossibleAnnihilationCrossSection)
            #transfer values to the old parameters
            MaximalParameters=numpy.array([AparameterValue,BparameterValue,CparameterValue])
            MaximalLogLikelihoodValue=MaxLHValue
            print 'interpolation being used!'	


        else:
            #Determines the Maximum parameters
            MaximalParameters,SuccessParameter = Library_MaximizeLikelihoodFunction.Main(
                LikelihoodFunction = PowerSpectrumPlusDispersionLogLikelihoodFunction, 
                StartParameters = numpy.array(MaximalParameters)*2, #(1600., -2., .01, GaussianMean, .01),
                PrintExtra = True,
                )

            MaximalLogLikelihoodValue = PowerSpectrumPlusDispersionLogLikelihoodFunction(MaximalParameters)
            #update MaxlLikelihoods
            SeriesofMaxLikelhoods=numpy.roll(SeriesofMaxLikelhoods,1)
            SeriesofMaxLikelhoods[0]=MaximalLogLikelihoodValue
            #update the Convergence Success                        
            SuccessSeries=numpy.roll(SuccessSeries,1)
            SuccessSeries[0]=SuccessParameter
            #update the SuccessParameters
            SeriesMaximalParametersA=numpy.roll(SeriesMaximalParametersA,1)
            SeriesMaximalParametersB=numpy.roll(SeriesMaximalParametersB,1)
            SeriesMaximalParametersC=numpy.roll(SeriesMaximalParametersC,1)
            SeriesMaximalParametersA[0]=MaximalParameters[0]
            SeriesMaximalParametersB[0]=MaximalParameters[1]
            SeriesMaximalParametersC[0]=MaximalParameters[2]
            #update Cross sections
            SeriesCrossSections=numpy.roll(SeriesCrossSections,1)
            SeriesCrossSections[0]=PossibleAnnihilationCrossSection
            #percent Change 	
            logDelta03=numpy.abs((SeriesofMaxLikelhoods[0]-SeriesofMaxLikelhoods[3])/(SeriesofMaxLikelhoods[0]+SeriesofMaxLikelhoods[3])*2)

        print '         logDelta03',logDelta03   
        print '         SeriesCrossSections',SeriesCrossSections 
        print '         SuccessSeries',SuccessSeries	
        ParameterSearchEndTime = datetime.datetime.now()            
        ParameterSearchTimeTaken = ParameterSearchEndTime - ParameterSearchStartTime
        print 'ParameterSearchTimeTaken', ParameterSearchTimeTaken

        print '       MaximalParameters', MaximalParameters
        print '       MaximalLogLikelihoodValue', MaximalLogLikelihoodValue

        #Store all the data we looked up for this combination of mass and cross section
        WimpMassAnnihilationCrossSectionLikelihoodInfo = {
            "PossibleWimpMass"                  : PossibleWimpMass, 
            "PossibleAnnihilationCrossSection"  : PossibleAnnihilationCrossSection,
            "MaximalParameters"                 : MaximalParameters,
            "MaximalLogLikelihoodValue"         : MaximalLogLikelihoodValue,
            "InitialGuessParameters"            : InitialGuessParameters,
            "JfactorToSignalNormalization"      : JfactorToSignalNormalization,
            }

        if (PossibleAnnihilationCrossSection >= 0.0):
            WimpMassMultiAnnihilationCrossSectionLikelihoodCube.append(WimpMassAnnihilationCrossSectionLikelihoodInfo)


        TrialNumber += 1

    #Save the WimpMassMultiAnnihilationCrossSectionLikelihoodCube: 
    #   (This is all the data for 1 Potential Wimp Mass)
    Library_LocalStorageSaveVariable.Main(
        Variable = WimpMassMultiAnnihilationCrossSectionLikelihoodCube,
        VariableName = WimpMassMultiAnnihilationCrossSectionLikelihoodCubeStorageName,
        Overwrite = False,
        )

    return 'Finished'
