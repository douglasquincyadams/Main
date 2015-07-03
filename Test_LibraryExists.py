import Library_LibraryExists
import Library_TestLooper


ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
            "LibraryName"  : 'Library_LibraryExists'           , 
        }
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "LibraryName"  : 'SomethingWonky'           , 
        }
        , 
        False
    )
)

LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_LibraryExists.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    HardDifferenceMax = 0.0,
    PrintExtra = False,
)






























