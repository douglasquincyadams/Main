"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Calculates the current value of the sum of different amounts
    If no additional variables are specified, 
        Each amount is discounted by it's time
        Each discount rate is the continuous risk free rate
        The value is equal to the sum of each of the discounted amounts
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
    StockPrice
        Type:
            <type 'float'>
        Description:
            the value of the stock - last traded price at current time
    Amounts
        Type:
            <type 'list'>
        Description:
            list of float values
    Times
        Type:
            <type 'list'>
        Description:
            list of float values
    ContinuousDividendYeildRate
        Type:
            <type 'float'>
        Description:
    ContinuousRiskFreeRate
        Type:
            <type 'float'>
        Description:
    CumulativeDefaultProbabilityFunction
        Type:
            <type 'function'>
        Description:
            CumulativeDefaultProbabilityFunction(time) = Probability of default before that time

RETURNS:
    Result
        Type:
        Description:
"""
import numpy
import Type_Number
import Type_Iterable
import Library_IterableIsSorted
def Main(
    StockPriceCurrent = None,

    ContinuousDividendYeildRate= None,
    ContinuousDividendEndTime = None,

    Amounts= None,
    Times= None, #Each in years
    ContinuousRiskFreeRate= None,               #TODO -> if this is a function(time) i.e. variable interest rate -> use it

    CumulativeDefaultProbabilityFunction= None, #TODO -> Use this

    DividendIncludeEndTime = None,

    CheckArguments = True,
    PrintExtra = False,
    ):

    Result = None


    DiscountArgs = [ContinuousDividendYeildRate, ContinuousDividendEndTime, Amounts, Times, ContinuousRiskFreeRate]
    AllDiscountArgsNone = all( i is None for i in DiscountArgs )
    #print 'AllDiscountArgsNone', AllDiscountArgsNone

    if (CheckArguments):
        ArgumentErrorMessage = ""

        #all( type(i) is int for i in lst )
        #if not AllDiscountArgsNone:
        #    AmountsTimesYeildRateNoneMessage = 'Need either [`Amounts`, `Times`, `ContinuousRiskFreeRate`] OR [`ContinuousDividendYeildRate`, `ContinuousDividendEndTime`]\n'
        #    if (Amounts is None or Times is None or ContinuousRiskFreeRate is None) and (ContinuousDividendYeildRate is None or ContinuousDividendEndTime is None):
        #        ArgumentErrorMessage += AmountsTimesYeildRateNoneMessage

        if not (None in DiscountArgs ):
            ArgumentErrorMessage += '(All possible args have values -> desired discount technique is ambiguous)\n'
    
        if StockPriceCurrent is None:
            ArgumentErrorMessage += '`StockPriceCurrent` must not be null\n'
        if not Type_Number.Main(StockPriceCurrent):
            ArgumentErrorMessage += '`StockPriceCurrent` must be a number\n'

        #Continuous discount args check:
        #if ContinuousDividendYeildRate is not None:
        #    if not Type_Function.Main(ContinuousDividendYeildRate):
        #        ArgumentErrorMessage += '`ContinuousDividendYeildRate` must be either None or a function which returns a number\n'

        ArgNameValuesNullOrNumber = [
            ('ContinuousDividendYeildRate', ContinuousDividendYeildRate),
            ('ContinuousDividendEndTime', ContinuousDividendEndTime),
            ('ContinuousRiskFreeRate', ContinuousRiskFreeRate),
            ]
        for ArgNameValue in ArgNameValuesNullOrNumber:
            ArgValue = ArgNameValue[1]
            if ArgValue is not None:
                if not Type_Number.Main(ArgValue):
                    ArgumentErrorMessage += '`' + ArgNameValue[0] + '` must either be None or a number\n'

        #Discrete discount args check:
        ArgNameValuesNullOrNumberList = [
            ('Amounts', Amounts),
            ('Times', Times),
            ]
        for ArgNameValue in ArgNameValuesNullOrNumberList:
            ArgValue = ArgNameValue[1]
            if ArgValue is not None:
                if not Type_Iterable.Main(ArgValue):
                    ArgumentErrorMessage += '`' +ArgNameValue[0] + '` must either be None or a iterable list of numbers\n'
                else:
                    if not len(ArgValue) > 0:
                        ArgumentErrorMessage += '`' +ArgNameValue[0] + '` must not be an emtpy list\n'
                    for Item in ArgValue:
                        if not Type_Number.Main(Item):
                            ArgumentErrorMessage += '`' +ArgNameValue[0] + '` must be an iterable list of numbers\n'
                            ArgumentErrorMessage += '(`'+ str(Item) + '` found in `'+ArgNameValue[0]+'` ) \n '
 
        if Times is not None:
            if not Library_IterableIsSorted.Main(Times) :
                ArgumentErrorMessage += 'Arg `Times` must be sorted values (last time is highest number)\n'


        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception('\n' + ArgumentErrorMessage)


    LastDividendTime = None
    if Times is not None:
        LastDividendTime = Times[-1]
    else:
        LastDividendTime = 9999.9 #1000 years should be large enough for options not to exist

    if (DividendIncludeEndTime is None):
        DividendIncludeEndTime = LastDividendTime


    if (AllDiscountArgsNone):
        DividendsCurrentValue = 0.0
    elif (Amounts is not None and Times is not None and ContinuousRiskFreeRate is not None): 
        DividendsCurrentValue = 0.0
        for Amount, Time in zip( Amounts, Times ):
            if (Time <= DividendIncludeEndTime):
                SingleDividendCurrentValue = Amount * numpy.exp( (-1.0) * ContinuousRiskFreeRate*Time )
                DividendsCurrentValue += SingleDividendCurrentValue
            #else:
            #    print 'DIVIDEND OMITTED'
            #    print 'Amount:', Amount, 'Time:', Time
            #    print 'DividendIncludeEndTime', DividendIncludeEndTime

    elif (ContinuousDividendYeildRate is not None and ContinuousDividendEndTime is not None):
        #print 'StockPriceCurrent', StockPriceCurrent
        #print 'ContinuousDividendYeildRate', ContinuousDividendYeildRate
        #print 'ContinuousDividendEndTime', ContinuousDividendEndTime
        DividendsCurrentValue = StockPriceCurrent - StockPriceCurrent * numpy.exp( (-1.0) * ContinuousDividendYeildRate*ContinuousDividendEndTime )
    else:
        DividendsCurrentValue = 0
        #print '    DiscountArgs = [ContinuousDividendYeildRate, ContinuousDividendEndTime, Amounts, Times, ContinuousRiskFreeRate]:'
        #print DiscountArgs
        #raise Exception('unkown error')

    Result = StockPriceCurrent - DividendsCurrentValue
    return Result 






