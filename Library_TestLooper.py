"""
SOURCES:
    http://stackoverflow.com/questions/3394835/args-and-kwargs

        >>> def print_three_things(a, b, c):
        ...     print 'a = {0}, b = {1}, c = {2}'.format(a,b,c)
        ...
        >>> mylist = ['aardvark', 'baboon', 'cat']
        >>> print_three_things(*mylist)
        a = aardvark, b = baboon, c = cat

DESCRIPTION:
    Allows for saving time when writing tests, by
        doing the loop, 
        keeping track of the test success,
        checking results against expected results
        Passing in the args contained within the  `ArgSetExpectedResultCombos`
    

ARGS:
    FunctionToTest
        Type: Python (Method / function / routine)
        Description:
        

    ArgSetExpectedResultCombos
        Description:
            Structure containing all the args with which to pass into the `FunctionToTest`

    OrderOfMagnitudeRatioMax
        Type: Python Float
        Description:
            Maximum distance between any expected result and the actual result of the function

    HardDifferenceMax:
        Type: Python Float
        Description:
            Maximum absolute distance between any expected result and the actual result of the function

RETURNS:
    TestSuccesses
        Type: Python List
        Description:
            Each value corresponds to a test success result
            If all the tests succeed expect to return 
                [True, True, .... True]
            If only the 4th test fails, expect to return 
                [True, True, True, False, True, ... True]

"""


import numpy
import pprint
import collections
import traceback
#------------------------------------------------------------------------------
import Library_OrderOfMagnitudeRatioSmallCheck
import Library_ComponentExtract
import Library_PrintFullTestSuccess
import Library_HardDifferenceSmallCheck


def Main(
    FunctionToTest = None,
    ArgSetExpectedResultCombos = None,
    ResultOrderMatters = True, #must be an arrray for this to make sense
    OrderOfMagnitudeRatioMax = None,
    HardDifferenceMax = .01,
    CheckArguments = True,
    PrintExtra = True,
    ):

    FullTestSuccess = True

    if( CheckArguments):
        ArgumentErrorMessage = ""

        #If any errors - terminate
        if ( len( ArgumentErrorMessage ) ):
            raise Exception( ArgumentErrorMessage)

    TestSuccesses = []

    k = 0
    for ArgSet, ExpectedResult in ArgSetExpectedResultCombos:
        print "Running Test ", k

        try:

            if (PrintExtra):
                print ' ArgSet:'
                items = ArgSet.items()
                items.sort()
                pprint.pprint( items, indent=4)
                print ''

            Result = FunctionToTest(
                **ArgSet #*ArgSet #**kwargs python wizzardry -> unpacks the ArgSet as named args into the function call
            )
            
            #TODO: More type case casting:
            if (type(ExpectedResult) == type({})):
                if (PrintExtra):
                    print ' Type Dictionary encountered -> converting Results to sorted by key names arrays'
                Result = [value for (key, value) in sorted(Result.items())]
                ExpectedResult = [value for (key, value) in sorted(ExpectedResult.items())]
                #Result = Result.values()
                #ExpectedResult = ExpectedResult.values()

            if ( ResultOrderMatters == False):
                Result = numpy.sort(numpy.array(Result), axis = 0)
                ExpectedResult = numpy.sort(numpy.array(ExpectedResult),  axis = 0)

            if (PrintExtra):
                print ' Result          '
                pprint.pprint( Result )
                print ''
                print ' ExpectedResult  '
                pprint.pprint( ExpectedResult )
                print ''

            OrderOfMagnitudeRatioSmallCheckResult = True
            if ( OrderOfMagnitudeRatioMax != None ):
                OrderOfMagnitudeRatioSmallCheckResult = \
                    Library_OrderOfMagnitudeRatioSmallCheck.Main( 
                        Result , 
                        ExpectedResult, 
                        OrderOfMagnitudeRatioMax)

            HardDifferenceSmallCheckResult = True
            if (HardDifferenceMax != None)    :
                HardDifferenceSmallCheckResult = \
                    Library_HardDifferenceSmallCheck.Main(        
                        Result, 
                        ExpectedResult, 
                        HardDifferenceMax) 

            if (PrintExtra):
                print ' OrderOfMagnitudeRatioSmallCheckResult', OrderOfMagnitudeRatioSmallCheckResult
                print ''
                print ' HardDifferenceSmallCheckResult', HardDifferenceSmallCheckResult
                print ''

            if ( OrderOfMagnitudeRatioSmallCheckResult and HardDifferenceSmallCheckResult):
                print ' Single Test Success'
                TestSuccesses.append(True)
                print ''
            else:
                print ' ArgSet:'
                pprint.pprint( ArgSet )
                print ' Result:'
                pprint.pprint( Result  )
                print ' ExpectedResult:'
                pprint.pprint( ExpectedResult )
                print ''
                print '                 !!!                     !!!'
                print '                     Single Test Failure'
                print '                 !!!                     !!!'
                print ''
                FullTestSuccess = False
                TestSuccesses.append(False)

        except Exception as E:
            print ' Exception In attempt'
            print str(E)
            traceback.print_exc()
            FullTestSuccess = False

        print ' '
        k += 1

    if (PrintExtra):
        Library_PrintFullTestSuccess.Main(FullTestSuccess)


    return TestSuccesses








