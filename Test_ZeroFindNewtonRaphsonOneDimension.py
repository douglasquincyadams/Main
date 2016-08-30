import Library_ZeroFindNewtonRaphsonOneDimension
import Library_TestLooper


def quadratic(x):
    return (x-1.)*(x+2.)     # just a function to show it works



ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "Function": quadratic, 
            "StartPoint": 0.0, 
            "MaximumError": .01
        }
        , 
        1.
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "Function": quadratic, 
            "StartPoint": -3., 
            "MaximumError": .01
        }
        , 
        -2.
    )
)



LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_ZeroFindNewtonRaphsonOneDimension.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    MaxFlatResultLength = None,
    ResultOrderMatters = True, 
    PrintExtra = True,
)

































