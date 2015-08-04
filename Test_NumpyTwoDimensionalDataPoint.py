
import numpy
#------------------------------------------------------------------------------
import Type_NumpyTwoDimensionalDataPoint
import Library_TestLooper

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
            "DataPoint"         : numpy.array([12.0, 13.0])  , 
        }
        , 
        [ True ]
    )
)


ArgSetExpectedResultCombos.append(
    (
        {
            "DataPoint"         : numpy.array([12, 13])  , 
        }
        , 
        [ True ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "DataPoint"         : numpy.array([12, 13])  , 
        }
        , 
        [ True ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "DataPoint"         : numpy.array([[12, 13]])  , 
        }
        , 
        [ False ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "DataPoint"         : numpy.array([[12], [13]])  , 
        }
        , 
        [ False ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "DataPoint"         : numpy.array(['asdf', 'asdf'])  , 
        }
        , 
        [ False ]
    )
)


LoopResult = Library_TestLooper.Main(
    FunctionToTest = Type_NumpyTwoDimensionalDataPoint.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    PrintExtra = False,
)























