"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Checks if an iterable is sorted
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
    Iterable
        Type:
            <type 'list'>
        Description:
RETURNS:
    Result
        Type:
        Description:
"""

import itertools
def Main(
    Iterable = [],
    Method = 'all', #Fastest
    CheckArguments = False,
    PrintExtra = False,
    ):

    Result = None

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    if( Method == 'iter' ):
        it = iter(Iterable)
        it.next()
        Result = all(b >= a for a, b in itertools.izip(Iterable, it))
    elif (Method == 'all'):
        Result = all(Iterable[i] <= Iterable[i+1] for i in xrange(len(Iterable)-1))
    
    elif (Method == 'sorted'):
        Result = sorted(Iterable) == Iterable

    return Result 

















