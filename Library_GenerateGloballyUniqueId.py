"""
SOURCE:
    http://stackoverflow.com/questions/159137/getting-mac-address
    http://stackoverflow.com/questions/11200636/how-to-read-dev-random-in-python
    https://docs.python.org/3/library/os.html#os.urandom
DESCRIPTION:
    Generates a unique id
    Regardless of 
        which machine
        how many processes
        all running at the same time
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
    DummyArg
        Type:
            <type 'NoneType'>
        Description:
RETURNS:
    Result
        Type:
        Description:
"""
import Library_DateStringNowGMT
import uuid 
import os

def Main(
    DummyArg= None,
    CheckArguments = True,
    PrintExtra = False,
    ):

    Result = None

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)


    DateStringNow = Library_DateStringNowGMT.Main()
    if PrintExtra: print 'DateStringNow', DateStringNow

    ProcessId = str(os.getpid())
    if PrintExtra: print 'ProcessId', ProcessId

    MacAddress = str( uuid.getnode() )
    if PrintExtra: print 'MacAddress', MacAddress

    UnixRandom = os.urandom(10)
    UnixRandomByteList = ( list(map(ord, UnixRandom)) )
    UnixRandomIntegerSum = str( sum(UnixRandomByteList) )
    if PrintExtra: print 'UnixRandomIntegerSum', UnixRandomIntegerSum

    UniqueId = '' 
    UniqueId += DateStringNow + '_' 
    UniqueId += ProcessId + '_' 
    UniqueId += MacAddress + '_' 
    UniqueId += UnixRandomIntegerSum 
    
    Result = UniqueId
    return Result 




