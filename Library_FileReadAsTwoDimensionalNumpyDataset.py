"""
DESCRIPTION:
    Opens a file and returns a 2D numpy  array of float values


    Reason for splitting data into floats and strings:

        I not concat these two arrays of different types in numpy.             ...Brilliant
            PROOF: 
                http://docs.scipy.org/doc/numpy/user/basics.rec.html
                http://stackoverflow.com/questions/11309739/store-different-datatypes-in-one-numpy-array

            CONCLUSTION:
                HOW IS THIS NOT A PROBLEM?????  <- Anger Anger Anger Anger Anger Anger 
                Somebody at numpy needs to get on their job


ARGS:
    Filepath
        The filepath to open 
    Delimeter   
        The character on which to split lines
    FirstDataLineNumber
        The first line of the file which contains wanted data
    HeaderLineNumber
        The line of the file which has column names
    ColumnNames 
        The columns on which to select a subset of the data
        If Ommited - requires Column Numbers to be passed
    ColumnNumbers 
        The columns on which to select the subset of the data
        Can be inferred from ColumnNames

    ReturnSubsetFloat = True
        Return float subset or nonfloat subset of the data
        Stupidity of numpy causes the existence of this arg(see description)

RETURNS:
    DatasetFloatPart   OR   DatasetNotFloatPart
        Stupidity of numpy causes the existence of these two possibilities (see description)
  

TESTS:
    None
"""




import numpy
import Library_FileReadAsTable

def Main(\
    Filepath = None, \
    Delimeter = None, \
    FirstDataLineNumber = None,\
    HeaderLineNumber = None,\
    ColumnNames = None,\
    ColumnNamesCastFloat = None,\
    RowUnitTransformFunction = lambda Row, HeaderRow: Row, \
    PrintExtra = False,\
    CheckArguments = True, \
    FilterNone = False, \
    ):

    #TODO: Any arg checking??? right now this is vacant
    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)


    FileAsTable = Library_FileReadAsTable.Main(\
        Filepath = Filepath, \
        Delimeter = Delimeter, \
        FilterNone = FilterNone,\
        )

    if (CheckArguments and (len(FileAsTable[FirstDataLineNumber]) < len(ColumnNames))):
        print "len(FileAsTable[FirstDataLineNumber])", len(FileAsTable[FirstDataLineNumber])
        print "len(ColumnNames)", len(ColumnNames)
        raise Exception("(len(FileAsTable[0]) < len(ColumnNames)) | `Likely A Delimeter Error`")

    if ( PrintExtra ):
        print "FileAsTable", FileAsTable

    HeaderRow = FileAsTable[HeaderLineNumber]
    if ( PrintExtra ):
        print "HeaderRow", HeaderRow

    #Find the column numbers associated with the column names to include
    ColumnNumbers = []
    for ColumnName in ColumnNames:
        ColumnNumbers.append( HeaderRow.index(ColumnName) )

    #Find the column numbers which we have to cast to float 
    ColumnNumbersCastFloat = []
    for ColumnName in ColumnNamesCastFloat:
        ColumnNumbersCastFloat.append( HeaderRow.index(ColumnName) )
    if ( PrintExtra ):
        print "ColumnNumbers", ColumnNumbers

    #Extract the lines which have data:
    FileAsTableLinesNeeded = FileAsTable[FirstDataLineNumber : -1]

    #Transform rows in place to have the unit conversions we want:
    RowCount = len(FileAsTableLinesNeeded)
    k = 0
    while(k < RowCount):
        FileAsTableLinesNeeded[k] = RowUnitTransformFunction( FileAsTableLinesNeeded[k], HeaderRow )
        k = k + 1

    #Transform the data into a numpy two dimensional dataset
    DataNumpyTwoDimensionalDataset = numpy.array(FileAsTableLinesNeeded)

    if (len(DataNumpyTwoDimensionalDataset.shape) < 2):
        DataNumpyTwoDimensionalDataset = numpy.atleast_2d(DataNumpyTwoDimensionalDataset).T

    #Convert the data to floats:
    ColumnNumbersNotCastFloat = list(set(ColumnNumbers) - set(ColumnNumbersCastFloat))
    
    if (PrintExtra):
        print "ColumnNumbers", ColumnNumbers
        print "ColumnNumbersNotCastFloat", ColumnNumbersNotCastFloat
        print "ColumnNumbersCastFloat", ColumnNumbersCastFloat
   
    #print "--------"
    #print "DataNumpyTwoDimensionalDataset", DataNumpyTwoDimensionalDataset
    #print "-------"

    DatasetNotFloatPart = DataNumpyTwoDimensionalDataset[:, ColumnNumbersNotCastFloat]
    DatasetFloatPart = DataNumpyTwoDimensionalDataset[:, ColumnNumbersCastFloat].astype(numpy.float)

    #CANNOT CONCAT(this is retarded) : 
    #   See 
    #       Work arounds in commented section at bottom of file
    #           which are valueless and more trouble than worth
    #       Description for concrete exmaples of performing these work arounds
    #   Does not allow numpy subset selection / array actions which defeats the use of numpy arrays
    #Dataset = numpy.concatenate((DatasetNotFloatPart, DatasetFloatPart), axis=1)  #<- should be possible but it's not


    #Dataset = None
    #if (ReturnSubsetFloat):
    #    Dataset = DatasetFloatPart
    #else:
    #    Dataset = DatasetNotFloatPart
    #return Dataset
    
    return DatasetFloatPart, DatasetNotFloatPart








"""

    #Structured Array BS:
    dtypes_row = ''
    NumRows = DataNumpyTwoDimensionalDataset.shape[0]
    NumColumns = DataNumpyTwoDimensionalDataset.shape[1]
    
    print "NumRows", NumRows
    print "NumColumns", NumColumns


    k = 0
    while (k < NumColumns):
        if (k != 0 and k in ColumnNumbers):
            dtypes_row += ', '
        if (k in ColumnNumbersNotCastFloat):
            dtypes_row += 'float64'
        elif (k in ColumnNumbersCastFloat):
            dtypes_row += 'float64'
        k = k + 1

    print "dtypes_row:\n '", dtypes_row , "'"
    Dataset = numpy.zeros( (NumRows,)  , dtype = dtypes_row)

"""


















