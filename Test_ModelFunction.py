


#------------------------------------------------------------------------------
import Library_ModelFunctionGaussianTwoDimensionalMeanParameters
import Library_TestLooper
import Type_ModelFunction


#Create some example model functions to test:
def ExampleFailModelFunction1(Arg1, Arg2):
    return Arg1

def ExampleFailModelFunction2(DataPoint, Arg2):
    return DataPoint

def ExampleFailModelFunction3(Arg1, Parameters):
    return Arg1

def ExampleGoodModelFunction(DataPoint, Parameters):
    return DataPoint


#Run the tests with the expected results:
ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
            "ModelFunctionCadidate"  : Library_ModelFunctionGaussianTwoDimensionalMeanParameters.Main         , 
        }
        , 
        [ True ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "ModelFunctionCadidate"  : None        , 
        }
        , 
        [ False ]
    )
)


ArgSetExpectedResultCombos.append(
    (
        {
            "ModelFunctionCadidate"  : ExampleFailModelFunction1        , 
        }
        , 
        [ False ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "ModelFunctionCadidate"  : ExampleFailModelFunction2        , 
        }
        , 
        [ False ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "ModelFunctionCadidate"  : ExampleFailModelFunction3        , 
        }
        , 
        [ False ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "ModelFunctionCadidate"  : ExampleGoodModelFunction        , 
        }
        , 
        [ True ]
    )
)

LoopResult = Library_TestLooper.Main(
    FunctionToTest = Type_ModelFunction.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = None,
    HardDifferenceMax = 0.01,
    PrintExtra = False,
)







































