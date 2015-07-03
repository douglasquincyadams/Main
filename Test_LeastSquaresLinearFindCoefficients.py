import numpy

#------------------------------------------------------------------------------
import Library_LeastSquaresLinearFindCoefficients
import Library_GeneratePolynomial #note -> largest term is first -> leads with highest power
import Library_TestLooper

DataPoints = numpy.array([[1,2],[2,4],[3,6]])



ArgSetExpectedResultCombos = []


ArgSetExpectedResultCombos.append(
    (
        {
            "Dataset"               : DataPoints                            ,
            "FunctionDimension"     : 1                                     ,
            "FitFunction"           : Library_GeneratePolynomial.Main(2)    ,  #ax^2 + bx + c
        } 
        , 
        numpy.array( [0, 2, 0] ) #0x^2 + 2x + 0
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "Dataset"               : DataPoints                            ,
            "FunctionDimension"     : 1                                     ,
            "FitFunction"           : Library_GeneratePolynomial.Main(1)    ,  #ax+ b
        } 
        , 
        numpy.array( [2, 0] ) #2x + 0
    )
)


Library_TestLooper.Main(
    FunctionToTest = Library_LeastSquaresLinearFindCoefficients.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = None,
    HardDifferenceMax = 0.01,
    PrintExtra = False,
)
