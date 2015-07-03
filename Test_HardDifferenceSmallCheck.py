


import Library_HardDifferenceSmallCheck

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

Max2 = 20.0

Result1 = Library_HardDifferenceSmallCheck.Main(A, B, Max0)
if (Result1 == False):
    print 'Single Test Success'
else:
    print 'Single Test Failure'
    FullTestSuccess = False

Result2 = Library_HardDifferenceSmallCheck.Main(A, C, Max0)

if (Result2 == False):
    print 'Single Test Success'
else:
    print 'Single Test Failure'
    FullTestSuccess = False

Result3 = Library_HardDifferenceSmallCheck.Main(A, C, Max1)

if (Result3 == False):
    print 'Single Test Success'
else:
    print "Result3", Result3
    print 'Single Test Failure'
    FullTestSuccess = False
    
Result4 = Library_HardDifferenceSmallCheck.Main(D, E, Max1)
if (Result4 == False):
    print 'Single Test Success'
else:
    print "Result4", Result4
    print 'Single Test Failure'
    FullTestSuccess = False
    

Result5 = Library_HardDifferenceSmallCheck.Main(D, F, Max1)
if (Result5 == False):
    print 'Single Test Success'
else:
    print "Result5", Result5
    print 'Single Test Failure'
    FullTestSuccess = False

Result6 = Library_HardDifferenceSmallCheck.Main(A, B, Max2)
if (Result6 == True):
    print 'Single Test Success'
else:
    print "Result6", Result6
    print 'Single Test Failure'
    FullTestSuccess = False

Library_PrintFullTestSuccess.Main(FullTestSuccess)

















