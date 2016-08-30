"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Find the numeric derivative of an arbitrary one dimensional python function. 
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
    Function
        Type:
            <type 'NoneType'>
        Description:
    PointValue
        Type:
            <type 'NoneType'>
        Description:
    Epsilon
        Type:
            <type 'NoneType'>
        Description:
RETURNS:
    Result
        Type:
        Description:
"""
def Main(
    Function= None,
    PointValue= None,
    Epsilon= None,
    CheckArguments = False, #We want this to be fast.
    PrintExtra = False,
    ):

    Result = None

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if(not Type_Number.Main(PointValue)):
            ArgumentErrorMessage = "`PointValue` must be a number.\n"

        if(not Type_Number.Main(Epsilon)):
            ArgumentErrorMessage = "`Epsilon` must be a number.\n"

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)


    Result = (Function(PointValue+Epsilon) - Function(PointValue-Epsilon)) / (2.0*Epsilon)

    return Result 







