
import numpy


def Main(
    Array = None,
    SubsetFraction = 1.,
    CheckArguments = True,
    ):

    SparseSubsetArray = []

    if (CheckArguments):
        ArgumentErrorMessage = ""

        #Type check the args
        if (str(type(SubsetFraction)) in ["<type 'float'>", "<type 'int'>"] ):
            SubsetFraction = float(SubsetFraction)

        else:
            ArgumentErrorMessage += "SubsetFraction must be of type int or float"

        
        #if (Type_ObjectIterable.Main(Array) != True):
            ArgumentErrorMessage += "`Array` must be an iterable type"

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
                print "SubsetFraction", SubsetFraction
            raise Exception(ArgumentErrorMessage)


    Array = numpy.array(Array)
    print 'Array'
    print Array


    ArraySubsetChoiceMask = numpy.random.choice([0, 1], size=(len(Array),), p=[(1 - SubsetFraction), SubsetFraction]).astype('bool')
    
    print 'ArraySubsetChoiceMask'
    print ArraySubsetChoiceMask




    SparseSubsetArray = Array[ArraySubsetChoiceMask]


    print 'SparseSubsetArray'
    print SparseSubsetArray


    """
    FractionDenom = SubsetFraction**(-1)

    k = 0 
    for Element in Array:
        if (k % FractionDenom == 0):
            SparseSubsetArray.append(Array)
        k = k + 1
    
    """

    return SparseSubsetArray














