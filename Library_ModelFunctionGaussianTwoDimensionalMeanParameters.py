"""


Description:
    Define a "Model Distribution" Definition 
       In this example we choose:
           Function to be a gaussian 
           Parameters to be choice of the mean   Mu == [x1, y1]
               (the covariance matrix is not a parameter in this case)


       Models In General:
           We need to design the function to be of two variables:
           [Point]
               An observation of real data
           [Parameters]
               There could be any number of parameters, all of which are in this list

ARGS:
   [Point]
       An observation of real data
   [Parameters]
       In this example this is a vector which describes the mean of the two dimmensional gaussian distribution


RETURNS:
    Guassian Density -> for the given point, parameters


Tests:
    Test_ModelFunctionGaussianTwoDimensionalMeanParameters

"""

import numpy
#------------------------------------------------------------------------------
import Library_Gaussian


def Main( DataPoint = None, Parameters = None ):
    ModelDistributionCovarianceMatrix = numpy.identity(2) #We assume to know this
    ModelDistributionMean = Parameters
    Result = Library_Gaussian.Main(
        DataPoint, 
        ModelDistributionMean, 
        ModelDistributionCovarianceMatrix , 
        PrintExtra = False
        )
    return Result   




















