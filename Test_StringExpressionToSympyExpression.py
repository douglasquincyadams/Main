import numpy
import sympy
import Library_StringExpressionToSympyExpression
import Library_TestLooper



ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "StringExpression": '-4 + 7.85398163397*I', 
        }
        , 
        -4. + 7.85398163397*sympy.I
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "StringExpression": '-inf + 7.85398163397*I', 
        }
        , 
        sympy.oo + 7.85398163397*sympy.I
    )
)

LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_StringExpressionToSympyExpression.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    MaxFlatResultLength = None,
    ResultOrderMatters = True, 
    EqualityCheckFunction = None,
    PrintExtra = True,
)










