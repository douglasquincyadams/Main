"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Creates a bessel function in sympy
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
    ResultType
        Type:
            <type 'NoneType'>
        Description:
    Kind
        Type:
            <type 'NoneType'>
        Description:
    Order
        Type:
            <type 'NoneType'>
        Description:
RETURNS:
    Result
        Type:
        Description:
"""
import sympy
import Library_SympyExpressionToPythonFunction
import Library_SympyExpressionToStringExpression

def Main(
    ResultType = None,
    Kind = 1,
    Order = None,
    VariableNames = ['x'],

    CheckArguments = True,
    PrintExtra = False,
    ):

    Result = None

    if (CheckArguments):
        ArgumentErrorMessage = ""
    
        AllowedResultTypes = ['sympy',  'string', 'python',]
        if ( not ResultType in AllowedResultTypes):
            ArgumentErrorMessage += 'Arg `ResultType` Must be any of: [' 
            for AllowedResultType in AllowedResultTypes:
                ArgumentErrorMessage += '\'' + AllowedResultType + '\','
            ArgumentErrorMessage += ']\n'
            ArgumentErrorMessage += '`ResultType` = ' + str(ResultType) + '\n'

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)


    if (len(VariableNames) == 1):
        OnlyVariableName = VariableNames[0]
        if (Kind == 1):
            if (ResultType == 'sympy'):
                    Result = sympy.besselj( Order, sympy.Symbol(OnlyVariableName) )
            if (ResultType == 'string'):
                    SympyBessel = sympy.besselj( Order, sympy.Symbol(OnlyVariableName) )
                    Result = Library_SympyExpressionToStringExpression.Main( SympyBessel )
            if (ResultType == 'python'):
                    SympyBessel = sympy.besselj( Order, sympy.Symbol(OnlyVariableName) )
                    Result = Library_SympyExpressionToPythonFunction.Main( SympyBessel )

    return Result 






















