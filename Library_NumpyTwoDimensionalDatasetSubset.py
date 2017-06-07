"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Takes an arbirary Type_NumpyTwoDimensionalDataset
    And takes a subset of the dataset given a list required dlements for each column
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
    NumpyTwoDimensionalDataset
        Type:
            <type 'NoneType'>
        Description:
            some table of data of which the columns are selectable upon

    RequiredColumnValues:
        Type:
            <type 'list'>
        Description:
    
            a list of values for which the column elements MUST be thos values
            all nones are ignored.

            for example:
                [None, 2, None, 4]
                would rqurie that the first column has value 2, and the 3 column has value 4
                but we will accept any column for column 0 and column 3



RETURNS:
    Result
        Type:
            Type_NumpyTwoDimensionalDataset
        Description:
            a subset of the original full dataset 
"""
import numpy
import Library_IterableTakeSubsetOnCondition
#-------------------------------------------------------------------------------
def Main(
    RequiredColumnValues = None,
    NumpyTwoDimensionalDataset= None,
    CheckArguments = True,
    PrintExtra = False,
    ):

    Result = None

    ColumnCount = NumpyTwoDimensionalDataset.shape[1]
    RowCount = NumpyTwoDimensionalDataset.shape[0]

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if len(RequiredColumnValues) != ColumnCount:
            ArgumentErrorMessage += '`RequiredColumnValues` needs to have the same number of elements a columns'
        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)


    #Create the condition function upon which to keep the row in the dataset if it is true:
    def ExampleConditionFunction(Row):
        Result = True
        for RequiredColumnValue, ColumnValue in zip( RequiredColumnValues, Row):
            if RequiredColumnValue is not None:
                if RequiredColumnValue != ColumnValue:
                    Result = False
        return Result

    #Iterate through the dataset and only keep the rows which pass the condition:
    NumpyTwoDimensionalDatasetSubset = Library_IterableTakeSubsetOnCondition.Main(
        Iterable= NumpyTwoDimensionalDataset,
        ConditionFunction= ExampleConditionFunction,
        )

    #Cast the result back to the native numpy array type:
    NumpyTwoDimensionalDatasetSubset = numpy.array(NumpyTwoDimensionalDatasetSubset)

    #Return the final result
    Result = NumpyTwoDimensionalDatasetSubset
    return Result 





























