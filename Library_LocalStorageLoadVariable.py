
"""

DESCRIPTION:
    loads a stored variable from a file

ARGS:
    VariableName
        type: python string
        description: the name of the variable of which to load

    StorageFileDirectory
        type: python string
        description: the directory of which the variable file is located


RETURNS:
    Variable:
        type: any python type - should match the type of the varible which was stored
        description: whatever was stored in the first place

        `None` on failure to load variable

"""

import pickle
import Const_LocalStorageTemp


def Main(
    VariableName = None,
    StorageFileDirectory = Const_LocalStorageTemp.Directory,
    ):

    Variable = None
    try:
        StorageFilePath = StorageFileDirectory + VariableName + '.txt'
        Variable = pickle.load(open( StorageFilePath, "r" ))
    except:
        pass

    return Variable
    
