


import numpy

import Library_IterableSelect

import Library_TestLooper

def NumbersGreaterThanFive(Num):
    if (Num > 5):
        return True
    return False

ListObject = [0,1,2,3,4,5,6,7,8,9]
ListObjectSubsetCriterionTrue = Library_IterableSelect.Main(
    Iterable = ListObject,
    ConditionFunction = NumbersGreaterThanFive,
    )
print 'ListObjectSubsetCriterionTrue', ListObjectSubsetCriterionTrue

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
            "Iterable"              : range(10) , 
            "ConditionFunction"     :   NumbersGreaterThanFive,
        }
        , 
        [6,7,8,9] 
    )
)


ArgSetExpectedResultCombos.append(
    (
        {
            "Iterable"              : numpy.array(range(10)) , 
            "ConditionFunction"     : NumbersGreaterThanFive  ,
        }
        , 
        numpy.array( [ 6,7,8,9 ] )
    )
)





LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_IterableSelect.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = None,
    HardDifferenceMax = 0.001,
    PrintExtra = False,
)

