import pprint

#------------------------------------------------------------------------------
import Library_ComponentExtract
import Library_PrintFullTestSuccess
import Library_OrderOfMagnitudeRatio


FullTestSuccess = True

ExampleDictionary = {"a": "aval", "b": "bval"}



ArgSetExpectedResultCombos = []
ArgSet1 = {
"Object"            : ExampleDictionary ,
"Key"               : "a"               ,
"DefaultValue"      : None              ,
}

ExpectedResult1 = "aval"
ArgSetExpectedResultCombos.append( (ArgSet1, ExpectedResult1) )

ArgSet2 = {
"Object"            : ExampleDictionary ,
"Key"               : "b"               ,
"DefaultValue"      : None              ,
}

ExpectedResult2 = "bval"
ArgSetExpectedResultCombos.append( (ArgSet2, ExpectedResult2) )



ArgSet3 = {
"Object"            : ExampleDictionary ,
"Key"               : "c"               ,
"DefaultValue"      : None              ,
}
ExpectedResult3 = None
ArgSetExpectedResultCombos.append( (ArgSet3, ExpectedResult3) )

ArgSet4 = {
"Object"            : ExampleDictionary ,
"Key"               : "c"               ,
"DefaultValue"      : "Cdefault"              ,
}
ExpectedResult4 = "Cdefault" 
ArgSetExpectedResultCombos.append( (ArgSet4, ExpectedResult4) )



k = 0
for ArgSet, ExpectedResult in ArgSetExpectedResultCombos:
    print "Running Test ", k

    Result = Library_ComponentExtract.Main(
        Object          = ArgSet["Object"],
        Key             = ArgSet["Key"],
        DefaultValue    = ArgSet["DefaultValue"],
    )

    print ' ArgSet:'
    pprint.pprint( ArgSet )

    print ' Result          ', Result  
    print ' ExpectedResult  ', ExpectedResult


    if ( Result ==  ExpectedResult ):
        print " Single Test Success"
    else:

        print " Single Test Failure"
        FullTestSuccess = False

    k += 1

Library_PrintFullTestSuccess.Main(FullTestSuccess)




















