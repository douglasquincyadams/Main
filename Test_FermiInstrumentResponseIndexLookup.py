
import Library_TestLooper




import Library_FermiInstrumentResponseIndexLookup

#       Indexes:
#      0,1,2,3,4,5
Los = [1,2,3,4,5,6]
His = [2,3,4,5,6,7]


ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
            "Value"  : 3.5           , 
            "Los"   : Los       ,
            "His"  : His       ,
        }
        , 
        [  2 ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "Value"  : 1.5           , 
            "Los"   : Los       ,
            "His"  : His       ,
        }
        , 
        [  0 ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "Value"  : -2           , 
            "Los"   : Los       ,
            "His"  : His       ,
        }
        , 
        [  0 ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "Value"  : 8           , 
            "Los"   : Los       ,
            "His"  : His       ,
        }
        , 
        [  5 ]
    )
)

LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_FermiInstrumentResponseIndexLookup.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = None,
    HardDifferenceMax = 0.1,
    PrintExtra = False,
)












