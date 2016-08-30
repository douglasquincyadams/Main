"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Calculates the options price given the other 
    parameters in the black scholes model
    
    For a rigorous investigation of black scholes model derivation: 
        Study Ito Calculus
        Specifically understand derivation of Ito's lemma
        Perform arbitrary calculus with random variables / regular variables

    For a cookbook USING black scholes model without understanding how to derive it
        See John C Hull's Options Futures and other Derivatives book

    This libary is intented as a the latter. A cookbook:
        Recipies are followed without understanding origins or derivations
        Recipies are directly taken from John C Hull cookbook. 

    Example John C Hull pricing problems are tested / checked
    

ARGS:
    CheckArguments
        Type:
            python boolean
        Description:
            if true, checks the arguments with conditions written in the function
            if false, ignores those conditions
    PrintExtra
        Type:
            python integer
        Description:
            if greater than 0, prints addional information about the function
            if 0, function is expected to print nothing to console
            Additional Notes:
                The greater the number, the more output the function will print
                Most functions only use 0 or 1, but some can print more depending on the number
    EuropeanOrAmerican
        Type:
            <type 'NoneType'>
        Description:
    CallOrPut
        Type:
            <type 'NoneType'>
        Description:
    StockPrice
        Type:
            <type 'NoneType'>
        Description:
    Strike
        Type:
            <type 'NoneType'>
        Description:
    ContinuousRiskFreeRate
        Type:
            <type 'NoneType'>
        Description:
    Volatility
        Type:
            <type 'NoneType'>
        Description:
    TimeToMaturity
        Type:
            <type 'NoneType'>
        Description:
RETURNS:
    Result
        Type:
        Description:
