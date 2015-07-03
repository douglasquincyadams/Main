
"""
DESCRIPTION:

    Searches for a 'hi' array and a 'lo' array of values to find an index 
    The index returned is used elsewhere to lookup parameters for fermi instrument response


    If the index should be lower than 0, 0 is returned

    If the index should be larger than the `Max Index`:
        `Max Index` will be returned

ARGS:


RETURNS:
"""


def Main(
    Value = None,
    Los = None,
    His = None,
    ):
    Index = -1

    NumberIndexes = len(Los)

    if (Value < Los[0]):
        Index = 0

    elif (Value > His[-1]):
        Index = NumberIndexes - 1

    else:
        k = 0 
        while (k < NumberIndexes):
            SingleLo = Los[k]
            #print 'SingleEnergyLo', SingleEnergyLo

            SingleHi = His[k]
            #print 'SingleEnergyHi', SingleEnergyHi

            if (    Value > SingleLo
                and Value < SingleHi):
                Index = k
                break
            k = k + 1

    return Index



























