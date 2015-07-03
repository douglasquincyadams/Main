"""
DESCRIPTION:

ARGS:
    hdulist[k]
    TYPE: http://docs.astropy.org/en/v0.3/io/fits/index.html


RETURNS:
    NONE

"""
import numpy
import pprint
#------------------------------------------------------------------------------
import Library_AstropyFitsCardsPrettyPrint


def Main(FitsTable = None, TableName = "", PrintLines = False):

    #COLUMNS:
    print '\n' + TableName + ' Column Information: '

    TableColumns = None
    TableColumnNames = None
    try:
        TableColumns = FitsTable.columns  
        TableColumnNames = FitsTable.columns.names
        #TableColumnUnits = FitsTable.columns.unit#info(attrib='unit')
    except:
        pass

    if (TableColumns == None):
        print "No Column Information"
    else:
        print TableName + '.columns'
        pprint.pprint( TableColumns )
        print TableName + '.columns.names'
        pprint.pprint( TableColumnNames )
        #print TableName + ".columns.info(attrib='unit')"


    #HEADER:
    print '\n' + TableName + ' Header Information: '
    TableHeader = FitsTable.header
    TableCards = TableHeader.cards
    Library_AstropyFitsCardsPrettyPrint.Main(CardList = TableCards, Names = TableColumnNames)
    

    #DATA:
    print '\n' + TableName + ' Data   Information: '
    
    TableData = FitsTable.data
    
    if (TableData == None):
        print 'No Table Data'
    else:
        TableDataLength = len(TableData)
        TableRowLength = len(TableData[0])
        FirstRow = TableData[0]

        print 'len('+TableName+'.data)' , TableDataLength
        print 'len('+TableName+'.data[0])', TableRowLength 
        print TableName +'.data[0]', FirstRow

        if (PrintLines):
            for Line in TableData:
                print Line

    return None












