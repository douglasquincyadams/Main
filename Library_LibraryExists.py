
"""
DESCRIPTION:

CHECKS IF A LIBRARY EXISTS:
"""

def Main( 
    LibraryName = None ,
    ):

    LibraryExists = False
    try:
        LibraryReadHandle = open(LibraryName + '.py', 'r')
        LibraryExists = True
    except:
        LibraryExists = False

    return LibraryExists
