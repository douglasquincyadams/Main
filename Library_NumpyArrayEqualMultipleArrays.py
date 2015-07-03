"""
DESCRIPTION:

ARGS:
    

RETURNS:
    Result
        Description: true on all arrays equal, false on all arrays not equal
            
        Type: python bool
        


"""


import numpy
import Library_SortNumpyDataset

def Main(
    ArrayTuple = None, #Tuple of numpy arrays
    OrderMatters = True,
    CheckArguments = True,
    PrintExtra = False
    ):
    NumArrays = len(ArrayTuple)

    if (CheckArguments):
        ArgumentErrorMessage = ""
        if (NumArrays < 2):
            ArgumentErrorMessage += "len(ArrayTuple) < 2\n"
        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    if (OrderMatters):
        ArrayTupleCopy = ArrayTuple
    else:
        ArrayTupleCopy = []
        for Array in ArrayTuple:
            #print 'Array', Array
            SortedArray = Library_SortNumpyDataset.Main(Dataset = Array, Axis = 0)
            #print 'SortedArray', SortedArray
            ArrayTupleCopy.append( SortedArray )

            #ArrayTupleCopy.append( numpy.sort(Array, axis = 0 ) )

    Result = True
    k = 0 
    while (k < NumArrays - 1):
        Result = Result and numpy.array_equal(ArrayTupleCopy[k], ArrayTupleCopy[k + 1] )
        if (not Result):
            break
        k = k + 1

    return Result


















