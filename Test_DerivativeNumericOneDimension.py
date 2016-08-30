import Library_DerivativeNumericOneDimension
import Library_TestLooper

import numpy

def ExampleFunction(Point = None):
    return Point**2



ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "Function": ExampleFunction, 
            "PointValue": 1., 
            "Epsilon": .01
        }
        , 
        2.0
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "Function": ExampleFunction, 
            "PointValue": 4., 
            "Epsilon": .01
        }
        , 
        8.0
    )
)


ArgSetExpectedResultCombos.append(
    (
        
        {
            "Function": numpy.sin, 
            "PointValue": 0.0, 
            "Epsilon": .01
        }
        , 
        1.0
    )
)





LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_DerivativeNumericOneDimension.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.01,
    HardDifferenceMax = 1.0,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    MaxFlatResultLength = None,
    ResultOrderMatters = True, 
    PrintExtra = True,
)

































