"""
DESCRIPTION:
    array = ['a       ', ' b    ', 'c   ']

    ==>    

    expected_result = ['a', ' b', 'c']

ARGS:
    Array

Returns
    python list

"""

def Main(Array):
    #print Array
    NoTrailingArray = []
    for Element in Array:
        NoTrailingArray.append(Element.rstrip())

    return NoTrailingArray

