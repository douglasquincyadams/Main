import sympy
import Library_SympyExpressionRestrictVariables
import Library_TestLooper
import Library_StringExpressionToSympyExpression
import Library_SympyExpressionEquality
import copy



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
FourierBasisExpressionRestrictedX = sympy.sin( n*pi*x_restricted/ T )
FourierBasisExpressionRestrictedNXT = sympy.sin( n_restricted*pi*x_restricted/ T_restricted )

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "SympyExpression": FourierBasisExpression, 
            "Restrictions": {'real':True}, 
            "VariableNames": ['x', 'z'] #No z exists in the expression -> should throw error
        }
        , 
        Exception('')
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "SympyExpression": FourierBasisExpression, 
            "Restrictions": {'real':True}, 
            "VariableNames": ['x']
        }
        , 
        FourierBasisExpressionRestrictedX
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "SympyExpression": FourierBasisExpressionRestrictedX, 
            "Restrictions": None, 
            "VariableNames": ['x']
        }
        , 
        FourierBasisExpression
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            #Remove all restrictions
            "SympyExpression": FourierBasisExpressionRestrictedNXT, 
            "Restrictions": None, 
            "VariableNames": None
        }
        , 
        FourierBasisExpression
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            #Remove all restrictions
            "SympyExpression": FourierBasisExpressionRestrictedNXT, 
            "Restrictions": None, 
            "VariableNames": None
        }
        , 
        FourierBasisExpression
    )
)


LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_SympyExpressionRestrictVariables.Main,
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

































