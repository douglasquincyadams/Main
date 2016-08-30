import Library_BlackScholesCalculateImpliedVolatility
Result = Library_BlackScholesCalculateImpliedVolatility.Main(
    EuropeanOrAmerican      = 'European',
    OptionPrice             = 1.875,
    CallOrPut               = 'Call',
    StockPrice              = 21.0,
    StrikePrice             = 20.0,
    ContinuousRiskFreeRate  = 0.1,
    TimeToMaturity          = 0.25
    )
print Result  #0.235

















































