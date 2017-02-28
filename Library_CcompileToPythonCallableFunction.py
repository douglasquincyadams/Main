"""
SOURCE:
    http://stackoverflow.com/questions/7109964/creating-your-own-header-file-in-c
    https://cffi.readthedocs.io/en/latest/overview.html
    http://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
    http://stackoverflow.com/questions/6418807/how-to-work-with-complex-numbers-in-c
DESCRIPTION:
    Takes the C source which is required in order to
        define a function header
        define a function source
    Compiles the C into a python importable module
        the compiled module is obfuscated from the invoker
        the compiled module is therefore named using a UniqueID
        the compiled module UniqueID does NOT need to be retrievable
    Returns a python Handle ontop of the module
        The python handle is given an attribute storing the unique ID just in case
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
    CfunctionHeader
        Type:
            <type 'NoneType'>
        Description:
    CfunctionSource
        Type:
            <type 'NoneType'>
        Description:
RETURNS:
    Result
        Type:
        Description:
"""
import os
import cffi
import imp
import Const_CodeBaseCompiled
import Library_GenerateGloballyUniqueId
import Library_SystemDirectoryCreateSafe
def Main(
    CfunctionHeader= None,
    CfunctionSource= None,
    CfunctionName = None,
    CheckArguments = True,
    PrintExtra = False,
    ):


    if CfunctionName is None:
        CfunctionName = 'Main'

    Result = None

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)


    print 'CfunctionSource', CfunctionSource

    #Location
    CodeBaseCompiledDirectory = os.path.realpath( Const_CodeBaseCompiled.LocalCodeTargetDirectory )
    Library_SystemDirectoryCreateSafe.Main( Directory = CodeBaseCompiledDirectory )

    #Generate a Name
    UniqueId = Library_GenerateGloballyUniqueId.Main( )
    CompiledModuleName = 'TempModule' + '_' + UniqueId

    #Build and compile source
    ffibuilder = None
    ffibuilder = cffi.FFI()
    ffibuilder.cdef(CfunctionHeader)
    ffibuilder.set_source(
        CompiledModuleName,
        CfunctionSource
        )
    ffibuilder.compile(tmpdir = CodeBaseCompiledDirectory, verbose=True)

    #Import the compiled build:
    CompiledModuleFileName = CompiledModuleName + '.so'
    CompiledModuleFilePath = CodeBaseCompiledDirectory + '/' + CompiledModuleFileName
    print 'CompiledModuleFilePath', CompiledModuleFilePath
    CompiledModuleDescriptionObject =  ('.so', 'rb', imp.C_EXTENSION)

    ModuleObject = None
    ModuleObject = imp.load_module(
        CompiledModuleName, 
        None,  #If path is provided, then this arg is no required
        CompiledModuleFilePath, 
        CompiledModuleDescriptionObject
        )


    #Return the function of interest:
    Result = getattr( ModuleObject.lib, CfunctionName)

    #setattr(Result, 'UniqueId', UniqueId)
    #Result.CompiledModuleName = CompiledModuleName

    return Result 






















