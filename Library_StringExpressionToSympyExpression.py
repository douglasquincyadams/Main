"""

SOURCE:
http://docs.sympy.org/dev/modules/parsing.html

DESCRIPTION:

    Takes a string expression, like one you would throw at google,
    Returns a sympy expression which can then be picked appart and make use of various pythonic things

ARGS:
    StringExpression
        Type: Python String

RETURNS:
    SympyExpression
        Type: sympy expression

"""

import sympy
import sympy.parsing.sympy_parser #Requires second import for unknown reason
import Type_SympyExpression
#def StringExpressionToSympyExpression(
def Main(
    StringExpression = None,
    ):

    SympyExpression = None
    if isinstance(StringExpression, str):
        SympyExpression = sympy.parsing.sympy_parser.parse_expr(StringExpression, evaluate=False)
    else:
        raise Exception('StringExpression is bs type')

    return SympyExpression






