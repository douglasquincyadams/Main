"""
DESCRIPTION:
    Gets the last extension from a filename

    Pulls the last stuff after a '.' in the filename

    If there is no . in the file name, then None is returned

ARGS:
    FileName
        type:
            python string
        descriptin
            some name of a file
    

RETURNS:

    Result
        Type:
            String or None
        Description:
            Returns the extension, or None if an extension does not exist

"""



def Main(
    FileName = None,
    PrintExtra = False,
    ):

    FileNamePieces = FileName.split(".")
    if (PrintExtra):
        print 'FileNamePieces', FileNamePieces
    NumFileNamePieces = len(FileNamePieces)
    Result = None
    if (NumFileNamePieces > 1):
        Result = FileNamePieces[-1]

    return Result
    
    

