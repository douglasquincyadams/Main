"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Checks to see if an iterable of sympy expressions are ALL mathematically equivelent to each other
    WARNING: 
        Current Implementation is not robust. 
        Only Works for basic summations and products 
        No identy substitutions are attempted
        i.e. The following do not work:
            e^(i*x) != cos(x) + i*sin(x) #Euler Identity
            sin(.5*x) = (-1) **(abs(x/2*pi)) * sqrt( (1-cos(x)) / 2. ) #Half angle formula for sin
    TODO:
        http://mathworld.wolfram.com/Half-AngleFormulas.html
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
    SympyExpressions
        Type:
            Type_Iterable
                <type 'sympy.core.expression'>
        Description:
RETURNS:
    Result
        Type:
        Description:
"""
import Type_SympyExpression
import Type_Iterable
def Main(
    SympyExpressions = None,

    CheckArguments = True,
    PrintExtra = False,
    ):

    Result = True

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (not Type_Iterable.Main(SympyExpressions) ):
            ArgumentErrorMessage += '`SympyExpressions` must be of `Type_Iterable` \n'

        for Expression, ExpressionIndex in zip(SympyExpressions, range(len(SympyExpressions)) ):
            if (not Type_SympyExpression.Main(Expression)):
                ArgumentErrorMessage += 'Expression in SympyExpressions is not `Type_SympyExpression`:\n'
                ArgumentErrorMessage += '  SympyExpressions[' + str(ExpressionIndex) +']: '+str(Expression) + ' \n'

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    #TODO **** ADD identy substitutions

    Expression0 = SympyExpressions[0]
    for Expression in SympyExpressions:
        if (Expression0.simplify().expand().trigsimp() != Expression.simplify().expand().trigsimp()):
            Result = False

    return Result 



















