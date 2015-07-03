"""
SOURCE:


DESCRIPTION:
    Checks to see if a function is of type `Type_ModelFunction`
    
    For a function to be a `Type_ModelFunction` it has exactly 2 arguments:
        Argument1)
            must have name `DataPoint`
            needs to correspond to some `DataPoint`
            could be any number of dimensions
            needs to accept argument of `Type_NumpyTwoDimensionalDataPoint` (!=`Type_NumpyTwoDimensionalDataset`)
        Argument2)
            must have name `Parameters`
            needs to correspond to some `Parameters`
            could be any number of parameters in the model
            needs to accept argument in the form of a python Tuple


ARGS:


RETURNS:


TESTS:
    Test_ModelFunction

"""

import inspect

def Main(
    ModelFunctionCadidate = None,
    PrintExtra = False,
    CheckArguments = True,
    ):

    #Cannot be None    
    if (ModelFunctionCadidate == None):
        if (PrintExtra):
            print '(ModelFunctionCadidate == None)'
        return False

    #Must be a function:
    if (not inspect.isfunction(ModelFunctionCadidate)): 
        if (PrintExtra):
            print '(not inspect.isfunction(ModelFunctionCadidate))'
        return False


    #Must have args with expected names:
    ArgSpec = inspect.getargspec(ModelFunctionCadidate)
    ArgNames = ArgSpec.args
    #print 'Args', Args
    if ( ArgNames[0] != 'DataPoint'):
        if (PrintExtra):
            print "( ArgNames[0] != 'DataPoint')"
        return False


    if ( ArgNames[1] != 'Parameters'):
        if (PrintExtra):
            print "( ArgNames[1] != 'Parameters')"
        return False
    #Defaults = ArgSpec.defaults
    #print 'Defaults', Defaults

    #ModelFunctionCandidateMembers = inspect.getmembers(ModelFunctionCadidate, predicate = inspect.iscode )
    #print 'ModelFunctionCandidateMembers', ModelFunctionCandidateMembers


    return True




















