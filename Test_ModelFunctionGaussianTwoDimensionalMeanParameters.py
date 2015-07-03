
import numpy
#------------------------------------------------------------------------------
import Library_ModelFunctionGaussianTwoDimensionalMeanParameters
import Library_OrderOfMagnitudeRatio
import Library_PrintFullTestSuccess
import Library_Gaussian

FullTestSuccess = True

Point = numpy.array([.1,.1])#This is a two dimensional cartesian coordinate
Parameters =  numpy.array([.2,.2])#This is a gaussian mean


Result = Library_ModelFunctionGaussianTwoDimensionalMeanParameters.Main(\
    DataPoint = Point ,\
    Parameters = Parameters)


AssumedCovarianceMatrix = numpy.identity(2)
ExpectedResult = Library_Gaussian.Main(\
    Point = Point,\
    MeanPoint = Parameters, \
    CovarianceMatrix = AssumedCovarianceMatrix)


OrderOfMagnitudeRatio = Library_OrderOfMagnitudeRatio.Main(ExpectedResult, Result)

if ( OrderOfMagnitudeRatio< 0.01):
    print "Single Test Success"
else:
    print "Single Test Success"



Library_PrintFullTestSuccess.Main(FullTestSuccess)


