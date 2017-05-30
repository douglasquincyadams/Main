"""
DESCRIPTION:
    Evaluates a single function at a value
    if supplied, multiplies by a coeficient

ARGS:

RETURNS:
    Value which the function returns


"""


def Main(
    Function = None,
    DataPoint = None,
    Coefficient = None,
    CheckArguments = True,
    PrintExtra = False,
    ):

    if ( Coefficient == None ):
        Coefficient = 1.


    Result = Coefficient * Function(DataPoint)
    if (PrintExtra):
        print 'Coefficient', Coefficient
        print 'DataPoint', DataPoint
        #print inspect.getsource( Function )
        print 'Function(DataPoint)', Function(DataPoint)
        #assert(False)

    return Result































