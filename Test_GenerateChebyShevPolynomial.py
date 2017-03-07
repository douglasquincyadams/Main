import Library_GenerateChebyShevPolynomial
import Library_TestLooper
import Library_StringExpressionToSympyExpression
import Library_SympyExpressionEquality
import sympy
#First kinds strings:
T_0x	=	"1"
T_1x	=	"x"
T_2x	=	"2.0*(x**2)-1.0"
T_3x	=	"4.0*(x**3)-3.0*(x)"
T_4x	=	"8.0*(x**4)-8.0*(x**2)+1.0"
T_5x	=	"16.0*(x**5)-20.0*(x**3)+5.0*(x)"
T_6x	=	"32.0*(x**6)-48.0*(x**4)+18.0*(x**2)-1."

FirstKindStrings = [
T_0x,
T_1x,
T_2x,
T_3x,
T_4x,
T_5x,
T_6x,
]

#First kinds sympys:
FirstKindSympys = []
for FirstKindString in FirstKindStrings:
    FirstKindSympy = Library_StringExpressionToSympyExpression.Main(FirstKindString)
    FirstKindSympys.append(FirstKindSympy)
    print FirstKindSympy


ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "ApproximationSymbol": sympy.Symbol('y'),
            "ResultType":'sympy',
            "Kind": 1, 
            "Order": 4,
            "ReturnAll" : False,
        }
        , 
        FirstKindSympys[4].subs(sympy.Symbol('x'), sympy.Symbol('y'))
    )
)


ArgSetExpectedResultCombos.append(
    (
        
        {
            "ResultType":'sympy',
            "Kind": 1, 
            "Order": 0
        }
        , 
        FirstKindSympys[0]
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "ResultType":'sympy',
            "Kind": 1, 
            "Order": 1
        }
        , 
        FirstKindSympys[1]
    )
)
ArgSetExpectedResultCombos.append(
    (
        
        {
            "ResultType":'sympy',
            "Kind": 1, 
            "Order": 2
        }
        , 
        FirstKindSympys[2]
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "ResultType":'sympy',
            "Kind": 1, 
            "Order": 3
        }
        , 
        FirstKindSympys[3]
    )
)
ArgSetExpectedResultCombos.append(
    (
        
        {
            "ResultType":'sympy',
            "Kind": 1, 
            "Order": 4
        }
        , 
        FirstKindSympys[4]
    )
)


ArgSetExpectedResultCombos.append(
    (
        
        {
            "ResultType":'sympy',
            "Kind": 1, 
            "Order": 4,
            "ReturnAll" : True,
        }
        , 
        FirstKindSympys[:5]
    )
)


LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_GenerateChebyShevPolynomial.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    MaxFlatResultLength = None,
    ResultOrderMatters = True, 
    EqualityCheckFunction = Library_SympyExpressionEquality.Main,
    PrintExtra = True,
)

































