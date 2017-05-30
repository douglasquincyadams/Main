
import Library_CopyFunction



"""
    Generates an assertion error on failure
    Returns nothing on success
"""
def Test0():
    print '\n\nStarting Test0\n'
    from logging import getLogger as _getLogger # pyflakes:ignore, must copy
    getLogger = Library_CopyFunction.Main(_getLogger)
    getLogger.__doc__ += '\n    This function is from the Std Lib logging module.\n    '
    assert getLogger.__doc__ is not _getLogger.__doc__
    assert getLogger.__doc__ != _getLogger.__doc__
    assert getLogger.__doc__ != _getLogger.__doc__
    print '  Test0 Success'


def Test1():
    print '\n\nStarting Test1\n'

    def ExampleFunction( OnlyArg = 10):
        return OnlyArg    

    def FunctionWithWantedDefaults(OnlyArg = 20):
        return None
    


    ExampleFunctionCopyDefaults = FunctionWithWantedDefaults.__defaults__
    print 'str(type(ExampleFunctionCopyDefaults))', str(type(ExampleFunctionCopyDefaults))

    print 'ExampleFunctionCopyDefaults'
    print str(ExampleFunctionCopyDefaults)


    ExampleFunctionCopy = Library_CopyFunction.Main( 
        Function = ExampleFunction, 
        NewName = 'ExampleFunctionCopy',
        NewDefaults = ExampleFunctionCopyDefaults 
        )


    #Destroy the original references
    ExampleFunction = lambda :  'ExampleFunctionReplacement'


    #Invoke the copy
    SingleFunctionCopyResult = ExampleFunctionCopy()
    print 'SingleFunctionCopyResult', SingleFunctionCopyResult

    assert( SingleFunctionCopyResult == 20 )
    print '  Test1 Success'

def Test2():
    print '\n\nStarting Test2\n'

    def ExampleFunction( FirstArg, SecondArg = 10):
        return FirstArg + SecondArg    

    ExampleFunctionCopyDefaults = {'FirstArg': 10, 'SecondArg' : 20}
    print 'str(type(ExampleFunctionCopyDefaults))', str(type(ExampleFunctionCopyDefaults))

    print 'ExampleFunctionCopyDefaults'
    print str(ExampleFunctionCopyDefaults)


    ExampleFunctionCopy = Library_CopyFunction.Main( 
        Function = ExampleFunction, 
        NewName = 'ExampleFunctionCopy',
        NewDefaults = ExampleFunctionCopyDefaults 
        )


    #Destroy the original references
    ExampleFunction = lambda :  'ExampleFunctionReplacement'


    #Invoke the copy
    SingleFunctionCopyResult = ExampleFunctionCopy()
    print 'SingleFunctionCopyResult', SingleFunctionCopyResult

    assert( SingleFunctionCopyResult == 30 )
    print '  Test2 Success'

def Test3():
    print '\n\nStarting Test3\n'

    def ExampleFunction( FirstArg, SecondArg = 10):
        return FirstArg + SecondArg    

    ExampleFunctionCopyDefaults = {'FirstArg': 10, 'ThirdArg' : 30} #We added a new arg, and plan to keep an old one
    print 'str(type(ExampleFunctionCopyDefaults))', str(type(ExampleFunctionCopyDefaults))

    print 'ExampleFunctionCopyDefaults'
    print str(ExampleFunctionCopyDefaults)


    ExampleFunctionCopy = Library_CopyFunction.Main( 
        Function = ExampleFunction, 
        NewName = 'ExampleFunctionCopy',
        NewDefaults = ExampleFunctionCopyDefaults 
        )


    #Destroy the original references
    ExampleFunction = lambda :  'ExampleFunctionReplacement'


    #Invoke the copy
    SingleFunctionCopyResult = ExampleFunctionCopy()
    print 'SingleFunctionCopyResult', SingleFunctionCopyResult

    assert( SingleFunctionCopyResult == 20 )
    print '  Test3 Success'


def Test4():
    print '\n\nStarting Test4\n'

    def ExampleFunction( FirstArg, SecondArg = 10):
        return FirstArg + SecondArg    

    ExampleFunctionCopyDefaults = {'FirstArg': 10,  'ThirdArg' : 30, 'SecondArg' :10} #We added a new arg, and plan to keep an old one
    print 'str(type(ExampleFunctionCopyDefaults))', str(type(ExampleFunctionCopyDefaults))

    print 'ExampleFunctionCopyDefaults'
    print str(ExampleFunctionCopyDefaults)


    ExampleFunctionCopy = Library_CopyFunction.Main( 
        Function = ExampleFunction, 
        NewName = 'ExampleFunctionCopy',
        NewDefaults = ExampleFunctionCopyDefaults 
        )


    #Destroy the original references
    ExampleFunction = lambda :  'ExampleFunctionReplacement'


    #Invoke the copy
    SingleFunctionCopyResult = ExampleFunctionCopy()
    print 'SingleFunctionCopyResult', SingleFunctionCopyResult

    assert( SingleFunctionCopyResult == 20 )
    print '  Test4 Success'


Test0()

Test1()

Test2()

Test3()

Test4()
print '\n\n'
print 'Full Test Success'
print '\n\n'







