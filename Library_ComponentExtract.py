"""

DESCRIPTION:
    Trys to get a value from a python object by index
    On failure returns default value provided, or none

ARGS:

RETURNS:

"""

def Main(
    Object = None, 
    Key = None, 
    DefaultValue = None,
    CheckArguments = True,
    PrintExtra = False,
    ):

    if (CheckArguments):
        ArgumentErrorMessage = ""
        if (Object == None):
            ArgumentErrorMessage += "(Object == None)\n"
        if (Key == None):
            ArgumentErrorMessage += "(Key == None)\n"

        #if (DefaultValue == None):
        #    ArgumentErrorMessage += "(DefaultValue == None)\n"

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    Result = DefaultValue

    try:
        Result = Object[Key]
    except:
        pass
    return Result
