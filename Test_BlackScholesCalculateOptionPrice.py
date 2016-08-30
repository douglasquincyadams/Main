import Library_BlackScholesCalculateOptionPrice
import Library_TestLooper

ArgSetExpectedResultCombos = []

#European call no dividends (Example 13.6 -> p298)
ArgSetExpectedResultCombos.append(
    (
        
        {
            "EuropeanOrAmerican": 'European', 
            "CallOrPut": 'Call', 
            "StockPrice": 42.0,
            "StrikePrice": 40.0,
            "ContinuousRiskFreeRate": .10,
            "Volatility": .20,
            "TimeToMaturity": 0.5
        }
        , 
        4.76
    )
)

#European put no dividends (Example 13.6 -> p298)
ArgSetExpectedResultCombos.append(
    (
        
        {
            "EuropeanOrAmerican": 'European', 
            "CallOrPut": 'Put', 
            "StockPrice": 42.0,
            "StrikePrice": 40.0,
            "ContinuousRiskFreeRate": .10,
            "Volatility": .20,
            "TimeToMaturity": 0.5
        }
        , 
        0.81
    )
)


#European call with discrete dividends (Example 13.8 -> p302)
ArgSetExpectedResultCombos.append(
    (
        
        {
            "EuropeanOrAmerican": 'European', 
            "CallOrPut": 'Call', 
            "StockPrice": 40.0,
            "StrikePrice": 40.0,
            "ContinuousRiskFreeRate": .09,
            "Volatility": .30,
            "TimeToMaturity": 0.5,


            "DividendTimes": [2./12., 5./12.],
            "DividendAmounts": [0.50, 0.50], 
        }
        , 
        3.67
    )
)

#American call with discrete dividends blacks approximation (Example 13.9 -> p304)
ArgSetExpectedResultCombos.append(
    (
        
        {
            "EuropeanOrAmerican": 'American', 
            "CallOrPut": 'Call', 
            "StockPrice": 40.0,
            "StrikePrice": 40.0,
            "ContinuousRiskFreeRate": .09,
            "Volatility": .30,
            "TimeToMaturity": 0.5,


            "DividendTimes": [2./12., 5./12.],
            "DividendAmounts": [0.50, 0.50], 
        }
        , 
        3.67 #Which is max (3.67, 3.52)   3.52 = price of a different european option expiring BEFORE dividend
    )
)

#European call with continous dividend rates (Example 14.1 p317):
ArgSetExpectedResultCombos.append(
    (
        
        {
            "EuropeanOrAmerican": 'European', 
            "CallOrPut": 'Call', 
            "StockPrice": 930.0,
            "StrikePrice": 900.0,
            "ContinuousRiskFreeRate": .08,
            "Volatility": .20,
            "TimeToMaturity": 2.0/12.0,


            "ContinuousDividendYeildRate": 0.03, # (q)
            "ContinuousDividendEndTime": 2.0/12.0,
        }
        , 
        51.83
    )
)

#American call with continous dividend rates (Cannot do): -> see binomial tree
#American put with continous dividend rates  (Cannot do): -> see binomial tree




LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_BlackScholesCalculateOptionPrice.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 0.01,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    MaxFlatResultLength = None,
    ResultOrderMatters = True, 
    EqualityCheckFunction = None,
    PrintExtra = True,
)

































