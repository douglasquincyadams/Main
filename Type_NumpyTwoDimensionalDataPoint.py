"""
SOURCE:

DESCRIPTION:

    ALWAYS `Type_NumpyOneDimensionalDataset`



    Checks to see if the only arg `DataPoint` is of the following form:
        Numpy Array:
            [ xCoord, yCoord, ..., zCoord ]
                

ARGS:
    DataPoint
        Type: Any
        Description: the datapoint to be tested regarding the type

RETURNS:
    True -> when dataset meets criterion for `Type_NumpyTwoDimensionalDataPoint`

    OR
    
    False -> when dataset does NOT meet criterion for `Type_NumpyTwoDimensionalDataPoint`

"""

import numpy
import Type_NumpyOneDimensionalDataset

def Main(
    DataPoint = None, 
    NumberDimensions = None, 
    PrintExtra = False
    ):

    if ( Type_NumpyOneDimensionalDataset.Main(DataPoint) == False):
        if (PrintExtra):
            print "DataPoint must be of type `Type_NumpyOneDimensionalDataset` to be of type `Type_NumpyTwoDimensionalDataPoint`"
        return False 
    #if ( NumberDimensions != None and NumberDimensions != DataPoint.shape[0]):
    #    if (PrintExtra):
    #        print "DataPoint does not have correct number of dimensions"
    #    return False 

    EligibleCoordinateTypes = [
        "<type 'numpy.int64'>",
        "<type 'numpy.float64'>" ,
        "<type 'float'>",
        ]
    for Coordinate in DataPoint:
        if (not (str(type(Coordinate)) in EligibleCoordinateTypes) ):
            if (PrintExtra):
                print ' DataPoint contains a coordinate of unexpected type'
                print ' Coordinate', Coordinate
                print ' type(Coordinate)', type(Coordinate)
            return False

    return True























        
