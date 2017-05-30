
import numpy
#------------------------------------------------------------------------------
import Library_EvaluateFunctionsAtNumpyDataPoints
import Library_TestLooper


ArgSetExpectedResultCombos = []


def x(x):
    return x**1
def x2(x):
    return x**2
def x3(x):
    return x**3

ExamplePolynomialFunctionList = [x, x2, x3]
ExampleDataPoints = numpy.array([1,2,3])



#Try out the 1dim case
ArgSetExpectedResultCombos.append(
    (
        {
            "DataPoints"  : ExampleDataPoints               , 
            "Functions"   : ExamplePolynomialFunctionList   ,
            "Coefficients"  : None                          ,
        }
        , 
        [  
            [ 1 , 1, 1 ]    ,
            [ 2 , 4, 8 ]    ,
            [ 3 , 9, 27 ]   ,
        ]
    )
)




LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_EvaluateFunctionsAtNumpyDataPoints.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    PrintExtra = False,
)

