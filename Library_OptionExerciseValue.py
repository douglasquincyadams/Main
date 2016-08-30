"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Calculates the current value of an option if executed

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
RETURNS:
    Result
        Type:
        Description:
"""
def Main(
    CallOrPut= None,
    StockPrice= None,
    StrikePrice= None,
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

    
    if CallOrPut == 'Call':
        DiffValue = StockPrice - StrikePrice
    elif CallOrPut == 'Put':
        DiffValue = StrikePrice - StockPrice
    else:
        'Unknown option type'

    Result = max(0.0, DiffValue)

    return Result 












