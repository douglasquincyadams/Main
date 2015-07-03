"""
Description:
    Generates a likelihood function out of the model function.
    Sets the the likelihood Function's Parameters to be = to the truedistribution 
    The parameters may or may not be exactly what matches to the point
    Especially if the point is a numpy.array() and the parameters are supposed to be a list of values


ARGS:
    ModelFunction
        Type: Python Function
        Description:

            REQUIRED
            Expects the model function to have the args:
                Point
                Parameters

    ModelIntegralFunction 
        Type: Python Function
        Description:
            A function of the indefinite integral of the model function
            EG:
                (Model == A * x ^ B )   

                   ||
                   VV   

                (ModelIntegral == (A / (B+1)) * x ^ (B + 1) )  V B!= -1

        Default:
            Returns 1
                assumes that the model provided is normalized as a 
                density function from minus infinity to infinity

    ModelProbabilityDensityFunction 
        Type:Python Function
        Description:
            A function which represents the probability of the number of observations 
            in the dataset given the normalization
        Default:
            Returns 1
                assumes that the provided model is already a probability density 
                and has a 100% of including all the points

    TrueDistributionSamplePoint
        Type: 
            `Type_NumpyTwoDimensionalDataPoint`
            `Type_NumpyTwoDimensionalDataset`
            
        Description:
            REQUIRED

            Can either be one single point, or a list of points
            If multiple points, then a JointLikelihood is returned


    StartDataPoint 
        Type:
        Description:
            Start of the window of which to integrate using the integration function
        Default:
            Smallest element of the domain of the dataset which is passed in
    EndDataPoint 
        Type:
        Description:
            End of the window of which to integrate using the itegration function
        Default:
            Largest element of the domain of the dataset which is passed in


    ReturnLogLikelihoodFunction 
        Type:
        Description:

RETURNS:
    Likelihood Function:
        The "Likelihood Function" has the Args (1 Count):
            1) [Parameters]

TESTS:
    Test_LikelihoodFunctionFromModelFunction

"""
import pprint
import numpy
import warnings

import Type_ModelFunction
import Type_NumpyTwoDimensionalDataPoint
import Type_NumpyTwoDimensionalDataset
import Library_DatasetGetMinimumDatapoint
import Library_DatasetGetMaximumDatapoint

