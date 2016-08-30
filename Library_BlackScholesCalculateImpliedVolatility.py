"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Calculates the implied volitility given the other 
    parameters in the black scholes model
    for a discussion of black scholes model derivation -> 
        See Ito Calculus
        without understanding Ito's lemma
        and how to perform calculus with random variables
        the derivation makes no sense
    For a printed cookbook for how to USE black scholes model without caring where it came from
        See John C Hull's Options Futures and other Derivatives book
    This libary is intented as a cookbook -> following a recipe without understanding it's origins
    Example implied vol problems are tested using the John hull book
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
            <type 'str'>
        Description:
            'European' or 'American'
    OptionPrice
        Type:
            <type 'float'>
        Description:
            The price of the option  
            (c or p)
    CallOrPut
        Type:
            <type 'str'>
        Description:
            'Call' or 'Put'
    StockPrice
        Type:
            <type 'float'>
        Description:
            Underlying stock price at time t = 0  
            (S_0)
    Strike
        Type:
            <type 'float'>
        Description:
            The price with which the executor can choose to buy or sell
            (K)
    ContinuousRiskFreeRate
        Type:
            <type 'float'>
        Description:
            The risk free rate of interest accumulated on money i.e. T-Bills
            (r)
    TimeToMaturity
        Type:
            <type 'float'>
        Description:
            Time is usally measured as the number of days left in the lifetime 
            of the option divided by the number of trading days in a year
            (T)
RETURNS:
    Result
        Type:
        Description:
"""
import Library_BlackScholesCalculateOptionPrice
import Library_ZeroFindNewtonRaphsonOneDimension

def Main(                           #Tabulated Notes refer to John C Hull Book
    EuropeanOrAmerican = None, 
    OptionPrice= None,
    CallOrPut= None,                # (c or p)
    StockPrice= None,               # (S_0)
    StrikePrice= None,              # (K)
    ContinuousRiskFreeRate= None,   # (r)
    TimeToMaturity= None,           # (T)
    CheckArguments = True,
    PrintExtra = False,
    ):

    Result = None

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    def RaphsonableBlackScholesPriceMinusRealPrice(Volatility):
        Price = Library_BlackScholesCalculateOptionPrice.Main(
            EuropeanOrAmerican= EuropeanOrAmerican,
            CallOrPut= CallOrPut,
            StockPrice= StockPrice,
            StrikePrice= StrikePrice,
            ContinuousRiskFreeRate= ContinuousRiskFreeRate,
            Volatility= Volatility,
            TimeToMaturity= TimeToMaturity
            )
        return Price - OptionPrice

    ImpliedVolatility = Library_ZeroFindNewtonRaphsonOneDimension.Main(
        Function= RaphsonableBlackScholesPriceMinusRealPrice,
        StartPoint= 0.5,
        MaximumError=  0.0001
        )
    Result = ImpliedVolatility
    return Result 















