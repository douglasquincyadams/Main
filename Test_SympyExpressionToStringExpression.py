import Library_SympyExpressionToStringExpression

#TODO -> make proper test


ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
            "SympyExpression"  : [ """ TODO """ ]           , 

        }
        , 
        [ "cos(x)*sin(x)+8" ] #unclear how the multiplication will be printed 
    )
)
ArgSetExpectedResultCombos.append(
    (
        {
            "SympyExpression"  : [ """ TODO """ ]           , 

        }
        , 
        [ "exp(x)*sin(x)+8" ] #unclear how the exponentiation will be printed 
    )
)

LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_SympyExpressionToStringExpression.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    PrintExtra = True,
)
