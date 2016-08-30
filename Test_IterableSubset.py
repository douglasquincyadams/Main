import Library_IterableSubset
import Library_TestLooper

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "IterableSubsetCandidate": [1,2,3], 
            "IterableParentCandidate": [1,2,3,4]
        }
        , 
        True
    )
)
ArgSetExpectedResultCombos.append(
    (
        
        {
            "IterableSubsetCandidate": [5,4], 
            "IterableParentCandidate": [1,2,3,4]
        }
        , 
        False
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "IterableSubsetCandidate": [1,4], 
            "IterableParentCandidate": [1,2,3,4]
        }
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "IterableSubsetCandidate": [[1,2],4], 
            "IterableParentCandidate": [[1,2],2,3,4]
        }
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "IterableSubsetCandidate": [['asdf0','asdf1'],4], 
            "IterableParentCandidate": [['asdf0','asdf1'],2,3,4]
        }
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        
        {
            "IterableSubsetCandidate": [['asdf0','asdf2'],4], 
            "IterableParentCandidate": [['asdf0','asdf1'],2,3,4]
        }
        , 
        False
    )
)




LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_IterableSubset.Main,
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

































