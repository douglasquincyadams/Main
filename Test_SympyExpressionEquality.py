import Library_SympyExpressionEquality
import Library_TestLooper
import Library_StringExpressionToSympyExpression

ExampleExpressionString1a = 'exp( i*( (x0 - 1)*(x0 + 2) ) )'
ExampleExpressionSympy1a = Library_StringExpressionToSympyExpression.Main(ExampleExpressionString1a)

ExampleExpressionString1b = 'exp( i*( (- 1 + x0 )*(x0 + 2) ) )'
ExampleExpressionSympy1b = Library_StringExpressionToSympyExpression.Main(ExampleExpressionString1b)

ExampleExpressionString2 = 'i*sin( (x0 - 1)*(x0 + 2) ) + cos( (x0 - 1)*(x0 + 2) )'
ExampleExpressionSympy2 = Library_StringExpressionToSympyExpression.Main(ExampleExpressionString2)


ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [ExampleExpressionSympy1a, ExampleExpressionSympy1b]}
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [ExampleExpressionSympy1a, ExampleExpressionSympy1b, ExampleExpressionSympy1b]}
        , 
        True
    )
)


ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": 'asdf' }
        , 
        Exception('')
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [ 'asdf', ExampleExpressionSympy1b, ExampleExpressionSympy1b] }
        , 
        Exception('')
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [ ['asdf', 'asdf'], ExampleExpressionSympy1b, ExampleExpressionSympy1b]}
        , 
        Exception('')
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [ExampleExpressionSympy1a, ExampleExpressionSympy1b, ExampleExpressionSympy1b]}
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [ExampleExpressionSympy1a, ExampleExpressionSympy2 ]}
        , 
        False #TODO **** FIX THIS
    )
)



LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_SympyExpressionEquality.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    ResultOrderMatters = True, 
    PrintExtra = True,
)
































