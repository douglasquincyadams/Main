"""
SOURCE:
    None

DESCRIPTION:

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

    LibraryName
        the library to check if it exists

RETURNS:

"""
import Library_FilePathExists
def Main( 
    LibraryName = None ,
    ):

    FilePath = LibraryName + '.py'

    LibraryExists = Library_FilePathExists.Main(FilePath)

    return LibraryExists
