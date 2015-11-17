import Library_EqualityCheck
import Library_TestLooper
import numpy


def ExampleFunction(ArgsAndStuff):
    print 'Does Stuff'

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {"ObjectsTuple": (None, None)}
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"ObjectsTuple": (numpy.array([1,2]), numpy.array([1,2]))}
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"ObjectsTuple": (numpy.nan, numpy.nan, numpy.nan, numpy.nan, numpy.nan) }
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"ObjectsTuple": (ExampleFunction, ExampleFunction) }
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"ObjectsTuple": (numpy.array([3,2]), numpy.array([1,2]))}
        , 
        False
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"ObjectsTuple": ('hello world', 'hello word')}
        , 
        False
    )
)


LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_EqualityCheck.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    PrintExtra = True,
)
































