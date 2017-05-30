
"""
SOURCE:

DESCRIPTION:
    Invokes a python function with a dictionary of named argument values
    Useful for dynamic python function calls
    Trash


ARGS:

RETURNS:

"""

def Main( 
    Function = None, 
    ArgSet  = None,
    ):

    return Function( **ArgSet )


def MainInvoker(
    Function = None, 
    ArgSet  = None,
    ):

    return Function( **ArgSet )



