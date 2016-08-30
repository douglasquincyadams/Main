"""
SOURCE:
    Mind of Douglas Adams

    http://stackoverflow.com/questions/20659456/python-implementing-a-numerical-equation-solver-newton-raphson

DESCRIPTION:
    Finds the zeros of an arbitrary function on a chosen open interval
    Using the Newton Raphson method. 
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
    StartPoint
        Type:
            <type 'NoneType'>
        Description:
    MaximumError
        Type:
            <type 'NoneType'>
        Description:
RETURNS:
    Result
        Type:
        Description:
"""
import Library_DerivativeNumericOneDimension
def Main(
    Function= None,
    StartPoint= None,
    MaximumError= None,
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




    lastX = StartPoint
    nextX = lastX + 10 * MaximumError               # "different than lastX so loop starts OK
    while (abs(lastX - nextX) > MaximumError):      # this is how you terminate the loop - note use of abs()
        newY = Function(nextX)                      # just for debug... see what happens
        #print "f(", nextX, ") = ", newY            # print out progress... again just debug
        lastX = nextX
        lastX_deriv = Library_DerivativeNumericOneDimension.Main(
            Function= Function,
            PointValue= lastX,
            Epsilon= MaximumError,
            )
        nextX = lastX - newY / lastX_deriv  # update estimate using N-R

    Result =  nextX


    return Result 

































