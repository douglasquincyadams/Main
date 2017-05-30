
"""
DESCRIPTION:
    Saves a variable for later after a program is terminated (writes it to a file)

ARGS:

    Variable
        type: ANY python variable
        description: anything

    VariableName
        type: python string
        description: the name of the variable of which to save

    StorageFileDirectory
        type: python string
        description: the directory of which the variable file is located

    Overwrite:
        type: python boolean
        description:
            deterimines if an existing variable can be overwritten with the same name
        default: False
            This is the safe defensive way to implement such a method
RETURNS:

    True on success
    False OR throws error on failure

"""
import os
#------------------------------------------------------------------------------
import pickle
import Const_LocalStorageTemp

def Main(
    Variable = None,
    VariableName = None,
    StorageFileDirectory = Const_LocalStorageTemp.Directory,
    Overwrite = False,
    ):

    StorageFilePath = StorageFileDirectory + VariableName + '.txt'

    OpenType = 'w'

    if (Overwrite == False):
        FileExists = os.path.isfile(StorageFilePath)
        if (FileExists):
            return False

    pickle.dump(Variable, open( StorageFilePath, OpenType ))

    return True







