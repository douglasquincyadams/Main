


import Library_OrderOfMagnitudeRatioSmallCheck

import Library_PrintFullTestSuccess
FullTestSuccess = True

A = [1,2,3]

B = [1.1, 2.2, 3.3]

C = [1.1, 2.2, 20.0]

D = 1.0

E = 10.0

F = 100.0

Max0 = 0.11

Max1 = 1.1

Result1 = Library_OrderOfMagnitudeRatioSmallCheck.Main(A, B, Max0)
if (Result1 == True):
    print 'Single Test Success'
else:
    print 'Single Test Failure'
    FullTestSuccess = False

Result2 = Library_OrderOfMagnitudeRatioSmallCheck.Main(A, C, Max0)

if (Result2 == False):
    print 'Single Test Success'
else:
    print 'Single Test Failure'
    FullTestSuccess = False

Result3 = Library_OrderOfMagnitudeRatioSmallCheck.Main(A, C, Max1)

if (Result3 == True):
    print 'Single Test Success'
else:
    print "Result3", Result3
    print 'Single Test Failure'
    FullTestSuccess = False
    
Result4 = Library_OrderOfMagnitudeRatioSmallCheck.Main(D, E, Max1)
if (Result4 == True):
    print 'Single Test Success'
else:
    print "Result4", Result4
    print 'Single Test Failure'
    FullTestSuccess = False
    

Result5 = Library_OrderOfMagnitudeRatioSmallCheck.Main(D, F, Max1)
if (Result5 == False):
    print 'Single Test Success'
else:
    print "Result5", Result5
    print 'Single Test Failure'
    FullTestSuccess = False

Library_PrintFullTestSuccess.Main(FullTestSuccess)

















