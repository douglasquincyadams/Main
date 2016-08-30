import Library_BlackScholesCalculateImpliedVolatility
import Library_TestLooper

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "OptionPrice": None, 
            "CallOrPut": None, 
            "StockPrice": None, 
            "Strike": None, 
            "ContinuousRiskFreeRate": None, 
            "TimeToMaturity": None
        }
        , 
        []
    )
)



LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_BlackScholesCalculateImpliedVolatility.Main,
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

































