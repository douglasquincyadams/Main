"""
DESCRIPTION:

    Because both python lists, and python numpy arrays both have retardedly complicated syntax for 
    selecting elements of a list which satisfy some condition,
    an implementation is made here.

ARGS:
    Iterable
        Type:
        Description:

    ConditionFunction:
        Type:
        Description:

RETURNS:

    IterableSubset
        Type: type(Iterable)
        Description: the subset of the `Iterable` for which `ConditionFunction` is true


"""

import numpy
import Type_Iterable
def Main(
    Iterable = None,
    ConditionFunction= None,
    PrintExtra= None,
    CheckArguments= None,
    ):


    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (not Type_Iterable.Main(Iterable)):
            ArgumentErrorMessage += 'ARG `Iterable`  must be of `Type_Iterable`'

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)




    IterableSubset = []
    print 'Starting function'

    for Item in Iterable:
        if (ConditionFunction(Item) == True):
            IterableSubset.append(Item)

    if (str(type(Iterable)) == "<type 'numpy.ndarray'>"):
        IterableSubset = numpy.array(IterableSubset)

    print 'ending function'

    return IterableSubset












































