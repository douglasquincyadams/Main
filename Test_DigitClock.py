
import numpy

import Library_DigitClock
import Library_TestLooper





ArgSetExpectedResultCombos = []


ArgSetExpectedResultCombos.append(
    (
        {
            "DigitMaximums"  : [1,2,1] , 
        }
        , 
        numpy.array([   
            [0,0,0],
            [0,0,1],
            [0,1,0],
            [0,1,1],
            [0,2,0],
            [0,2,1],
            [1,0,0],
            [1,0,1],
            [1,1,0],
            [1,1,1],
            [1,2,0],
            [1,2,1],
        ])
    )
)



LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_DigitClock.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = None,
    HardDifferenceMax = 0.001,
    ResultOrderMatters = False,
    PrintExtra = True,
)

