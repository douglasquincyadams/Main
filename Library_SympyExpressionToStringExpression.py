"""
SOURCE:


DESCRIPTION:
    Takes an arbitrary sympy expression, and converts it into a string
    The string can then be reconverted into a sympy expression if desired

ARGS:
    SympyExpression
        Description: 
            An expression which has any number of variables in it, 
            which can be evaluated to a float upon fixing all the variables
        Type:
            Sympy Expression
        



RETURNS:
    StringExpression:
        Description:
            A new expression which is a product of polynomials
        Type:
            Sympy Expression

"""


def Main(
    SympyExpression = None,
    ):

    #TODO -> fix this line of code
    StringExpression = str(SympyExpression)
    #StringExpression = SympyExpression.tostring()

    return StringExpression
