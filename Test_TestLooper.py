


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


#Define a fake library method on which to test the looper 
#   (This would be the content of a library usualy)
def ExampleFunction2(
    Alpha = [],
    Beta = ()
    ):

    ResultSet = set()

    for BetaElement in Beta:
        ResultSet.add( tuple( Alpha + [BetaElement] )  )

    return ResultSet

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

ArgSetExpectedResultCombos.append(
    (
        {
            "Alpha"  : 4           , 
            "Beta"   : ""       ,
            "Delta"  : ""       ,
        }
        , 
        Exception('')
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "Alpha"  : 4           , 
            "Beta"   : ""       ,
            "Delta"  : ""       ,
        }
        , 
        4
    )
)



ArgSetExpectedResultCombos2 = []
ArgSetExpectedResultCombos2.append(
    (
        {
            "Alpha"  : [12,13]           , 
            "Beta"   : (1,2)      ,
        }
        , 
        [ (12,13,2),  (12,13,1) ]
    )
)



#Run the loop on the arg combo's, and make sure that we get the results we expect:
#   This is code which is extremely useful for example
#   Copy and paste the loop in the below section
#-----------------------------------------
#           COPY SECTION:
#-----------------------------------------
print 'BEGINING LOOP1'
LoopResult = Library_TestLooper.Main(
    FunctionToTest = ExampleFunction,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    PrintExtra = True,
)

#-----------------------------------------
print 'BEGINING LOOP2'
LoopResult2 = Library_TestLooper.Main(
    FunctionToTest = ExampleFunction2,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos2,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    PrintExtra = True,
)
#-----------------------------------------
#TODO: Add another section which tests the 'MinFlatResultLength' arg


#TODO: Add another section which tests the 'ResultOrderMatters' arg



print 'LOOP RESULT CHECKING:'
#Check the results of the loop run against what we expected:
print 'LoopResult', LoopResult
ExpectedLoopResult = [True, True, False, True, True, False]
print 'ExpectedLoopResult', ExpectedLoopResult



#Check the results of the loop run against what we expected:
print 'LoopResult2', LoopResult2
ExpectedLoopResult2 = [True]
print 'ExpectedLoopResult2', ExpectedLoopResult2





if (
        LoopResult == ExpectedLoopResult 
    and LoopResult2 == ExpectedLoopResult2
    ):
    pass
else:
    FullTestSuccess = False



Library_PrintFullTestSuccess.Main(FullTestSuccess)












