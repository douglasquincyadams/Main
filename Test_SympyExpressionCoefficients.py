import Library_SympyExpressionCoefficients
import Library_TestLooper
import Library_StringExpressionToSympyExpression


ExpectedPoly1 = {
    Library_StringExpressionToSympyExpression.Main('1') : 3,
    Library_StringExpressionToSympyExpression.Main('x**2') : 2,
    Library_StringExpressionToSympyExpression.Main('x**3') : 1, 
}

ExpectedPoly2 = {
    Library_StringExpressionToSympyExpression.Main('1') : 1,
    Library_StringExpressionToSympyExpression.Main('x**2') : 2,
    Library_StringExpressionToSympyExpression.Main('x**3') : 3, 
}

ExpectedPoly3 = {
    Library_StringExpressionToSympyExpression.Main('1') : 1,
    Library_StringExpressionToSympyExpression.Main('x**2') : 0.70710678118,
    Library_StringExpressionToSympyExpression.Main('x**3') : 3, 
}

ExpectedPoly4 = {
    Library_StringExpressionToSympyExpression.Main('1') : 1,
    Library_StringExpressionToSympyExpression.Main('x**2') : -1.66658390518,
    Library_StringExpressionToSympyExpression.Main('x**3') : 3, 
}

ExpectedPoly5 = {
    Library_StringExpressionToSympyExpression.Main('1') : 1,
    Library_StringExpressionToSympyExpression.Main('x') : 1.22474487139159,
}

ExpectedPoly6 = {
    Library_StringExpressionToSympyExpression.Main('x') : 1.22474487139159,
}





ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "SympyExpression": Library_StringExpressionToSympyExpression.Main('3 + 2*x**2 + x**3')
        }
        , 
        ExpectedPoly1
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "SympyExpression": Library_StringExpressionToSympyExpression.Main('1 + 2*x**2 + 3*x**3')
        }
        , 
        ExpectedPoly2
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "SympyExpression": Library_StringExpressionToSympyExpression.Main('1 + sqrt(2)*x**2/2 + 3*x**3')
        }
        , 
        ExpectedPoly3
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "SympyExpression": Library_StringExpressionToSympyExpression.Main('1 + sqrt(2)*x**2/cos(34) + 3*x**3')
        }
        , 
        ExpectedPoly4
    )
)


ArgSetExpectedResultCombos.append(
    (
        
        {
            "SympyExpression": Library_StringExpressionToSympyExpression.Main('1+1.22474487139159*x')
        }
        , 
        ExpectedPoly5
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "SympyExpression": Library_StringExpressionToSympyExpression.Main('1.22474487139159*x')
        }
        , 
        ExpectedPoly6
    )
)




LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_SympyExpressionCoefficients.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = None,
    HardDifferenceMax = 0.1,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    MaxFlatResultLength = None,
    ResultOrderMatters = True, 
    EqualityCheckFunction = None,
    PrintExtra = True,
)

































