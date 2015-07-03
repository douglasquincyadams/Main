
"""
Type_NumpyOneDimensionalDataset

Desciption:

    Checks to see if the only arg `Dataset` is of the following form:
        Dataset
        == 
        [point, point, ... , point]
        ==
        where each `point` is a scalar value

ARGS:
    Dataset: (any) 
        This is the thing we are checking

    PrintExtra: (boolean)

RETURNS:
    True -> when dataset meets criterion for `Type_NumpyOneDimensionalDataset`

    OR
    
    False -> when dataset does NOT meet criterion for `Type_NumpyOneDimensionalDataset`


"""

import numpy
#------------------------------------------------------------------------------

def Main(Dataset = None, PrintExtra = False):

    #Must not be null
    if Dataset == None:
        if (PrintExtra):
            print "Emtpy Dataset: Must not be null"
        return False 

    #Type Numpy Array
    if ( str(type(Dataset)) != "<type 'numpy.ndarray'>" ):
        if (PrintExtra):
            print "DatasetType:  must be Type Numpy Array"
        return False
    
    #Must be One Code Dimension 
    if (len(Dataset.shape) != 1):
        if (PrintExtra):
            print "len(Dataset.shape) != 1: NumpyOneDimensionalDataset must be exactly One Code Dimension"
        return False

    #Must have at least 1 observation
    if (Dataset.shape[0] < 1):
        if (PrintExtra):
            print "DatasetShape[1] < 1 NumpyOneDimensionalDataset must have at least 1 observation"
        return False
        
    return True
    
