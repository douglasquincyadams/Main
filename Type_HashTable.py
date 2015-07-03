
"""
SOURCE:

    http://stackoverflow.com/questions/25231989/how-to-check-if-a-variable-is-a-dictionary-in-python


DESCRIPTION:

    This implements what is known as a 
        `Duck typing`

    Does it quack?
    Does it look like a duck?

        
ARGS:
    HashTableCandidate
        Description:
            The object of which to check if it is an HashTable python object
            Examples of hashtable python objects are:
                Dictionary
                Collections.<sooooooo many things>
                JSON object
                etc..

RETURNS:
    True if HashTable
    False if NOT HashTable


"""

def Main(
    HashTableCandidate = None,
    PrintExtra = False,
    CheckArguments = True,
    ):
    

    
    try:
        keys = HashTableCandidate.keys()
        #print 'keys', keys
        firstKey = keys[0]
        #print 'firstKey', firstKey
        firstValue = HashTableCandidate[firstKey]
        #print 'firstValue', firstValue
        Result = True
    except:
        Result = False


    return Result






