"""

import scipy
import datetime
import numpy
from scipy.stats import norm
#-------------------------------------------------------------------------------
import Library_StockPriceDiscountDividends
def Main(
    EuropeanOrAmerican= None,               # (american or european option type)
    CallOrPut= None,                        # (c or p)
    StockPrice= None,                       # (S_0)
    StrikePrice= None,                      # (K)
    ContinuousRiskFreeRate= None,           # (r)
    Volatility= None,                       # (sigma)
    TimeToMaturity= None,                   # (T)

    DividendTimes = None,                   # (t_0, t_1, ... t_n-1)
    DividendAmounts = None,                 # (D_0, D_1, ... D_n-1)
    ContinuousDividendYeildRate = None,     # (q)
    ContinuousDividendEndTime = None,

    CheckArguments = True,
    PrintExtra = False,
    ):

    Result = None

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if not (CallOrPut in ['Call', 'Put']):
            CallOrPutStrCast = None
            try:
                CallOrPutStrCast = str(CallOrPut)
            except:
                CallOrPutStrCast = 'Something so poorly chosen it couldnt even be cast to string'
            ArgumentErrorMessage += 'You tried `CallOrPut` == ' + CallOrPutStrCast + '\n'

        if not (EuropeanOrAmerican in ['European', 'American']):
            EuropeanOrAmericanStrCast = None
            try:
                EuropeanOrAmericanStrCast = str(EuropeanOrAmerican)
            except:
                EuropeanOrAmericanStrCast = 'Something so poorly chosen it couldnt even be cast to string'
            ArgumentErrorMessage += 'You tried `EuropeanOrAmerican` == ' + EuropeanOrAmericanStrCast + '\n'

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    StockPriceDividendDiscounted = Library_StockPriceDiscountDividends.Main(
        StockPriceCurrent                   = StockPrice,
        Amounts                             = DividendAmounts,
        Times                               = DividendTimes, #In trade years (same unit as TimeToMaturity )
        ContinuousRiskFreeRate              = ContinuousRiskFreeRate,
        ContinuousDividendYeildRate         = ContinuousDividendYeildRate, 
        ContinuousDividendEndTime           = ContinuousDividendEndTime,
        )
    if(PrintExtra): print 'StockPriceDividendDiscounted', StockPriceDividendDiscounted

    DividendsExist = (StockPriceDividendDiscounted != StockPrice)

    #d1 = (ln(s0/K) + (r + sigma**2 / 2)T)   /  (sigma(sqrt(T)))
    #d2 = (ln(s0/K) + (r - sigma**2 / 2)T)   /  (sigma(sqrt(T))) = d1 - sigma(sqrt(T))
    d1 = ( numpy.log(StockPriceDividendDiscounted / StrikePrice ) + (ContinuousRiskFreeRate + (Volatility**2)/2 ) * TimeToMaturity ) / (Volatility * numpy.sqrt(TimeToMaturity) )
    if(PrintExtra): print 'd1', d1

    d2 = ( numpy.log(StockPriceDividendDiscounted / StrikePrice ) + (ContinuousRiskFreeRate - (Volatility**2)/2 ) * TimeToMaturity ) / (Volatility * numpy.sqrt(TimeToMaturity) )
    if(PrintExtra): print 'd2', d2

    #d2minusd1 = d1 - (Volatility * numpy.sqrt(TimeToMaturity) )
    #if(PrintExtra): print 'd2minusd1', d2minusd1

    #N(x) = scipy.stats.norm.cdf(x)
    if CallOrPut == 'Call' :
        #c = s0 N(d1) - ( K e^(-rT) )  N(d2)
        EuropeanCallPrice = StockPriceDividendDiscounted * scipy.stats.norm.cdf(d1) - StrikePrice * numpy.exp( (-1.0) * ContinuousRiskFreeRate * TimeToMaturity ) * scipy.stats.norm.cdf(d2)
    elif CallOrPut == 'Put' :
        #p = ( K e^(-rT) )  N(-d2) - s0 N( -d1)
        EuropeanPutPrice = StrikePrice * numpy.exp( (-1.0) * ContinuousRiskFreeRate * TimeToMaturity ) * scipy.stats.norm.cdf((-1.0) *d2) - StockPriceDividendDiscounted * scipy.stats.norm.cdf( (-1.0) * d1) 

    if (EuropeanOrAmerican == 'European'):
        if CallOrPut == 'Call' :
            Result = EuropeanCallPrice
        elif CallOrPut == 'Put' :
            Result = EuropeanPutPrice
    elif (EuropeanOrAmerican == 'American'):
        if (CallOrPut == 'Call'):
            EuropeanOptionPrice = EuropeanCallPrice
        elif (CallOrPut == 'Put'):
            EuropeanOptionPrice = EuropeanPutPrice

        StockPriceAllButLastDividendDiscounted = None
        if DividendsExist:
            if (ContinuousDividendYeildRate is not None or ContinuousDividendEndTime is not None):
                raise Exception('Cannot do american continuous dividend paying option with black scholes')
            if (len(DividendAmounts) != len(DividendTimes) or len(DividendAmounts) < 1 or len(DividendTimes) < 1):
                raise Exception ('DividendAmounts and DividendTimes lengths bad')

            StockPriceAllButLastDividendDiscounted = Library_StockPriceDiscountDividends.Main(
                StockPriceCurrent           = StockPrice,
                Amounts                     = DividendAmounts[0:-1],
                Times                       = DividendTimes[0:-1], #In trade years (same unit as TimeToMaturity )
                ContinuousRiskFreeRate      = ContinuousRiskFreeRate,
                ContinuousDividendYeildRate = ContinuousDividendYeildRate, 
                ContinuousDividendEndTime   = ContinuousDividendEndTime,
                )
            if(PrintExtra): print 'StockPriceAllButLastDividendDiscounted', StockPriceAllButLastDividendDiscounted

            EuropeanOptionPriceExLastDividend = Main(
                EuropeanOrAmerican      = 'European',                               # (american or european)
                CallOrPut               = CallOrPut,                                # (c or p)
                StockPrice              = StockPriceAllButLastDividendDiscounted,   # (S_0)
                StrikePrice             = StrikePrice,                              # (K)
                ContinuousRiskFreeRate  = ContinuousRiskFreeRate,                   # (r)
                Volatility              = Volatility,                               # (sigma)
                TimeToMaturity          = DividendTimes[-1],                        # (T)
                ContinuousDividendEndTime   = ContinuousDividendEndTime,
                )
            if(PrintExtra):
                print 'EuropeanOptionPrice', EuropeanOptionPrice
                print 'EuropeanOptionPriceExLastDividend', EuropeanOptionPriceExLastDividend
            Result = numpy.maximum( EuropeanOptionPrice , EuropeanOptionPriceExLastDividend ) 

        else:
            Result = EuropeanOptionPrice

    return Result 












