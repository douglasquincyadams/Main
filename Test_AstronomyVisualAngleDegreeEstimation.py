
import Library_OrderOfMagnitudeRatio
import Library_AstronomyVisualAngleDegreeEstimation
import Library_PrintFullTestSuccess

FullTestSuccess = True

#TEST1
Distance = 10**20 #cm 
Rvir = Distance / 2.
ExpectedResult = 60.
Result = Library_AstronomyVisualAngleDegreeEstimation.Main(Distance = Distance, Rvir = Rvir)

if ( Library_OrderOfMagnitudeRatio.Main(Result, ExpectedResult ) < .01 ):
    print 'Single Test Success'
else:
    print 'Single Test Failure'
    print 'Result         ', Result
    print 'ExpectedResult ', ExpectedResult
    FullTestSuccess = False

Library_PrintFullTestSuccess.Main(FullTestSuccess)



