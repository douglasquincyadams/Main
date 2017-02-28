import Library_SystemDirectoryCreateSafe
import Library_TestLooper

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {"Directory": null}
        , 
        []
    )
)



LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_SystemDirectoryCreateSafe.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    PrintExtra = True,
)
































