import Library_BinomialTreeOptionPrice
import Library_TestLooper

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "IntervalCount": None,
            "EuropeanOrAmerican": None, 
            "CallOrPut": None, 
            "StockPrice": None, 
            "StrikePrice": None, 
            "ContinuousRiskFreeRate": None, 
            "ContinuousAssetYeildRate": None, 
            "Volatility": None, 
            "TimeToMaturity": None, 

            "DividendTimes": None, 
            "DividendAmounts": None, 

        }
        , 
        Exception('No Args')
    )
)

#(Example 17.1, Figure 17.3 p394 6th edition)
for IntervalCount, ExpectedResult in zip([5,30,50,100, 500], [4.49, 4.263, 4.272, 4.278, 4.283]):
    ArgSetExpectedResultCombos.append(
        (
            
            {
                "IntervalCount": IntervalCount,
                "EuropeanOrAmerican": 'American', 
                "CallOrPut":  'Put', 
                "StockPrice": 50, 
                "StrikePrice": 50, 
                "ContinuousRiskFreeRate": .10, 
                "ContinuousAssetYeildRate": None, 
                "Volatility":  .40, 
                "TimeToMaturity": 5.0/12.0, 

                "DividendTimes": None, 
                "DividendAmounts": None, 

            }
            , 
            ExpectedResult
        )
    )

##(Example 17.3, Figure 17.5,  p399 6th edition)
for IntervalCount, ExpectedResult in zip([4,50,100], [19.16, 20.18, 20.22]):
    ArgSetExpectedResultCombos.append(
        (
            
            {
                "IntervalCount": IntervalCount,
                "EuropeanOrAmerican": 'American', 
                "CallOrPut":  'Call', 
                "StockPrice": 300, 
                "StrikePrice": 300, 
                "ContinuousRiskFreeRate": .08,
                "ContinuousAssetYeildRate": .08,
                "Volatility":  .30,
                "TimeToMaturity": 4.0/12.0,

                "DividendTimes": None, 
                "DividendAmounts": None, 

            }
            , 
            ExpectedResult
        )
    )
##(Example 17.4, Figure 17.6,  p400 6th edition)
for IntervalCount, ExpectedResult in zip([4, 50,  100], [0.0710, 0.0738, 0.0738]):
    ArgSetExpectedResultCombos.append(
        (
            
            {
                "IntervalCount": IntervalCount,
                "EuropeanOrAmerican": 'American', 
                "CallOrPut":  'Put', 
                "StockPrice":  1.6100,
                "StrikePrice": 1.6000,
                "ContinuousRiskFreeRate": .08,
                "ContinuousAssetYeildRate": .09,
                "Volatility":  .12,
                "TimeToMaturity": 1.0,

                "DividendTimes": None, 
                "DividendAmounts": None, 

            }
            , 
            ExpectedResult
        )
    )
#(Example 17.5, Figure 17.9,  p404 6th edition)
for IntervalCount, ExpectedResult in zip([5, 50,  100], [4.44, 4.202, 4.212]):
    ArgSetExpectedResultCombos.append(
        (
            
            {
                "IntervalCount": IntervalCount,
                "EuropeanOrAmerican": 'American', 
                "CallOrPut":  'Put', 
                "StockPrice":  52.00,
                "StrikePrice": 50.00,
                "ContinuousRiskFreeRate": .10,
                "ContinuousAssetYeildRate": None,
                "Volatility":  .40,
                "TimeToMaturity":5.0/12.0,

                "DividendTimes": [3.5/12.0],
                "DividendAmounts": [2.06],

            }
            , 
            ExpectedResult
        )
    )

LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_BinomialTreeOptionPrice.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.001,
    HardDifferenceMax = 0.01,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    MaxFlatResultLength = None,
    ResultOrderMatters = True, 
    EqualityCheckFunction = None,
    PrintExtra = True,
)

































