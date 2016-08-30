import Library_BlackScholesCalculateOptionPrice
import scipy
import scipy.stats


#European call no dividends (Example 13.6 -> p298)
Result = Library_BlackScholesCalculateOptionPrice.Main(
    EuropeanOrAmerican= 'European',
    CallOrPut= 'Call',
    StockPrice= 42.0,
    StrikePrice= 40.0,
    ContinuousRiskFreeRate= .10,
    Volatility= .20,
    TimeToMaturity= 0.5
    )
print Result  ,'#~=? 4.76'

#European put no dividends (Example 13.6 -> p298)
Result = Library_BlackScholesCalculateOptionPrice.Main(
    EuropeanOrAmerican= 'European',
    CallOrPut= 'Put',
    StockPrice= 42.0,
    StrikePrice= 40.0,
    ContinuousRiskFreeRate= .10,
    Volatility= .20,
    TimeToMaturity= 0.5
    )
print Result  ,'#~=? 0.81'


#European call with discrete dividends (Example 13.8 -> p302)
Result = Library_BlackScholesCalculateOptionPrice.Main(
    EuropeanOrAmerican= 'European',
    CallOrPut= 'Call',
    StockPrice= 40.0,
    StrikePrice= 40.0,
    ContinuousRiskFreeRate= .09,
    Volatility= .30,
    TimeToMaturity= 0.5,

    DividendTimes = [2./12., 5./12.],                   # (t_0, t_1, ... t_n-1)
    DividendAmounts = [0.50, 0.50],                 # (D_0, D_1, ... D_n-1)
    PrintExtra = False,
    )
print Result  ,'#~=? 3.67'


#American call with discrete dividends blacks approximation (Example 13.9 -> p304)
Result = Library_BlackScholesCalculateOptionPrice.Main(
    EuropeanOrAmerican= 'American',
    CallOrPut= 'Call',
    StockPrice= 40.0,
    StrikePrice= 40.0,
    ContinuousRiskFreeRate= .09,
    Volatility= .30,
    TimeToMaturity= 0.5,

    DividendTimes = [2./12., 5./12.],                   # (t_0, t_1, ... t_n-1)
    DividendAmounts = [0.50, 0.50],                 # (D_0, D_1, ... D_n-1)
    PrintExtra = False,
    )
print Result  ,'#~=? 3.67'



#European call with continous dividend rates (Example 14.1 p317):
Result = Library_BlackScholesCalculateOptionPrice.Main(
    EuropeanOrAmerican= 'European',
    CallOrPut= 'Call',
    StockPrice= 930.0,
    StrikePrice= 900.0,
    ContinuousRiskFreeRate= .08,
    Volatility= .20,
    TimeToMaturity= 2.0/12.0,

    ContinuousDividendYeildRate = 0.03,             # (q)
    ContinuousDividendEndTime   = 2.0/12.0,

    PrintExtra = False,
    )
print Result  ,'#~=? 51.83'



#American call with continous dividend rates (Cannot do): -> see binomial tree
#American put with continous dividend rates  (Cannot do): -> see binomial tree

































