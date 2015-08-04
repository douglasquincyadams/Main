"""
DESCRIPTION:
    Parses through a fermi Fits file and extracts all observed events into a numpy array
    It is assumed that columns which columns are which after the extraction
    Performs no cuts on the data - all columns, and all events are included in the 2D numpy array

ARGS:
    Filepath
        Description: location of the fits file
        Type: python String

RETURNS:
    EventsNumpyArray:
        Type: One Dimensional Numpy Array OF Tuples WITH Column Names
        Description:
            Dimensions of `Dataset` are as follows:
                [
                    Event1, 
                    Event2 == (Event2_col0_value, ... , Event2_colN_value ),
                    .
                    .
                    EventN
                ]


            EventsNumpyArray[`<columnName>`] ->  returns a column of the table result
            EventsNumpyArray[0] -> returns a tuple (col0_value, ... , colN_value )
            EventsNumpyArray[`<columnName>`][0] -> returns the first event's value of that column

    EventsColumnNames:
        Type: Python List
        Description:
            ColumnNames associated with the datatable which is returned
            This can be used to help with selection on the numpy dataset

"""
import numpy
import astropy
import astropy.io.fits
#------------------------------------------------------------------------------
import Library_AstropyFitsTablePrettyPrint


def Main(\
    Filepath = None,\
    PrintExtra = False,\
    ):
    #Astropy uses zero-based indexing
    #Fortran uses FITS bases standard one-based indexing
    HDUList = astropy.io.fits.open(Filepath)

    if (PrintExtra):
        print 'FILE INFO: \n'
        HDUList.info()

    NumTables = len(HDUList)

    if (PrintExtra):
        print 'NumTables', NumTables

    ###########################################################################
    #Primary Table:
    PRIMARY = HDUList[0]
    if (PrintExtra):
        Library_AstropyFitsTablePrettyPrint.Main(FitsTable = PRIMARY, TableName = "PRIMARY")

    ###########################################################################
    #Events Table:
    EVENTS = HDUList[1]
    if (PrintExtra):
        Library_AstropyFitsTablePrettyPrint.Main(FitsTable = EVENTS, TableName = "EVENTS")

    ###########################################################################
    #GTI Table:
    GTI = HDUList[2]
    if (PrintExtra):
        Library_AstropyFitsTablePrettyPrint.Main(FitsTable = GTI, TableName = "GTI")

    EventsColumnNames = EVENTS.columns.names
    
    EventsNumpyArray = numpy.array( EVENTS.data )

    Result = EventsNumpyArray, EventsColumnNames
    return Result


































