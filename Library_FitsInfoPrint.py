"""
DESCRIPTION:
    Takes an arbitrary fits file and prints useful infomation about the file


ARGS:
    FitsFilePath:
        Type: String
        Description: the file path on the local machine of where the fits file is located.
            This is the file for which information will be printed.


RETURNS

"""
import astropy
import astropy.io
import astropy.io.fits
import numpy
#------------------------------------------------------------------------------

import Library_AstropyFitsCardsPrettyPrint


def Main(FitsFilePath):
    HDUList = astropy.io.fits.open(FitsFilePath)

    print '\n\n\n=======FITS FILE DETAILS:======\n\n\n'
    #Get the first bit of default information using pyfits:

    HDUList.info()

    NumTables = len(HDUList)
    print 'NumTables', NumTables


    #Get more detailed information (useful for parsing choices):
    TableNumber = 0
    for Table in HDUList:
        print 'TableNumber  ', TableNumber 

        #Get the table column names
        try:
            TableColumns = Table.columns
            print ' TableColumns'
            print TableColumns
        except Exception as E:
            print " Exception In Printing Table Columns: \n"
            print ' ' + str(E)

        #Get more detailed informatoin about each column (including a description)
        try:
            #Library_AstropyFitsCardsPrettyPrint.Main(Table.header)
            #for element in Table.header:
            #    print element
            pass
        except Exception as E:
            print " Exception In Printing Table Header Details: \n"
            print ' ' + str(E)

        TableNumber += 1

    return None #Only does printing -> does not return information

