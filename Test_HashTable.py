





import Library_IsPrime
import numpy
import Type_HashTable
import Library_TestLooper





ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
            "HashTableCandidate"  : {'key1': 'Value1'}           , 
        }
        , 
        True
    )
)
ArgSetExpectedResultCombos.append(
    (
        {
            "HashTableCandidate"  : [12,13]           , 
        }
        , 
        False
    )
)
ArgSetExpectedResultCombos.append(
    (
        {
            "HashTableCandidate"  : 12           , 
        }
        , 
        False
    )
)
ArgSetExpectedResultCombos.append(
    (
        {
            "HashTableCandidate"  : 'HelloWorld'           , 
        }
        , 
        False
    )
)
ArgSetExpectedResultCombos.append(
    (
        {
            "HashTableCandidate"  : numpy.array([[1,2],[3,4],[5,6]])           , 
        }
        , 
        False
    )
)
ArgSetExpectedResultCombos.append(
    (
        {
            "HashTableCandidate"  : Library_IsPrime.Main          ,  #WE have passed a function here
        }
        , 
        False
    )
)

LoopResult = Library_TestLooper.Main(
    FunctionToTest = Type_HashTable.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = None,
    HardDifferenceMax = 0.0,
    PrintExtra = False,
)
