"""
There likely exists a better name for this function
"""


import datetime

#------------------------------------------------------------------------------
import Library_ChiSquaredConfidenceLevelToDeltaLogLikelihoodMaximum
import Library_OrderOfMagnitudeRatio
import Library_PrintFullTestSuccess


FullTestSuccess = True

NumDimensions = 2
ConfidenceLevel = 0.95
NumIterations = 1000 

#Do some time testing:
start = datetime.datetime.utcnow()

k = 0
while (k < NumIterations):
    Result = Library_ChiSquaredConfidenceLevelToDeltaLogLikelihoodMaximum.Main(NumDimensions, ConfidenceLevel)
    ExpectedResult = 5.99

    #print Result
    #print ExpectedResult

    #Also check the accuracy of the results 
    #   (this check should have minimal impact on time):
    OrderOfMagnitudeRatio = Library_OrderOfMagnitudeRatio.Main(Result, ExpectedResult)
    
    if (OrderOfMagnitudeRatio < 0.01):
        pass
    else:
        print "Single Test Failure"
        print "    We know that for NumDimm = 2  -> this should get us something close to 5.99"
        FullTestSuccess = False


    k = k + 1

end = datetime.datetime.utcnow()

timetaken =  end - start


Library_PrintFullTestSuccess.Main(FullTestSuccess)


print timetaken.total_seconds() ,  " seconds taken for ", NumIterations, " iterations."











"""
Leverover code && Notes from the library:

#import Library_GammaIncompleteRegularizedLambdaGenerateFixDimension
#   Set X2CDF(ChiSquaredDomainChoice, K) == Confidence Level
#   Can make the computer solve for `Xvector` by using the Scipy Optimize function:


#FIND MIN (  ( X2CDF(ChiSquaredDomainChoice, NumDim) - ConfidenceLevel)^2   )
    #Extract the first element because we know this is only 1 parameter

#Look for Contour Edge
#
#   Define && Denote some variables as mathematical terms: 
#       X2CDF               = "Chi-Squared Cumulative Density Function" == "Regularlized Gamma Function"
#       Xvector             = "Parameters in vector form"
#       NumDimensions       = "Number of degrees of freedom in the Chi-Squared distribution" -> this should be the same as the number of the parameters
#       ConfidenceLevel     = "Confidence Level"
#
"""














