import Library_ArraySwapTwoElements
import Library_TestLooper

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
        "Array": ['a','b', 'c', 'd'],
        "Index1": 1,
        "Index2": 2,
        }
        , 
        ['a', 'c', 'b', 'd']
    )
)



LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_ArraySwapTwoElements.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    MaxFlatResultLength = None,
    ResultOrderMatters = True, 
    PrintExtra = True,
)
































