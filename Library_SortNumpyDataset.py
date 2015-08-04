
"""
DESCRIPTION:
    Sorts a `Type_NumpyTwoDimensionalDataset` by either rows or columns

    The numpy.sort() routine seems to mess with the elements upon the sort
    

ARGS:
    Dataset:
        type: `<type 'list'>` , `Type_NumpyTwoDimensionalDataset` OR `Type_NumpyOneDimensionalDataset`
        Description: some sort of array of dimension 1 or 2
            Does not handle nested types (cannot be list of numpy arrays)

    CheckArguments:
        Type:
            Bool
        Description:
            IF left on:
                Dataset can be any type listed under it's heading
                Args will be checked for correctness, and errors thrown on bad calls
            If turned off:
                Dataset can only be of type `Type_NumpyTwoDimensionalDataset`
                Args are not checked for correctness
                Function runs faster

    Axis
        Type:
            python int
        Description:
            Must be 0 or 1   -> either sort the columns or the rows
        Default:
            0

    SortPriorityIndexes: (TODO)
        Type:
            python list
            
            Each element:
                Type:
                    python int
        Description:
            Deterimines which columns have priority in the sort
            *Must be the same length as the axis over which to sort
            *Must contain each possible index along that axis exactly once

            Each element must be an possible index such that:
                if (axis == 0):
                    Dataset[Index]  returns a value
                if (axis == 1):
                    Dataset.T[Index] returns a value

    PreserveOrder:
        Type:
            Bool

        Description:
            If this is set to true, then a list of indexes is returned 
                corresponding to the original array's order
            


RETURNS:
    Result:
        if (PreserveOrder):
            Type: `Type_NumpyTwoDimensionalDataset`
            Description: SortedDataset
        else:
            Type: python tuple
                [0]
                    Type:  type(Dataset)
                    Description: SortedDataset
                [1]
                    Type: Numpy 1D Array
                    Description: SortedDatasetIndexes
"""
import numpy
import Type_NumpyTwoDimensionalDataset
import Type_NumpyOneDimensionalDataset
import Library_CastNumpyOneDimensionalDatasetToNumpyTwoDimensionalDataset
def Main( 
    Dataset = None,
    Axis = 0,
    PreserveOrder = False,
    CheckArguments = True,
    ):
    if ( CheckArguments ):
        ArgumentErrorMessage = ""

        DatasetType = str(type(Dataset))
        #Type saving
        if ( DatasetType == "<type 'list'>"):
            Dataset = numpy.array(Dataset)
            DatasetDimension = 0
        if ( Type_NumpyOneDimensionalDataset.Main(Dataset) ):
            DatasetDimension = 1
            Dataset = Library_CastNumpyOneDimensionalDatasetToNumpyTwoDimensionalDataset.Main(Dataset)
        elif ( Type_NumpyTwoDimensionalDataset.Main(Dataset) ):
            DatasetDimension = 2
        else:
            ArgumentErrorMessage += "( Type_NumpyTwoDimensionalDataset.Main(Dataset) == False)\n"
        if ( len(ArgumentErrorMessage) > 0 ):
            raise Exception(ArgumentErrorMessage)

    #if (SortPriorityIndexes == []):
    if (Axis == 1) :
        SortedDatasetIndexes = numpy.lexsort(Dataset)
        SortedDataset = numpy.array( Dataset.T[SortedDatasetIndexes] ).T

    elif (Axis == 0):
        SortedDatasetIndexes = numpy.lexsort(Dataset.T).T
        SortedDataset = numpy.array( Dataset[SortedDatasetIndexes] )
    else:
        raise (Exception ("Only Eligable Axis in [0,1]"))

    if (CheckArguments):
        if (DatasetDimension == 1):
            #
            #import numpy
            #a=[2.3, 1.23, 3.4, 0.4]
            #a_sorted = numpy.sorted(a)
            #a_order = numpy.argsort(a)
            #
            SortedDataset = SortedDataset.T[0]

        if (DatasetType == "<type 'list'>" ):
            SortedDataset = SortedDataset.tolist()

    Result = None
    if ( PreserveOrder ):   
        Result = ( SortedDataset, SortedDatasetIndexes )
    else:
        Result = SortedDataset
    
    return Result

















