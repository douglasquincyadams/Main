


#Cannot test the test looper with the test looper -> oh the irony...
import Library_TestLooper
import Library_PrintFullTestSuccess


FullTestSuccess = True


#Define a fake library method on which to test the looper 
#   (This would be the content of a library usualy)
def ExampleFunction(
    Alpha = [],
    Beta = "",
    Delta = None,
    ):
    print ' ExampleFunction Started'
    print '  Alpha', Alpha
    print '  Beta', Beta
    print '  Delta', Delta

    return Alpha + [len(Beta) , len(Delta)]


#Define the arguement result combinations -> 
#   This is code which is extremely useful for example
#   Copy and paste the first  combo into new test files


#-----------------------------------------
#           COPY SECTION:
#-----------------------------------------
ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
            "Alpha"  : [12,13]           , 
            "Beta"   : "Yo Dawg  "       ,
            "Delta"  : "CoolBeens"       ,
        }
        , 
        [   12 , 13 , 9 , 9 ]
    )
)
#-----------------------------------------




ArgSetExpectedResultCombos.append(
    (
        {
            "Alpha"  : [12,13]           , 
            "Beta"   : "Yo Dawg  "       ,
            "Delta"  : "CoolBeens"       ,
        }
        , 
        [   12 , 13 , 9 , 9.9 ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "Alpha"  : [12,13]           , 
            "Beta"   : "Yo Dawg  "       ,
            "Delta"  : "CoolBeens"       ,
        }
        , 
        [   12 , 13 , 9 , 7.9 ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "Alpha"  : []           , 
            "Beta"   : ""       ,
            "Delta"  : ""       ,
        }
        , 
        [   0,0 ]
    )
)


#Run the loop on the arg combo's, and make sure that we get the results we expect:
#   This is code which is extremely useful for example
#   Copy and paste the loop in the below section
#-----------------------------------------
#           COPY SECTION:
#-----------------------------------------
LoopResult = Library_TestLooper.Main(
    FunctionToTest = ExampleFunction,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    PrintExtra = False,
)
#-----------------------------------------



#Check the results of the loop run against what we expected:
print 'LoopResult', LoopResult
ExpectedLoopResult = [True, True, False, True]
print 'ExpectedLoopResult', ExpectedLoopResult
if (LoopResult == ExpectedLoopResult):

    print 'Single Test Success'
else:
    print 'Single Test Failure'
    FullTestSuccess = False
Library_PrintFullTestSuccess.Main(FullTestSuccess)
















