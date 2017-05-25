import Type_SympyExpression
import Library_TestLooper
import Library_StringExpressionToSympyExpression
import sympy
ExampleExpressionString = '(x0- .3)*(x0 + .2)*(x0 - .1)+100'
SympyExpression = Library_StringExpressionToSympyExpression.Main(ExampleExpressionString)
#TODO: add python native complex numbers to the mix

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressionCandidate": SympyExpression}
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressionCandidate": sympy.I}
        , 
        True
    )
)



ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressionCandidate": 'yo dawg'}
        , 
        False
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressionCandidate": 1}
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressionCandidate": 4.}
        , 
        True
    )
)


LoopResult = Library_TestLooper.Main(
    FunctionToTest = Type_SympyExpression.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    ResultOrderMatters = True, 
    PrintExtra = True,
)
































