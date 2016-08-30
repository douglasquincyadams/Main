"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Calculates the current value of an option,
        using a binomial tree
    Procedures are followed in John C Hull options pricing book. 

    (Chapter 17 John C Hull)

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
    StrikePrice
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
    DividendTimes
        Type:
            <type 'NoneType'>
        Description:
    DividendAmounts
        Type:
            <type 'NoneType'>
        Description:
    ContinuousAssetYeildRate
        Type:
            <type 'NoneType'>
        Description:
    ContinuousDividendEndTime
        Type:
            <type 'NoneType'>
        Description:
RETURNS:
    Result
        Type:
        Description:
"""
import numpy
import pprint
import Library_OptionExerciseValue
import Library_StockPriceDiscountDividends
def Main(
    #REQUIRED:
    IntervalCount = None,
    EuropeanOrAmerican= None,
    CallOrPut= None,
    StockPrice= None,
    StrikePrice= None,
    ContinuousRiskFreeRate= None,
    ContinuousAssetYeildRate= None,

    Volatility= None,
    TimeToMaturity= None,

    #OPTIONAL
    DividendTimes= None,
    DividendAmounts= None,

    #OR
    #ContinuousDividendYeild = None,
    #ContinuousDividendEndTime= None,

    CheckArguments = True,
    PrintExtra = False,
    PrintTree = False,
    ):

    Result = None

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)


    StockPrice = Library_StockPriceDiscountDividends.Main(
        StockPriceCurrent = StockPrice,
        Amounts = DividendAmounts,
        Times = DividendTimes,
        ContinuousRiskFreeRate = ContinuousRiskFreeRate,
        )
    #print '~~~StockPriceAdjusted', StockPrice

    if (ContinuousAssetYeildRate is None):
        ContinuousAssetYeildRate = 0.0

    TimePerInterval = float(TimeToMaturity) / IntervalCount

    #Solve for `p`, `u`, `d`  ->  which are functions of `a`
    #p = probability that the perfecntage change is u
    #1-p = probability that the percentage change is d
    #a = Growth Factor 

    #u
    PercentageChangeUpInOneInterval = numpy.exp(Volatility * numpy.sqrt(TimePerInterval) )
    if PrintExtra: print 'PercentageChangeUpInOneInterval', PercentageChangeUpInOneInterval

    #d
    PercentageChangeDownInOneInterval = numpy.exp((-1.0)*Volatility * numpy.sqrt(TimePerInterval) )
    if PrintExtra: print 'PercentageChangeDownInOneInterval', PercentageChangeDownInOneInterval

    #a
    GrowthFactor = numpy.exp( (ContinuousRiskFreeRate - ContinuousAssetYeildRate)*TimePerInterval )
    if PrintExtra: print 'GrowthFactor', GrowthFactor

    #p
    ProbabilityUp = (GrowthFactor -  PercentageChangeDownInOneInterval) / (PercentageChangeUpInOneInterval - PercentageChangeDownInOneInterval)
    if PrintExtra: print 'ProbabilityUp', ProbabilityUp

    #1-p
    ProbabilityDown = 1 - ProbabilityUp
    if PrintExtra: print 'ProbabilityDown', ProbabilityDown

    # Discount Factor
    DiscountFactorSingleInterval = numpy.exp( (-1.0)*(ContinuousRiskFreeRate) * TimePerInterval )
    if PrintExtra: print 'DiscountFactorSingleInterval', DiscountFactorSingleInterval

    #Start first node at t = 0 , last node at t = T
    NodeTimeCount = IntervalCount + 1
    NodeTimes = numpy.linspace(0, float(TimeToMaturity), NodeTimeCount)
    #print 'NodeTimes', NodeTimes
    NodeTimeNums = list(reversed(range(NodeTimeCount)))
    #print 'NodeTimeNums', NodeTimeNums




    FullAssetPriceTree = [[]]*NodeTimeCount
    FullOptionPriceTree = [[]]*NodeTimeCount




    #Work Backwards:
    for NodeTimeNum in NodeTimeNums:
        NodeTime = NodeTimes[NodeTimeNum]

        #Figure out the total value of all the dividends at the time of the node:
        NodeTimeDividendsTotalValueDiscounted = 0
        if (DividendTimes is not None and DividendAmounts is not None):
            for DividendTime, DividendAmount in zip(DividendTimes, DividendAmounts):
                if NodeTime < DividendTime:
                    NodeTimeDividendsTotalValueDiscounted += DividendAmount * numpy.exp( (-1.0) * ContinuousRiskFreeRate*(DividendTime - NodeTime) )
            #print 'NodeTimeDividendsTotalValueDiscounted', NodeTimeDividendsTotalValueDiscounted

        NodeTimePossibleAssetValues = []
        NodeTimePossibleOptionValues = []
        for PossibleValueNum in range(NodeTimeNum + 1):

            NodeTimePossibleAssetValue = StockPrice \
                * (PercentageChangeUpInOneInterval)**(NodeTimeNum - PossibleValueNum) \
                * (PercentageChangeDownInOneInterval)**(PossibleValueNum)

            NodeTimePossibleAssetValue += NodeTimeDividendsTotalValueDiscounted


            NodeTimePossibleAssetValues.append( NodeTimePossibleAssetValue )

            NodeTimePossibleOptionValue = None
            if NodeTimeNum == IntervalCount:
                NodeTimePossibleOptionValue = Library_OptionExerciseValue.Main(
                    CallOrPut= CallOrPut,
                    StockPrice= NodeTimePossibleAssetValue,
                    StrikePrice= StrikePrice
                    )
            else:
                NextNodeTimeNum = NodeTimeNum + 1
                NextNodeTimeValueUpIndex = PossibleValueNum
                NextNodeTimeValueDownIndex = PossibleValueNum + 1
                NextNodeTimeValueUpOptionValue = FullOptionPriceTree[NextNodeTimeNum][NextNodeTimeValueUpIndex]*DiscountFactorSingleInterval
                NextNodeTimeValueDownOptionValue = FullOptionPriceTree[NextNodeTimeNum][NextNodeTimeValueDownIndex]*DiscountFactorSingleInterval
                NodeTimePossibleOptionValueWait = ProbabilityUp*NextNodeTimeValueUpOptionValue + ProbabilityDown*NextNodeTimeValueDownOptionValue
                #print 'NodeTimePossibleOptionValueWait', NodeTimePossibleOptionValueWait

                if (EuropeanOrAmerican == 'American'):
                    NodeTimePossibleOptionValueExercise = Library_OptionExerciseValue.Main(
                        CallOrPut= CallOrPut,
                        StockPrice= NodeTimePossibleAssetValue,
                        StrikePrice= StrikePrice
                        )

                    #print 'NodeTimePossibleOptionValueExercise', NodeTimePossibleOptionValueExercise
                else:
                    NodeTimePossibleOptionValueExercise = 0.0

                NodeTimePossibleOptionValue = max(NodeTimePossibleOptionValueWait, NodeTimePossibleOptionValueExercise)
                #print 'NodeTimePossibleOptionValue', NodeTimePossibleOptionValue


            NodeTimePossibleOptionValues.append(NodeTimePossibleOptionValue)

        #if PrintExtra:
        #    print 'NodeTimePossibleAssetValues'
        #    print NodeTimePossibleAssetValues
        #    print 'NodeTimePossibleOptionValues'
        #    print NodeTimePossibleOptionValues

        FullAssetPriceTree[NodeTimeNum] = NodeTimePossibleAssetValues
        FullOptionPriceTree[NodeTimeNum] = NodeTimePossibleOptionValues


    if (PrintTree or PrintExtra):
        print 'FullOptionPriceTree'
        pprint.pprint(FullOptionPriceTree)
        
        print 'FullAssetPriceTree'
        pprint.pprint(FullAssetPriceTree)

    Result = FullOptionPriceTree[0][0]

    return Result 
































