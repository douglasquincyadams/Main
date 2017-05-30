import Library_EvaluateFunctionAtNumpyDataPoint

import Library_PrintFullTestSuccess
FullTestSuccess = True

def Function (x):

    return x

Result1 = Library_EvaluateFunctionAtNumpyDataPoint.Main(
    Function = Function, 
    DataPoint = 1
    )

if (Result1 == 1.):
    print 'Single Test Success'
else:
    print 'Single Test Failure'
    FullTestSuccess = False


Result2 = Library_EvaluateFunctionAtNumpyDataPoint.Main(
    Function = Function, 
    Coefficient = 2.5,
    DataPoint = 1,
    )

if (Result1 == 1.):
    print 'Single Test Success'
else:
    print 'Single Test Failure'
    FullTestSuccess = False

Library_PrintFullTestSuccess.Main(FullTestSuccess)
