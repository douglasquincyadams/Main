import Library_GenerateGloballyUniqueId
import Library_TestLooper


AllResults = []
for x in range(100):
    SingleResult = Library_GenerateGloballyUniqueId.Main()
    assert ( not (SingleResult in AllResults) )
    AllResults.append(SingleResult)

print AllResults


#TODO -> use a parallel for loop with this to assert that multiprocessing won't break this

"""
ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "DummyArg": None
        }
        , 
        
    )
)



LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_GenerateGloballyUniqueId.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    MaxFlatResultLength = None,
    ResultOrderMatters = True, 
    EqualityCheckFunction = None,
    PrintExtra = True,
)

"""































