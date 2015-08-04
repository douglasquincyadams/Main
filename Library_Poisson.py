"""
SOURCE:
    http://en.wikipedia.org/wiki/Poisson_distribution

DESCRIPTION:

    Approximiation to the Binomial
        p = probability of an event sucess
        N = total number of events
        Lambda = N*p
        k = the number of observed success

    Probability( k ) = lambda^k * e ^ -lambda / k!

ARGS:
    K
        the number of observed success
    Lamda
        N*p
        Expected Value
        Variance

RETURNS:

"""

import math
import numpy
import scipy
import scipy.special

def Main(
    K = None,
    Lambda = None,
    Log = False,
    CheckArguments = True,
    PrintExtra = False,
    ):
    if (CheckArguments):
        ArgumentErrorMessage = ""
        if (K == None):
            ArgumentErrorMessage += '(K == None)\n'
        if (Lambda == None):
            ArgumentErrorMessage += '(Lambda == None)\n'
        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    if (Lambda == 0 ):
        if (K == 0):
            if (Log):
                return 0
            else:
                return 1
        else:
            if (Log):
                return -1.*numpy.inf
            else:
                return 0 

    elif (Lambda < 0):
        if (Log):
            return -1.*numpy.inf
        else:
            return 0 

    elif (Lambda == numpy.inf):
        if (Log):
            return -1.*numpy.inf
        else:
            return 0 

    else:
        pass

    #LogFactorialK = numpy.log( K * numpy.log(K) - K + 1./2. * numpy.log(2.* numpy.pi* K) )

    #(Lambda**K) * (numpy.e**(-1.*Lambda)) / (FactorialK)
    LogLambdaToTheK = K * numpy.log(Lambda)
    LogEToTheMinusLambda = -1.*Lambda
    LogFactorialK = scipy.special.gammaln(K+1)

    Result = LogLambdaToTheK +  LogEToTheMinusLambda - LogFactorialK

    if (Log == False):        
        Result = numpy.e**Result


    return Result
































