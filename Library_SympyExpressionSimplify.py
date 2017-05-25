"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Simplifys an expression in ALL the ways we know how
    This is Useful for equality checking between two expressions
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
    SympyExpression
        Type:
            <type 'NoneType'>
        Description:
RETURNS:
    Result
        Type:
        Description:
"""
import sympy
import sympy.sets
import copy
import Library_SympyExpressionPrintInfo

def Main(
    SympyExpression= None,
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


    try:
        #sin = copy.deepcopy(sympy.sin)
        #cos = copy.deepcopy(sympy.cos)
        #exp = copy.deepcopy(sympy.exp)

        #make a copy of input
        #Result = copy.deepcopy(SympyExpression)
        #if(PrintExtra): Library_SympyExpressionPrintInfo.Main(Result)
        Result = SympyExpression.simplify()

        #Force Trig Equalities, by plugging in the exp:
        Result = Result.rewrite(sympy.sin, sympy.exp).rewrite(sympy.cos, sympy.exp)
        if(PrintExtra):Library_SympyExpressionPrintInfo.Main(Result)
        
        #Simplify the Exponentials:
        Result = Result.trigsimp()
        if(PrintExtra):Library_SympyExpressionPrintInfo.Main(Result)

        #Force consts to be evaluated:
        Result = Result.evalf()
        if(PrintExtra):Library_SympyExpressionPrintInfo.Main(Result)

        #Do the built in symplifies:
        Result = Result.simplify().cancel().expand() #.logcombine()
        if(PrintExtra):Library_SympyExpressionPrintInfo.Main(Result)

        #Make another copy
        #FinalResult = copy.deepcopy(Result)
        #if(PrintExtra):Library_SympyExpressionPrintInfo.Main(FinalResult)
    except:
        Result = SympyExpression


    return Result 







