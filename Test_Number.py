


import Type_Number

import numpy
import Library_TestLooper
import Library_IsPrime #Used to pass a bad value

print Type_Number.Main(0.0)

print Type_Number.Main(1.0)

print Type_Number.Main(1)

print Type_Number.Main(numpy.pi)


print Type_Number.Main('Hello World')

print Type_Number.Main(False + 1)

print Type_Number.Main(numpy.inf)

print 'DONE'
"""
ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
            "NumberCandidate"  : 1 ,
        }
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "NumberCandidate"  : 0 ,
        }
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "NumberCandidate"  : 1.0,
        }
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "NumberCandidate"  : numpy.pi,
        }
        , 
        True
    )
)


ArgSetExpectedResultCombos.append(
    (
        {
            "NumberCandidate"  : Library_IsPrime.Main          ,  #WE have passed a function here
        }
        , 
        False
    )
)


LoopResult = Library_TestLooper.Main(
    FunctionToTest = Type_Number.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = None,
    HardDifferenceMax = 0.0,
    PrintExtra = False,
)

"""
