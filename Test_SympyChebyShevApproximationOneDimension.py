import Library_SympyChebyChevApproximationOneDimension
import Library_TestLooper

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "SympyExpression": None, 
            "DomainMinimumPoint": None, 
            "DomainMaximumPoint": None, 
            "ApproximationOrder": None
        }
        , 
        []
    )
)



LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_SympyChebyChevApproximationOneDimension.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    MaxFlatResultLength = None,
    ResultOrderMatters = True, 
    PrintExtra = True,
)

































