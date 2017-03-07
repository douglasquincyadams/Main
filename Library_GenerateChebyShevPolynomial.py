"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Creates a ChebyShevPolynomial
    which can be of various types.
ARGS:
    CheckArguments
        Type:
            python boolean
        Description:
            if true, checks the arguments with conditions written in the function
            if false, ignores those conditions
    PrintExtra
        Type:
            python integer
        Description:
            if greater than 0, prints addional information about the function
            if 0, function is expected to print nothing to console
            Additional Notes:
                The greater the number, the more output the function will print
                Most functions only use 0 or 1, but some can print more depending on the number
    Kind
        Type:
            <type 'int'>
        Description:
    Order
        Type:
            <type 'int'>
        Description:
    ResultType:
        Type:
            <type 'str'>

        Description:
            in ['sympy', 'python']



RETURNS:
    Result
        Type:
        Description:
"""
import pprint
import Library_SympyExpressionToPythonFunction
import Library_SympyExpressionToStringExpression
import sympy
import sympy.core
#import sympy.core.numbers

def Main(
    ApproximationSymbol = sympy.Symbol('x'),
    ResultType = 'sympy',
    Kind= None,
    Order= None,
    ReturnAll = False,
    CheckArguments = True,
    PrintExtra = False,
    ):

    Result = None

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    ChebyChevPolynomials = []
    ChebyChevPolynomials.append(sympy.sympify(1.))
    ChebyChevPolynomials.append(ApproximationSymbol)

    #Generate the polynomial with sympy:
    for Term in range(Order + 1)[2:]:
        Tn = ChebyChevPolynomials[Term - 1]
        Tnminus1 = ChebyChevPolynomials[Term - 2]
        Tnplus1 = 2*ApproximationSymbol*Tn - Tnminus1

        ChebyChevPolynomials.append(Tnplus1.simplify().expand().trigsimp())

    if(PrintExtra): print 'ChebyChevPolynomials'
    if(PrintExtra): pprint.pprint(ChebyChevPolynomials)


    if (ReturnAll):
        Result = []
        for SympyChebyChevPolynomial in ChebyChevPolynomials:
            if (ResultType == 'python'):
                Result.append(Library_SympyExpressionToPythonFunction.Main(SympyChebyChevPolynomial))
            elif (ResultType == 'string'):
                Result.append(Library_SympyExpressionToStringExpression.Main(SympyChebyChevPolynomial))
            else:
                Result.append(SympyChebyChevPolynomial)

    else:
        SympyExpression = ChebyChevPolynomials[Order] #the last one

        #If the result type is something other than sympy, we can cast it into that type here:
        if (ResultType == 'python'):
            Result = Library_SympyExpressionToPythonFunction.Main(SympyExpression)
        elif (ResultType == 'string'):
            Result = Library_SympyExpressionToStringExpression.Main(SympyExpression)
        else:
            Result = SympyExpression



    return Result 
























