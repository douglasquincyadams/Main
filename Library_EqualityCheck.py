"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Checks if each element within a tuple of objects is EXACTLY the same
    ExampleObjectsTuple = (a,b,c)
    To return true, the following must also be true:
        a == b
        a == c
        b == c
        b == a
        c == a
        c == b
    Is expected to work on arbitary python objects


    TODO:
        STUFF MIGHT GET WEIRD WITH FUNCTION COPIES
        -> UNTESTED BEHAVIOR


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
    ObjectsTuple
        Type:
            <type 'tuple'>
        Description:
            tuple of python objects

RETURNS:
    Result
        Type:
        Description:
"""
import pickle
import Type_SympyExpression
import Library_SympyExpressionEquality
def Main(
    ObjectsTuple = None,

    CheckArguments = True,
    PrintExtra = False,
    ):

    Result = True

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    #Duck equality checking ->
    FirstObject = ObjectsTuple[0]

    ObjectType = None
    if ( Type_SympyExpression.Main(FirstObject) ):
        ObjectType = 'sympy'
    #elif (Type_stuff la do di da):
    #    ObjectType = 'la do di da'

    for Object in ObjectsTuple:
        if(ObjectType == 'sympy'):
            Result = Result and Library_SympyExpressionEquality.Main( (Object , FirstObject) )
        else:
            Result = Result and (pickle.dumps(Object) == pickle.dumps(FirstObject))

    return Result 
















