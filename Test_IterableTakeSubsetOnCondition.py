import Library_IterableTakeSubsetOnCondition
import Library_TestLooper

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "Iterable": None, 
            "ConditionFunction": None
        }
        , 
        []
    )
)



LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_IterableTakeSubsetOnCondition.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    MaxFlatResultLength = None,
    ResultOrderMatters = True, 
    EqualityCheckFunction = None,
    PrintExtra = True,
)

































