import Library_StockPriceDiscountDividends
import Library_TestLooper
import numpy

ArgSetExpectedResultCombos = []
#No discount args -> no discount
ArgSetExpectedResultCombos.append(
    (
        
        {
            "StockPriceCurrent": 40, 
            "Amounts": None, 
            "Times": None, 
            "ContinuousDividendYeildRate": None, 
            "ContinuousRiskFreeRate": None, 
        }
        , 
        40.0
    )
)
#Discrete case (Example 13.8 p302)
ArgSetExpectedResultCombos.append(
    (
        
        {
            "StockPriceCurrent": 40, 
            "Amounts": [0.5, 0.5],
            "Times": [2.0/12, 5.0/12], #In years
            "ContinuousRiskFreeRate": 0.09, 
        }
        , 
        39.0259
    )
)
#Discrete case remove last dividend (Modified Example 13.8 p302)
ArgSetExpectedResultCombos.append(
    (
        
        {
            "StockPriceCurrent": 40, 
            "Amounts": [0.5, 0.5],
            "Times": [2.0/12, 5.0/12], #In years
            "ContinuousRiskFreeRate": 0.09, 
            "DividendIncludeEndTime": 2.1/12,
        }
        , 
        39.5074
    )
)
#Continous case  (Example 14.1 p317):
ArgSetExpectedResultCombos.append(
    (
        
        {
            "StockPriceCurrent": 930, 
            "ContinuousDividendYeildRate": 0.08, 
            "ContinuousDividendEndTime": 2.0/12.0,
        }
        , 
        930 * numpy.exp(-1.0 * 0.08 * 2.0/12.0)
    )
)

LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_StockPriceDiscountDividends.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 0.001, #Do not allow differences
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    MaxFlatResultLength = None,
    ResultOrderMatters = True, 
    EqualityCheckFunction = None,
    PrintExtra = True,
)

































