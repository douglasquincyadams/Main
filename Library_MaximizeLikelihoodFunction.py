

"""
Maximizes the a likelyhood function.

#   Expects the likelihood function to have only the arg:
#       Parameters

"""
import numpy
import scipy
import scipy.optimize
from scipy.optimize import minimize #This is retarded - but required. We cannot simply import scipy.optimize.minimize


def Main(
    LikelihoodFunction = None,
    ParameterCount = None,
    StartParameters = None,
    Constraints = None,
    CheckArguments = True,
    PrintExtra = False,
    ):

    #Do some arguement checking here:
    if (CheckArguments):
        ArguementsErrorMessage = ""
        if (LikelihoodFunction == None):
            ArguementsErrorMessage += "(LikelihoodFunction == None)"
        if (ParameterCount == None and StartParameters == None):
            ArguementsErrorMessage += "(ParameterCount == None)"
        if (len(ArguementsErrorMessage) > 0 ):
            raise Exception(ArguementsErrorMessage)

    if (StartParameters == None):
        #Start off the minimization function at the origin == [0,0,0....0] 
        StartParameters = numpy.zeros(shape = (ParameterCount,) )

    if (ParameterCount == None):
        ParameterCount = len(StartParameters)

    #Define a "Negative Likelihood Function" 
    NegativeLikelihoodFunction = lambda(Parameters):  (-1.0)*LikelihoodFunction(Parameters)


    options = {
        "xtol" : 0.1,
        "ftol" : 0.01,
        "maxfev": 1000,
        "disp": True,
    }


    #Maximize the likelihood function( by minimizing he negative likelyhood function)
    MaximumResult = scipy.optimize.minimize(
        NegativeLikelihoodFunction, 
        StartParameters,
        #method = 'SLSQP',
        #method = 'BFGS',
        method = 'Nelder-Mead', #Seems to work well for likelihood
        #method = 'Powell',	        
        #constraints = Constraints,
        #bounds = [(None, None),(-3, None)]
        options = options,
        )

        


    if (PrintExtra):
        print 'MaximumResult', MaximumResult

    MaximumLikelihoodParameters = MaximumResult.x, MaximumResult.success 
    return MaximumLikelihoodParameters




























