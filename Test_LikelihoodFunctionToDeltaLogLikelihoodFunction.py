
import numpy
#------------------------------------------------------------------------------
import Library_ModelFunctionGaussianTwoDimensionalMeanParameters

import Library_MaximizeLikelihoodFunction

#Function Transformations:
import Library_ModelFunctionToLikelihoodFunction
import Library_LikelihoodFunctionToDeltaLogLikelihoodFunction

import Library_PrintFullTestSuccess
import Library_OrderOfMagnitudeRatio

FullTestSuccess = True

#Fix a True Distrubtion Sample Point (An Observation)
TrueDistributionSamplePoint = numpy.array([1,1])

#Define a gaussian "Model Distribution" Definition 
#       Parameters -> Mu == [x1, y1]
#       Fixed -> covariance matrix
ModelDistributionDensityFunction = Library_ModelFunctionGaussianTwoDimensionalMeanParameters.Main


#Define the likelihood function as a fixed version of the Model Distribution Function
#   Model distribution function needs to be defined like above, as a function of 
#       [Point]
#       [Parameters]
#
#   The likelihood function has the Args:
#       [Parameters]
LikelihoodFunction = Library_ModelFunctionToLikelihoodFunction.Main(  \
    ModelFunction = ModelDistributionDensityFunction,           \
    TrueDistributionSamplePoint = TrueDistributionSamplePoint)

#Find the parameters which maximize the likelihood function which we defined above:
MaximumLikelihoodParameters = Library_MaximizeLikelihoodFunction.Main(\
    LikelihoodFunction = LikelihoodFunction, \
    ParameterCount = 2)

#Define a "Delta Log Likelihood" function:
DeltaLogLikelihoodFunction = Library_LikelihoodFunctionToDeltaLogLikelihoodFunction.Main(\
    LikelihoodFunction = LikelihoodFunction,\
    MaximumLikelihoodParameters = MaximumLikelihoodParameters )

"""BEGIN TESTS"""
#TODO: (Add more tests)
#Try out a Single Value:
Result = DeltaLogLikelihoodFunction(TrueDistributionSamplePoint)
ExpectedResult = 0.0

if (ExpectedResult - Result < 0.00001):
    print "Single Test Success"
else:
    FullTestSuccess = False
    print "Result", Result
    print "ExpectedResult", ExpectedResult
    print "Single Test Failure"
    



Library_PrintFullTestSuccess.Main(FullTestSuccess)



