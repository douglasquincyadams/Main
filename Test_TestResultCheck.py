"""
NOTES: 
    Because this is part of the Library_TestLooper Dependency tree, 
    this will not make use of the Library_TestLooper

"""

import Library_TestResultCheck


Result1 = ['a', 'b', 2]
ExpectedResult1 = ['a', 'b', 2]
CorrecnessResult1 = Library_TestResultCheck.Main(
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 0.1,
    Result = Result1, 
    ExpectedResult  = ExpectedResult1, 
    )

assert(CorrecnessResult1)


Result2 = ['a', 'b', 2]
ExpectedResult2 = ['a', 'b', 2]
CorrecnessResult2 = Library_TestResultCheck.Main(
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 0.1,
    Result = Result2, 
    ExpectedResult  = ExpectedResult2, 
    )

assert(CorrecnessResult2)


Result3 = ['a', 'b', 2]
ExpectedResult3 = ['a', 'b', 3]
CorrecnessResult3 = Library_TestResultCheck.Main(
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 0.1,
    Result = Result3, 
    ExpectedResult  = ExpectedResult3, 
    )

assert(CorrecnessResult3 == False)


Result4 = ['a', 'b', 2]
ExpectedResult4 = ['a', 'b', 3]
CorrecnessResult4 = Library_TestResultCheck.Main(
    OrderOfMagnitudeRatioMax = 1.0,
    HardDifferenceMax = 2.0,
    Result = Result4, 
    ExpectedResult  = ExpectedResult4, 
    )

assert(CorrecnessResult4)


Result5 = ['a', 'b', 2]
ExpectedResult5 = ['a', 'c', 3]
CorrecnessResult5 = Library_TestResultCheck.Main(
    OrderOfMagnitudeRatioMax = 1.0,
    HardDifferenceMax = 2.0,
    Result = Result5, 
    ExpectedResult  = ExpectedResult5, 
    )

assert(CorrecnessResult5 == False)

Result6 = ['a', 'b', 2]
ExpectedResult6 = ['a', 'c', 3]
CorrecnessResult6 = Library_TestResultCheck.Main(
    Result = Result6, 
    ExpectedResult  = ExpectedResult6, 
    )

assert(CorrecnessResult6 == False)

Result7 = ['a', {'b' : 5}, 2]
ExpectedResult7 = ['a', {'b' : 5}, 3]
CorrecnessResult7 = Library_TestResultCheck.Main(
    Result = Result7, 
    ExpectedResult  = ExpectedResult7, 
    )

assert(CorrecnessResult7 == True)


Result8 = ['a', {'b' : ['a','b']}, 2]
ExpectedResult8 = ['a', {'b' : ['a','b']}, 3]
CorrecnessResult8 = Library_TestResultCheck.Main(
    Result = Result8, 
    ExpectedResult  = ExpectedResult8, 
    )

assert(CorrecnessResult8 == True)


Result9 = Exception('Some error message')
ExpectedResult9 = Exception('Some different error message')
CorrecnessResult9 = Library_TestResultCheck.Main(
    Result = Result9, 
    ExpectedResult  = ExpectedResult9, 
    )

assert(CorrecnessResult9 == True)


Result10 = [ (12,13,2),  (12,13,1) ]
ExpectedResult10 = Exception('Some different error message')
CorrecnessResult10 = Library_TestResultCheck.Main(
    Result = Result10, 
    ExpectedResult  = ExpectedResult10, 
    )

assert(CorrecnessResult10 == False)




#Result9 = [ (12,13,2),  (12,13,1) ]

print 'Full Test Success' #Code cannot get here if the asserts fail









