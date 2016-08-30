import sympy
#------------------------------------------------------------------------------
import Library_SympyExpressionEquality
import Library_TestLooper
import Library_StringExpressionToSympyExpression
import Library_SympyExpressionRestrictVariables
import Library_SympyExpressionSimplify
import Library_SympyExpressionPrintInfo
#------------------------------------------------------------------------------

#Create some variables:
pi = sympy.pi
x = sympy.Symbol('x')
n = sympy.Symbol('n')
T = sympy.Symbol('T')

#Create a copy with the main variable restricted
x_restricted = sympy.Symbol('x', real=True)
n_restricted = sympy.Symbol('n', real=True)
T_restricted = sympy.Symbol('T', real=True)

#Create a basic sympy expression of more than 1 variable
FourierBasisExpression = sympy.sin(n*pi*x/T )
print '\nFourierBasisExpression'
Library_SympyExpressionPrintInfo.Main(FourierBasisExpression)

FourierBasisExpressionRestrictedX = sympy.sin( n*pi*x_restricted/ T )
print '\nFourierBasisExpressionRestrictedX'
Library_SympyExpressionPrintInfo.Main(FourierBasisExpressionRestrictedX)

FourierBasisExpressionUnrestrictedX = Library_SympyExpressionRestrictVariables.Main(
    SympyExpression = FourierBasisExpressionRestrictedX,
    Restrictions = None
    )
print '\nFourierBasisExpressionUnrestrictedX'
Library_SympyExpressionPrintInfo.Main(FourierBasisExpressionUnrestrictedX)



FourierBasisExpressionRestrictedNXT = Library_SympyExpressionRestrictVariables.Main(
    SympyExpression = FourierBasisExpression,
    Restrictions = {'Real': True}
    )

Example_x = sympy.Symbol('x')
Example_x_Restrict = Library_SympyExpressionRestrictVariables.Main(
    SympyExpression = Example_x,
    Restrictions = {'Real': True}
    )




ExampleExpressionString1a = 'exp( I*( (x0 - 1)*(x0 + 2) ) )'
ExampleExpressionSympy1a = Library_StringExpressionToSympyExpression.Main(ExampleExpressionString1a)
ExampleExpressionSympy1aSimplified = Library_SympyExpressionSimplify.Main(ExampleExpressionSympy1a)


ExampleExpressionString1b = 'exp( I*( (- 1 + x0 )*(x0 + 2) ) )'
ExampleExpressionSympy1b = Library_StringExpressionToSympyExpression.Main(ExampleExpressionString1b)
ExampleExpressionSympy1bSimplified = Library_SympyExpressionSimplify.Main(ExampleExpressionSympy1b)


ExampleExpressionString2 = 'I*sin( (x0 - 1)*(x0 + 2) ) + cos( (x0 - 1)*(x0 + 2) )'
ExampleExpressionSympy2 = Library_StringExpressionToSympyExpression.Main(ExampleExpressionString2)
ExampleExpressionSympy2Simplified = Library_SympyExpressionSimplify.Main(ExampleExpressionSympy2)

Const1 = Library_StringExpressionToSympyExpression.Main( "sqrt(2/pi)" )
Const2 = Library_StringExpressionToSympyExpression.Main( "0.7978845608" ) 


ArgSetExpectedResultCombos = []

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [
            sympy.sin(sympy.Symbol('x',)),
            sympy.sin(sympy.Symbol('x', real = True)) , 
            
            ]}
        , 
        False
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [
            
            sympy.sin(sympy.Symbol('x', real = True)) , 
            sympy.sin(sympy.Symbol('x',)),
            
            ]}
        , 
        False
    )
)



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
        {"SympyExpressions": [ Const1, Const2 ],
        "HardDifferenceMax": .1 
        }
        , 
        True
    )
)


ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [ExampleExpressionSympy1a, ExampleExpressionSympy2 ]}
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [
            Library_StringExpressionToSympyExpression.Main( '1.22474487139159*x' ) , 
            Library_StringExpressionToSympyExpression.Main( 'sqrt(6)*x/2' )  
            ],
        "HardDifferenceMax": .1 
        }
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [
            ExampleExpressionSympy1a , 
            ExampleExpressionSympy1aSimplified
            ]}
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [
            ExampleExpressionSympy1b , 
            ExampleExpressionSympy1bSimplified
            ]}
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [
            ExampleExpressionSympy2, 
            ExampleExpressionSympy2Simplified
            ]}
        , 
        True
    )
)







ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [
            sympy.sin(sympy.Symbol('y'))*sympy.sin(sympy.Symbol('x', real = True)) , 
            sympy.sin(sympy.Symbol('y'))*sympy.sin(sympy.Symbol('x',))
            ]}
        , 
        False
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [
            Example_x , 
            Example_x
            ]}
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [
            Example_x , 
            Example_x_Restrict
            ]}
        , 
        False
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [
            FourierBasisExpression , 
            FourierBasisExpressionRestrictedX
            ]}
        , 
        False
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [
            FourierBasisExpression , 
            FourierBasisExpressionRestrictedNXT
            ]}
        , 
        False
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [
            FourierBasisExpression , 
            FourierBasisExpressionUnrestrictedX
            ]}
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"SympyExpressions": [
             Library_StringExpressionToSympyExpression.Main( '-0.418546 + 7.85398*I' ) , 
             Library_StringExpressionToSympyExpression.Main( '-0.418546340629224 + 2.5*I*pi' )
            ],
        "HardDifferenceMax": .1 
        }
        , 
        True
    )
)



LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_SympyExpressionEquality.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 0.1,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    ResultOrderMatters = True, 
    PrintExtra = True,
)
































