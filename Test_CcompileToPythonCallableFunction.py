import Library_CcompileToPythonCallableFunction
import Library_TestLooper

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "CfunctionHeader": None, 
            "CfunctionSource": None
        }
        , 
        []
    )
)



LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_CcompileToPythonCallableFunction.Main,
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

































