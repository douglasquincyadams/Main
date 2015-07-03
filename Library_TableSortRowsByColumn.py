



def Main(
    Table = None, 
    ColumnIndex = None,
    ):
	SortedTable = sorted(Table, key = lambda row: row[ColumnIndex])

	return SortedTable
