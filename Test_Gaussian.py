"""



"""

import numpy
import scipy
import scipy.stats

#------------------------------------------------------------------------------

import Library_Gaussian
import Library_OrderOfMagnitudeRatio
import Library_PrintFullTestSuccess
import Library_OrderOfMagnitudeRatioSmallCheck

FullTestSuccess = True

#Try out some expected good cases against the built in scipy gaussian:
print "----Test multi Dim Case:----"
TestPoints = numpy.array([[0.1, 0.1],[0.5, 0.5],[0, 0.5]])
MeanPoint = numpy.array([0.0, 0.0])
CovarianceMatrix = numpy.cov(TestPoints.T) #Transpose because difference in convention
print "TestPoints       :\n", TestPoints
print "MeanPoint        :", MeanPoint
print "CovarianceMatrix :", CovarianceMatrix
ExpectedMultipleEvaluationResults = []
for Point in TestPoints:
    print "TEST_Point   :", Point
    ScipyResult = scipy.stats.multivariate_normal.pdf(Point, MeanPoint,  CovarianceMatrix, False)
    ExpectedMultipleEvaluationResults.append(ScipyResult)
    print "ScipyResult  :" , ScipyResult
    Result = Library_Gaussian.Main(Point = Point, MeanPoint = MeanPoint, CovarianceMatrix = CovarianceMatrix, PrintExtra = False)
    print "Result       :", Result    
    OrderOfMagnitudeRatio = Library_OrderOfMagnitudeRatio.Main(ScipyResult, Result)
    print "Order Of Magnitude Ratio : ", OrderOfMagnitudeRatio
    if (OrderOfMagnitudeRatio < 0.01):
        print "Test Success"
    else:
        FullTestSuccess = False
        print "Test Failure"

#Try out mulitple multidimensional points at once:
print "----Test multi Dim Case Multi Eval:----"
ExpectedMultipleEvaluationResults = scipy.stats.multivariate_normal.pdf(TestPoints, MeanPoint,  CovarianceMatrix, False)
Results = Library_Gaussian.Main(
    Point = TestPoints, 
    MeanPoint = MeanPoint, 
    CovarianceMatrix = CovarianceMatrix, 
    PrintExtra = False
    )
print ' Results', Results
print ' ExpectedMultipleEvaluationResults', ExpectedMultipleEvaluationResults

if (Library_OrderOfMagnitudeRatioSmallCheck.Main(Results, ExpectedMultipleEvaluationResults, 0.1) ):
    print 'Multi Point Evaluation Success' 
else:
    FullTestSuccess = False
    print 'Multi Point Evaluation Failure' 


print "\n----Test Single Dim Case:----"
TestPoints2 = numpy.array([[0.1], [0.2], [0.3] ])
MeanPoint2 = numpy.array([1.0])
CovarianceMatrix2 = numpy.array([[1.0]])
print "TestPoints2      :\n", TestPoints2
print "MeanPoint2       :", MeanPoint2
print "CovarianceMatrix2:", CovarianceMatrix2

for Point2 in TestPoints2:
    print "TEST_Point2  :", Point2
    ScipyResult2 = scipy.stats.multivariate_normal.pdf(Point2, MeanPoint2,  CovarianceMatrix2, False)
    print "ScipyResult2 :", ScipyResult2
    Result2 =  Library_Gaussian.Main(Point = Point2, MeanPoint = MeanPoint2, CovarianceMatrix = CovarianceMatrix2, PrintExtra = False)
    print "Result2      :", Result2 
    OrderOfMagnitudeRatio = Library_OrderOfMagnitudeRatio.Main(ScipyResult2, Result2)
    print "Order Of Magnitude Ratio : ", OrderOfMagnitudeRatio
    if (OrderOfMagnitudeRatio < 0.01):
        print "Test Success"
    else:
        FullTestSuccess = False
        print "Test Failure"



#Try out the argument handling by passing in some cooky values which should be caught:
#TODO:

Library_PrintFullTestSuccess.Main(FullTestSuccess)


"""
Leftover code:

if( PrintExtra ):
    print "Point                   \n", Point                   ,"\n"
    print "MeanPoint               \n", MeanPoint               ,"\n"
    print "CovarianceMatrix        \n", CovarianceMatrix        ,"\n"
    print "PointDelta              \n", PointDelta              ,"\n"
    print "PointDeltaTranspose     \n", PointDeltaTranspose     ,"\n"
    print "CovarianceMatrixInverse \n", CovarianceMatrixInverse ,"\n"
    print "Exponent                \n", Exponent                ,"\n"
    print "NormalizationTerm       \n", NormalizationTerm       ,"\n"
    print "Result                  \n", Result                  ,"\n"
"""












