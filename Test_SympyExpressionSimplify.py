import sympy
import Library_SympyExpressionSimplify
import Library_TestLooper
import Library_StringExpressionToSympyExpression

#There is no intuitive way to write a good test for this, 
#   as it is recursivly dependent on the useage of 
#   Library_SympyExpressionEquality
#   Tests are omited for now
ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "SympyExpression": sympy.sin(sympy.Symbol('x'))
        }
        , 
        sympy.sin(sympy.Symbol('x'))
    )
)



LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_SympyExpressionSimplify.Main,
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

































