"""
SOURCE:
    http://stackoverflow.com/questions/6527633/how-can-i-make-a-deepcopy-of-a-function-in-python

    **Cannot find the official documentation for `types.FunctionType` 
        Must have named arguments somehwere, and cannot find with google

DESCRIPTION:
    Makes a deep copy of a function in python


    return a function with same code, globals, defaults, closure, and 
    name (or provide a new name)


    #STILL DOES NOT TRUELY DEEP COPY A FUNCTION 
    #   -> THE DEFAULT ARGS DON'T GET COPIED OVER
    #   -> THEY REMAIN REFERENCES/POINTERS

ARGS:
    Function
        The function to copy
    NewName
        The new name for the function's copy
    NewDefaults
        Description:
            New default values for the function arguments
            This enables copying some data to private scope for the new function copy
                Especially useful in parallel processing
        type  
            python `None`
            OR 
            python `tuple`
            OR 
            `Type_HashTable` allowed if `CheckArguments==True` 



RETURNS:
    FunctionCopy


"""
import types
import copy
import pprint
import inspect
import Type_HashTable

def Main(
    Function = None, 
    NewName = None,
    NewDefaults = None, 
    CheckArguments = True,
    PrintExtra = False
    ):

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (type(NewDefaults) == type(None)):
            pass

        elif ( type(NewDefaults) is tuple):
            pass

        elif( Type_HashTable.Main(NewDefaults) ):
            #Cast the dictionary values into a tuple
            FunctionArgumentInformation = inspect.getargspec(Function)       

            FunctionArgumentNamesInOrder = FunctionArgumentInformation.args
            if (PrintExtra):
                print 'FunctionArgumentNamesInOrder', FunctionArgumentNamesInOrder
           
            #TODO: Hybridizaion of any partial NewDefaults, with the original function defaults 
            #FunctionDefaultValues = FunctionArgumentInformation.defaults #Tuple starts from the first Named Argument 
            #print 'FunctionDefaultValues', FunctionDefaultValues

            #Generate a list of new default values in order:
            NewDefaultsValueList = []
            for FunctionArgumentName in FunctionArgumentNamesInOrder:
                NewDefaultsValueList.append(NewDefaults[FunctionArgumentName])
    
            NewDefaults = copy.deepcopy( tuple(NewDefaultsValueList) )
            if (PrintExtra):
                print 'NewDefaults', NewDefaults

            #TODO: We will ignore **kwards, and *args for now
            #FunctionSpecialArgsName = FunctionArgumentNamesInOrder[1] 
            #print 'FunctionSpecialArgsName', FunctionSpecialArgsName
            #FunctionSpecialKwarsName = FunctionArgumentNamesInOrder[2]
            #print 'FunctionSpecialKwarsName', FunctionSpecialKwarsName

        else:
            ArgumentErrorMessage += 'NewDefaults must be of type `None`, `tuple`, or `Type_HashTable`'

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage

            raise Exception(ArgumentErrorMessage)

    if (PrintExtra):
        #All function property information:
        
        FunctionProperties = dir(Function)
        print 'FunctionProperties'
        pprint.pprint(FunctionProperties)

    #Create a new function by invoking the python function `types.FunctionType`
    #   Documentation for this function is thus unfound
    #   TODO: Find the documentation for this
    FunctionCopy = types.FunctionType(
        Function.__code__, 
        Function.__globals__, 
        copy.deepcopy(NewName) or Function.__name__,
        NewDefaults or Function.__defaults__ , 
        Function.__closure__
        )

    # in case Function was given attrs 
    #   Note: 
    #       * The original version of this dict copy was a shallow copy):
    #       * It is unknown if using the copy.deepcopy method fixes this to be a true deep copy
    #   TODO: find out the deep copy `Goodness` of this line of code
    FunctionCopy.__dict__.update(copy.deepcopy( Function.__dict__) ) 

    return FunctionCopy























