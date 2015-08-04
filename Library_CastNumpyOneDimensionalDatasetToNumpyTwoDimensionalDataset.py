"""
DESCRIPTION:
    Takes a dataset of the form:
        ``
    and converts it to a dataset of the form:
        ``
    
ARGS:
    Dataset
        Type: `Type_NumpyOneDimensionalDataset`
RETURNS:
    Dataset
        Type: `Type_NumpyTwoDimensionalDataset`


"""


import numpy
def Main(NumpyOneDimensionalDataset = None):
    NumpyTwoDimensionalDataset = numpy.atleast_2d(NumpyOneDimensionalDataset).T
    return NumpyTwoDimensionalDataset

