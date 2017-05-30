import numpy

import Library_Poisson

import Library_TestLooper


ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
            "K"         : 3     , 
            "Lambda"    : 2     ,
        }
        , 
        [   0.180 ]
    )
)
ArgSetExpectedResultCombos.append(
    (
        {
            "K"         : 100   , 
            "Lambda"    : 100   ,
        }
        , 
        [  0.039 ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "K"         : 0   , 
            "Lambda"    : 0   ,
        }
        , 
        [  1 ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "K"         : 0   , 
            "Lambda"    : 0   ,
            "Log"       : True, 
        }
        , 
        [  0 ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "K"         : 1   , 
            "Lambda"    : 0   ,
            "Log"       : False, 
        }
        , 
        [  0 ]
    )
)


ArgSetExpectedResultCombos.append(
    (
        {
            "K"         : 1   , 
            "Lambda"    : 0   ,
            "Log"       : True, 
        }
        , 
        [  -1.*numpy.inf ]
    )
)

LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_Poisson.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = None,
    HardDifferenceMax = 0.01,
    PrintExtra = False,
)















