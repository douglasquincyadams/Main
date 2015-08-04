"""
Description:
    Takes a "Likelihood Function:" and returns the corresponding "Delta Log Likelihood Function"

ARGS: (2 Count):
    1) LikelihoodFunction
        The "Likelihood Function" has the Args (1 Count):
            1) [Parameters]

    2) MaximumLikelihoodParameters
        This is a numpy array array
            N == Number of parameters
            MaximumLikelihoodParameters.Shape == (N,)

RETURNS (1 Count):

    Delta Log Likelihood Function:
        The "Delta Log Likelihood Function" has the Args (1 Count):
            1) [Parameters]


TESTS:
    Test_DeltaLogLikelihoodFunctionFromLikelihoodFunction

"""
import numpy

def Main(LikelihoodFunction = None, MaximumLikelihoodParameters = None, CheckArguments = True):

    #ArgumentChecking:
    if (CheckArguments):
        ArgrumentsExceptionMessage = ""
        if (LikelihoodFunction == None):
            ArgrumentsExceptionMessage += "(LikelihoodFunction == None)"
        if (MaximumLikelihoodParameters == None):
            ArgrumentsExceptionMessage += "(MaximumLikelihoodParameters == None)"
        if (len(ArgrumentsExceptionMessage) > 0):
            raise Exception(ArgrumentsExceptionMessage)

    #result = numpy.log( LikelihoodFunction(Parameters) ) - numpy.log( LikelihoodFunction(MaximumLikelihoodParameters) )
    DeltaLogLikelihoodFunction = lambda(Parameters): \
        numpy.log( LikelihoodFunction(Parameters) / LikelihoodFunction(MaximumLikelihoodParameters) )
    return DeltaLogLikelihoodFunction
















































