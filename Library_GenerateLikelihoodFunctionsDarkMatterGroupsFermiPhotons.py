"""
    Define ModelFunctions per wimp mass, per cross section

"""

import warnings
import copy
#------------------------------------------------------------------------------
import Library_ModelFunctionToLikelihoodFunction
import Library_Poisson


def Main(
    PossibleWimpMass = None,
    PossibleAnnihilationCrossSection = None,

    SelectedPhotonEnergies = None,
    WindowStart = None,
    WindowEnd = None,


    EnergyDispersionFunctionForFermi= None,
    TotalJsmoothExposureFoldProbabilityDensityFunction=None,
    ):

    #Fixed for a wimp mass:
    #   WindowMinimumEnergy
    #   WindowMaximumEnergy

    #Fixed for all wimp masses, and all annihilation cross sections
    #   GroupSourcesData
    #   GroupSourcesDataColumnNames




    #Fix the energy dispersion function based on the (WimpMass == RecievedPhotonEnergy)
    EnergyDispersionIntegratedOverInclinationOverRegionOfInterest = \
        copy.deepcopy( EnergyDispersionFunctionForFermi )

    #Signal Probability Density Normalization:
    JfactorToSignalNormalization = PossibleAnnihilationCrossSection / (PossibleWimpMass**2)
    JfactorToSignalNormalization = copy.deepcopy( JfactorToSignalNormalization )

    #Define a model function of signal (changes for each wimp mass)
    def PowerSpectrumPlusDispersionModelFunction( 
        DataPoint = None,
        Parameters = None, 
        ):
        DataPoint = DataPoint - WindowStart

        A = Parameters[0]
        B = Parameters[1]

        Gamma = Parameters[2]

        #Define the power law part of the fit:
        PowerLawTerm = A * (DataPoint**(B))

        C = Gamma*JfactorToSignalNormalization

        #Define the energy dispersion part of the fit:
        DispersionTerm = C*EnergyDispersionIntegratedOverInclinationOverRegionOfInterest(
            Energy = DataPoint,
            )

        return PowerLawTerm + DispersionTerm
    PowerSpectrumPlusDispersionModelFunction = copy.deepcopy( PowerSpectrumPlusDispersionModelFunction )


    #Define the integral of the model function (changes for each wimp mass)
    def PowerSpectrumPlusDispersionIntegralFunction(
        DataPoint = None,
        Parameters = None, #A, B
        ):
        DataPoint = DataPoint - WindowStart + 0.1

        A = Parameters[0]
        B = Parameters[1]

        Gamma = Parameters[2]

        PowerLawIndefiniteIntegralValue = 0
        with warnings.catch_warnings():
            warnings.filterwarnings('error')
            try:
                if (B == -1.):
                    PowerLawIndefiniteIntegralValue = A*numpy.log(DataPoint)
                else:
                    PowerLawIndefiniteIntegralCoefficient = (A / (B + 1.))
                    PowerLawIndefiniteIntegralPower = ( DataPoint**(B + 1.)  )
                    PowerLawIndefiniteIntegralValue = PowerLawIndefiniteIntegralCoefficient * PowerLawIndefiniteIntegralPower

            except Warning, warning:
                print 'Warning Message:', str(warning)
                print 'DataPoint', DataPoint
                print 'Parameters', Parameters
                #print 'PowerLawIndefiniteIntegralCoefficient', PowerLawIndefiniteIntegralCoefficient
                #print 'PowerLawIndefiniteIntegralPower', PowerLawIndefiniteIntegralPower
                #print 'PowerLawIndefiniteIntegralValue', PowerLawIndefiniteIntegralValue
                assert(False)
        

        #We are going to assume that the integral of the normalized dispersion function 
        #   from one side of the window to the other sider of the window is exactly 1
        #   (We are assuming that the entire dispersion is between our two window edges)
        if (DataPoint < PossibleWimpMass):
            DispersionTermIndefiniteIntegralValue = 0 
        else:
            DispersionTermIndefiniteIntegralValue = Gamma * JfactorToSignalNormalization

        IndefiniteIntegralValue = PowerLawIndefiniteIntegralValue + DispersionTermIndefiniteIntegralValue

        return IndefiniteIntegralValue
    PowerSpectrumPlusDispersionIntegralFunction = copy.deepcopy(PowerSpectrumPlusDispersionIntegralFunction)



    #Define a probability density function assuption:
    def PowerSpectrumPlusDispersionProbabilityDensityFunction( 
        Parameters = None,
        ObservationCount  = None,
        ExpectedNumberOfObservations = None,
        Log = False,
        ):
        Gamma = Parameters[2]
        ProbabilityPoissonPowerLaw = Library_Poisson.Main(
            K = ObservationCount,
            Lambda = ExpectedNumberOfObservations,
            Log = Log,
            )
        #print 'ProbabilityPoissonPowerLaw', ProbabilityPoissonPowerLaw
        ProbabilityDarkMatterJsmooth = TotalJsmoothExposureFoldProbabilityDensityFunction(
            TotalJfactor = Gamma,
            Log = Log,
            )
        #print 'ProbabilityDarkMatterJsmooth', ProbabilityDarkMatterJsmooth
        Result = 0 
        if (Log):
            Result = ProbabilityPoissonPowerLaw + ProbabilityDarkMatterJsmooth
        else:
            Result = ProbabilityPoissonPowerLaw * ProbabilityDarkMatterJsmooth
        return Result
    PowerSpectrumPlusDispersionProbabilityDensityFunction = copy.deepcopy(PowerSpectrumPlusDispersionProbabilityDensityFunction)



    #Define a loglikelihood function out of the other 3 functions:
    PowerSpectrumPlusDispersionLogLikelihoodFunction = Library_ModelFunctionToLikelihoodFunction.Main(
        ModelFunction                   = PowerSpectrumPlusDispersionModelFunction, 
        ModelIntegralFunction           = PowerSpectrumPlusDispersionIntegralFunction,
        ModelProbabilityDensityFunction = PowerSpectrumPlusDispersionProbabilityDensityFunction,
        TrueDistributionSamplePoint     = SelectedPhotonEnergies,
        StartDataPoint                  = WindowStart ,
        EndDataPoint                    = WindowEnd ,
        ReturnLogLikelihoodFunction     = True,
        #PrintFailures = True,
        #PrintExtraIndent = 2,
        )
    PowerSpectrumPlusDispersionLogLikelihoodFunction = copy.deepcopy( PowerSpectrumPlusDispersionLogLikelihoodFunction)


    WimpMassAnnihilationCrossSectionFunctionInfo = {
        "EnergyDispersionIntegratedOverInclinationOverRegionOfInterest" : EnergyDispersionIntegratedOverInclinationOverRegionOfInterest,
        "JfactorToSignalNormalization"                          : JfactorToSignalNormalization,
        "PowerSpectrumPlusDispersionModelFunction"              : PowerSpectrumPlusDispersionModelFunction ,
        "PowerSpectrumPlusDispersionIntegralFunction"           : PowerSpectrumPlusDispersionIntegralFunction,
        "PowerSpectrumPlusDispersionProbabilityDensityFunction" : PowerSpectrumPlusDispersionProbabilityDensityFunction,                         
        "PowerSpectrumPlusDispersionLogLikelihoodFunction"      : PowerSpectrumPlusDispersionLogLikelihoodFunction,
    }
        

    return WimpMassAnnihilationCrossSectionFunctionInfo


