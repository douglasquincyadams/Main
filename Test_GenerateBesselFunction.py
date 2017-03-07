import Library_GenerateBesselFunction
import Library_TestLooper
import sympy
ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
            "ResultType": 'sympy', 
            "Kind": 1, 
            "Order": '0'
        }
        , 
        sympy.besselj( 0, sympy.Symbol('x') )
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "ResultType": 'sympy', 
            "Kind": 2, 
            "Order": '2'
        }
        , 
        None
    )
)



LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_GenerateBesselFunction.Main,
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
