def Main( 
    ModelFunction = None, 
    ModelIntegralFunction = None,
    ModelProbabilityDensityFunction = None,
    TrueDistributionSamplePoint  = None,    #Observation(s)
    StartDataPoint = None,                  #Window for model
    EndDataPoint = None,                    #Window for model
    ReturnLogLikelihoodFunction = False,    #If true - returned function returns loglikelihood

    CheckArguments = True,

    PrintExtra = False,
    PrintFailures = True,

    PrintExtraIndent = 0,
    ):

    PrintExtra = (PrintExtra == True or PrintExtraIndent != 0)
    if (PrintExtra):
        PntInd = ' '*PrintExtraIndent
    else:
        PntInd = ' '*4
    TypeTrueDistributionSamplePoint = None
    if (CheckArguments):
        ArgumentErrorMessage = ""
        if (Type_ModelFunction.Main(ModelFunction) == False):
            ArgumentErrorMessage += '(Type_ModelFunction.Main(ModelFunction) == False)\n'

        #TrueDistributionSamplePoint Type Checking:
        if ( Type_NumpyTwoDimensionalDataPoint.Main(TrueDistributionSamplePoint) == True ):
            TypeTrueDistributionSamplePoint = 'Type_NumpyTwoDimensionalDataPoint'

        elif ( Type_NumpyTwoDimensionalDataset.Main(TrueDistributionSamplePoint) == True ):
            TypeTrueDistributionSamplePoint = 'Type_NumpyTwoDimensionalDataset'

        else:
            ArgumentErrorMessage += 'type(TrueDistributionSamplePoint) not recognized \n'

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    if (PrintExtra):
        print PntInd + 'TrueDistributionSamplePoint:'
        pprint.pprint(TrueDistributionSamplePoint)
        print PntInd + 'TypeTrueDistributionSamplePoint', TypeTrueDistributionSamplePoint

    #Integral normalization:
    #   Normalization = ModelIntegral from start to end
    #   Default is set to 1 
    if (ModelIntegralFunction != None):
        if (StartDataPoint == None):
            if (TypeTrueDistributionSamplePoint == 'Type_NumpyTwoDimensionalDataset'):
                StartDataPoint = Library_DatasetGetMinimumDatapoint.Main(TrueDistributionSamplePoint)
            else:
                raise Exception('StartDataPoint == None && TrueDistributionSamplePoint is 1 point')
        if (PrintExtra):
            print PntInd + 'StartDataPoint', StartDataPoint

        if (EndDataPoint == None):
            if (TypeTrueDistributionSamplePoint == 'Type_NumpyTwoDimensionalDataset'):
                EndDataPoint = Library_DatasetGetMaximumDatapoint.Main(TrueDistributionSamplePoint)
            else:
                raise Exception('EndDataPoint == None && TrueDistributionSamplePoint is 1 point')
        if (PrintExtra):
            print PntInd + 'EndDataPoint', EndDataPoint

        def ModelDefiniteIntegral(Parameters):
            IntegralStart = ModelIntegralFunction(StartDataPoint, Parameters )
            IntegralEnd = ModelIntegralFunction(EndDataPoint , Parameters)
            Result = IntegralEnd - IntegralStart
            return Result #This is the expected number of observations
    else:
        def ModelDefiniteIntegral(Parameters):
            return 1.

    #Probability Density Normalization:
    #   Default the  is set to 1
    if (ModelProbabilityDensityFunction == None):
        def ModelProbabilityDensityFunction( 
            ObservationCount  = None,
            ExpectedNumberOfObservations = None,
            ):
            return ExpectedNumberOfObservations

    #Get some Dataset Statistics:
    ObservationCount = 0
    if (TypeTrueDistributionSamplePoint == 'Type_NumpyTwoDimensionalDataPoint'):
        TrueDistributionSamplePoint = numpy.array([TrueDistributionSamplePoint])
        ObservationCount = 1.
    else:
        ObservationCount = len(TrueDistributionSamplePoint)
    if ( PrintExtra ):
        print PntInd + 'ObservationCount', ObservationCount


    ###########################################################################
    #   BUILD THE LIKELIHOOD FUNCTION    
    ###########################################################################
    def LikelihoodFunction ( Parameters ): 
        Impossible = False
        ImpossibleValue = 0
        ImpossibleValueLog = -1*numpy.inf


        if ( PrintExtra ):
            print '\nParameters', Parameters

        #ExpectedNumberOfObservations
        #   The number of observations we expect to see in the window 
        #   The area under the model curve
        ExpectedNumberOfObservations = ModelDefiniteIntegral(Parameters)
        if ( PrintExtra ):
            print PntInd + ' ExpectedNumberOfObservations', ExpectedNumberOfObservations


        #Probability Observation Count
        #   The probability that we have :
        #       `N observed events` 
        #       given 
        #       `expected Lambda Events`
        ProbabilityObservationCount = 0
        if (ReturnLogLikelihoodFunction):
            ProbabilityObservationCount = ModelProbabilityDensityFunction(
                Parameters = Parameters, 
                ObservationCount = ObservationCount,
                ExpectedNumberOfObservations = ExpectedNumberOfObservations,
                Log = ReturnLogLikelihoodFunction,
                )
        else:
            ProbabilityObservationCount = ModelProbabilityDensityFunction(
                ObservationCount = ObservationCount,
                ExpectedNumberOfObservations = ExpectedNumberOfObservations,
                )

        if ( PrintExtra ):
            print PntInd + ' ProbabilityObservationCount', ProbabilityObservationCount

        if (ReturnLogLikelihoodFunction):
            if (ProbabilityObservationCount == -1*numpy.inf ):
                return ImpossibleValueLog

        else:
            if (ProbabilityObservationCount == 0 ):
                return ImpossibleValue



        #Start off the likelihood as the probability of seeing the number of observations you have:
        Result = ProbabilityObservationCount

        #Loop through the points and multiply by the probability of seeing that point:
        for SingleTrueDistributionSamplePoint in TrueDistributionSamplePoint:

            #Find the likelihood of the model given a single observation:
            ModelLikelihoodResultOnePoint = 0
            try:
                ModelLikelihoodResultOnePoint = ModelFunction( 
                    DataPoint = SingleTrueDistributionSamplePoint, 
                    Parameters = Parameters ,
                    )
            except Exception, E:
                if ( PrintFailures ):
                    print '*ERROR*: ModelLikelihoodResultOnePoint '
                    print 'E' , str(E)
                    print PntInd + 'ModelLikelihoodResultOnePoint', ModelLikelihoodResultOnePoint
                    print PntInd + 'Parameters', Parameters

                if (ReturnLogLikelihoodFunction):
                    return ImpossibleValueLog
                else:
                    return ImpossibleValue

            if ( PrintExtra > 1): #True == 1
                print PntInd + ' ModelLikelihoodResultOnePoint', ModelLikelihoodResultOnePoint


            #Divide by the expected number of observations we are expecting to see: 
            NormalizedLikelihoodResultOnePoint = ModelLikelihoodResultOnePoint / ExpectedNumberOfObservations
            if (NormalizedLikelihoodResultOnePoint <= 0):
                if ( PrintFailures ):
                    print '*WARNING* NormalizedResultOnePoint'
                    print PntInd + 'NormalizedResultOnePoint <= 0'
                    print PntInd + 'ModelLikelihoodResultOnePoint', ModelLikelihoodResultOnePoint
                    print PntInd + 'ExpectedNumberOfObservations', ExpectedNumberOfObservations
                    print PntInd + 'NormalizedLikelihoodResultOnePoint', NormalizedLikelihoodResultOnePoint
                    print PntInd + 'Parameters', Parameters

                if (ReturnLogLikelihoodFunction):
                    return ImpossibleValueLog
                else:
                    return ImpossibleValue

            if ( PrintExtra > 1): #True == 1
                print PntInd + 'NormalizedLikelihoodResultOnePoint', NormalizedLikelihoodResultOnePoint


            #Add the likelihood for a single datapoint to the total result
            if (ReturnLogLikelihoodFunction):           
                Result += numpy.log(NormalizedLikelihoodResultOnePoint)   #Sum log likelihoods
            else:
                Result *= NormalizedLikelihoodResultOnePoint              #Product likelihoods



        if ( PrintExtra ):
            print ' '*PrintExtraIndent + 'Likelihood: ', Result

        return Result 


    ###########################################################################




    return LikelihoodFunction





































