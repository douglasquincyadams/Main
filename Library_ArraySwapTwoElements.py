"""
SOURCE:
    http://stackoverflow.com/questions/2493920/how-to-switch-position-of-two-items-in-a-python-list
DESCRIPTION:
    Swaps two elemnts of an array
    Puts each element at the index location of the other
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
    Array
        Type:
            <type 'NoneType'>
        Description:
    Index1
        Type:
            <type 'NoneType'>
        Description:
    Index2
        Type:
            <type 'NoneType'>
        Description:
RETURNS:
    Result
        Type:
        Description:
"""
import copy
def Main(
    Array = None,
    Index1 = None,
    Index2 = None,

    CheckArguments = True,
    PrintExtra = False,
    ):

    Result = None

    if (CheckArguments):
        ArgumentErrorMessage = ""
        if (None in [Array, Index1, Index2]):
            ArgumentErrorMessage += 'All args must not be null'

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    ArrayCopy = copy.deepcopy(Array)

    ArrayCopy[Index2], ArrayCopy[Index1] = ArrayCopy[Index1], ArrayCopy[Index2]

    return ArrayCopy 



