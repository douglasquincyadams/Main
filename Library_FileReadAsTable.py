"""
DESCRIPTION:
    Opens a file and returns a python list of lists where
    ValueFromTable = Table[ Line # ][ Column # ]

ARGS:
    Filepath
        The filepath to open 
    Delimeter   
        The character on which to split lines

RETURNS:
    python 2d array
        NOT a numpy array 
        Native list of lists

TESTS:
    None
"""
def Main(\
    Filepath = None,\
    Delimeter = None,\
    FilterNone = False,\
    ):

    if (Delimeter == None):
        Delimeter = ","

    Table = []
    with open(Filepath, 'r') as File:
        for line in File:
            #print line
            NewLine = None
            if (FilterNone):
                NewLine = filter(None, line.replace("\n", "").split(Delimeter))
            else:
                NewLine = line.replace("\n", "").split(Delimeter)
            Table.append( NewLine )
	
    return Table
































