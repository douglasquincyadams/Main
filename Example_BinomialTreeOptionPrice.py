import Library_BinomialTreeOptionPrice
import Library_BlackScholesCalculateOptionPrice


print '\n\n#(Example 17.5, Figure 17.9,  p404 6th edition)'
for IntervalCount in [5]:
    Result = Library_BinomialTreeOptionPrice.Main(
        IntervalCount = IntervalCount,
        EuropeanOrAmerican= 'American',
        CallOrPut= 'Put',
        StockPrice= 52.00,
        StrikePrice= 50.00,
        ContinuousRiskFreeRate= .10,
        ContinuousAssetYeildRate= None,
        Volatility= .40,
        TimeToMaturity= 5.0/12.0,

        DividendTimes= [3.5/12.0],
        DividendAmounts= [2.06],

        PrintExtra = True,
        PrintTree = False,
        )
    print 'IntervalCount', IntervalCount, '=>', Result







































