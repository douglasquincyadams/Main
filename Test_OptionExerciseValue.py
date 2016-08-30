import Library_OptionExerciseValue
import Library_TestLooper

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "CallOrPut":  'Call', 
            "StockPrice": 120.0, 
            "StrikePrice": 100.0
        }
        , 
        20.0
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "CallOrPut":  'Call', 
            "StockPrice": 100.0, 
            "StrikePrice": 120.0
        }
        , 
        0.0
    )
)
ArgSetExpectedResultCombos.append(
    (
        
        {
            "CallOrPut":  'Put', 
            "StockPrice": 120.0, 
            "StrikePrice": 100.0
        }
        , 
        0.0
    )
)
ArgSetExpectedResultCombos.append(
    (
        
        {
            "CallOrPut":  'Put', 
            "StockPrice": 100.0, 
            "StrikePrice": 120.0
        }
        , 
        20.0
    )
)


LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_OptionExerciseValue.Main,
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

































