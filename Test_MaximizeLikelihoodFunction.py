import numpy
#------------------------------------------------------------------------------
import Library_Gaussian
import Library_MaximizeLikelihoodFunction
import Library_OrderOfMagnitudeRatio
import Library_PrintFullTestSuccess

FullTestSuccess = True

#For this test we define a likelihood function of 2 parameters:
#   This likelihood function is of exactly 2 parameters:
def LikelihoodFunction(Parameters):
    Point = numpy.array(Parameters)
    MeanPoint = numpy.array([1,1])
    CovarianceMatrix = numpy.identity(2)
    return Library_Gaussian.Main(Point = Point, MeanPoint = MeanPoint, CovarianceMatrix = CovarianceMatrix )

#We need to tell the maximization function either
#   how many parameters the likelihood function expects as inputs:
#   OR
#   what parameters to start off trying
ParameterCount = 2


#Intuitively - we know that the following:
#   the likelihood function is a gaussian 
#   the gaussian is has mean [1,1]
#   The gaussian is centered at it's mean
#   The maximum should be at the location of the mean
MaximalParameters = Library_MaximizeLikelihoodFunction.Main(
    LikelihoodFunction = LikelihoodFunction, 
    ParameterCount = ParameterCount ,
    )


ExpectedMaximalParameters = numpy.array([1,1])
NumParameters = len(MaximalParameters)
k = 0
while ( k < NumParameters ):
    MaximalParameter = MaximalParameters[k]
    ExpectedMaximalParameter = ExpectedMaximalParameters[k]
    OrderOfMagnitudeRatio = Library_OrderOfMagnitudeRatio.Main(MaximalParameter, ExpectedMaximalParameter)
    if (OrderOfMagnitudeRatio < 0.01):
        print "Single Test Success"
    else:
        print "Single Test Failure"
        FullTestSuccess = False
    k = k + 1





Library_PrintFullTestSuccess.Main(FullTestSuccess)








