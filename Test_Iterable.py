



import Library_IsPrime
import numpy
import Type_Iterable
import Library_TestLooper





ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
            "IterableCandidate"  : [12,13]           , 
        }
        , 
        True
    )
)
ArgSetExpectedResultCombos.append(
    (
        {
            "IterableCandidate"  : 12           , 
        }
        , 
        False
    )
)
ArgSetExpectedResultCombos.append(
    (
        {
            "IterableCandidate"  : 'HelloWorld'           , 
        }
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "IterableCandidate"  : 'HelloWorld'           , 
            "StringAllowed" : False,
        }
        , 
        False
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "IterableCandidate"  : numpy.array([[1,2],[3,4],[5,6]])           , 
        }
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "IterableCandidate"  : numpy.array([[1,2],[3,4],[5,6]])           , 
            "StringAllowed" : False,
        }
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "IterableCandidate"  : Library_IsPrime.Main          ,  #WE have passed a function here
        }
        , 
        False
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "IterableCandidate"  : ['alpha','beta']           , 
        }
        , 
        True
    )
)
ArgSetExpectedResultCombos.append(
    (
        {
            "IterableCandidate"  : ['alpha','beta']           , 
            "StringAllowed" : False,
        }
        , 
        True
    )
)

LoopResult = Library_TestLooper.Main(
    FunctionToTest = Type_Iterable.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = None,
    HardDifferenceMax = 0.0,
    PrintExtra = False,
)
