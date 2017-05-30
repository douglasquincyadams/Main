
#------------------------------------------------------------------------------
import Library_GammaIncompleteRegularized
import Library_ChiSquaredDeltaLogLikelihoodToConfidenceLevel


import Library_OrderOfMagnitudeRatio
import Library_PrintFullTestSuccess


FullTestSuccess = True

NumDimensions = 2
Likelihood = 5.99

Result1 = Library_GammaIncompleteRegularized.Main(NumDimensions/2.0, Likelihood/2.0)
ExpectedResult1 = 0.95
Result1_OrderOfMagnitudeRatio = Library_OrderOfMagnitudeRatio.Main(Result1, ExpectedResult1)
if (Result1_OrderOfMagnitudeRatio < 0.01):
    print "Single Test Success"
else:
    print "Single Test Failure"
    FullTestSuccess = False

Result2 = Library_ChiSquaredDeltaLogLikelihoodToConfidenceLevel.Main(NumDimensions, Likelihood)
ExpectedResult2 = 0.95
Result2_OrderOfMagnitudeRatio = Library_OrderOfMagnitudeRatio.Main(Result2, ExpectedResult2)
if (Result2_OrderOfMagnitudeRatio < 0.01):
    print "Single Test Success"
else:
    print "Single Test Failure"
    print '   Result2', Result2
    print '   ExpectedResult2', ExpectedResult2
    print '   Result2_OrderOfMagnitudeRatio', Result2_OrderOfMagnitudeRatio

    FullTestSuccess = False


Library_PrintFullTestSuccess.Main(FullTestSuccess)


