

import matplotlib
import matplotlib.pylab
import numpy

import Library_Gaussian
import Library_GaussianIndefiniteIntegral
import Library_TestLooper






ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
            "Point"  : 0.           , 
            "MeanPoint"   : 0.       ,
            "CovarianceMatrix"  : 1       ,
        }
        , 
        [   .5 ]
    )
)


ArgSetExpectedResultCombos.append(
    (
        {
            "Point"  : 3.           , 
            "MeanPoint"   : 3.       ,
            "CovarianceMatrix"  : 1       ,
        }
        , 
        [   .5 ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "Point"  : 1.           , 
            "MeanPoint"   : 1.       ,
            "CovarianceMatrix"  : 2       ,
        }
        , 
        [   .5 ]
    )
)

ArgSetExpectedResultCombos.append(
    (
        {
            "Point"  : 3.           , 
            "MeanPoint"   : 3.       ,
            "CovarianceMatrix"  : 5       ,
        }
        , 
        [   .5 ]
    )
)

LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_GaussianIndefiniteIntegral.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 0.1,
    PrintExtra = False,
)



#Graphing for sanity:
if(True):
    matplotlib.pylab.figure()

    DatasetDomainMin = -1.
    DatasetDomainMax = 1.

    GraphMean = 0.
    GraphCovarianceMatrix = .01

    Inputs = numpy.linspace(DatasetDomainMin, DatasetDomainMax, 100)
    print '   Graphing Gaussian...'
    Outputs = []
    for Input in Inputs:
        Outputs.append(
            Library_Gaussian.Main( 
            Point = numpy.array([Input]),
            MeanPoint = GraphMean,
            CovarianceMatrix = GraphCovarianceMatrix,
            )
        )
    matplotlib.pyplot.plot(Inputs, Outputs, 'r', label='Gaussian')


    print '   Graphing IntGaussian...'
    Outputs = []
    for Input in Inputs:
        Outputs.append(
            Library_GaussianIndefiniteIntegral.Main( 
            Point = numpy.array([Input]),
            MeanPoint = GraphMean,
            CovarianceMatrix = GraphCovarianceMatrix,
            )
        )
    matplotlib.pyplot.plot(Inputs, Outputs, 'b', label='IntegralGaussian')

    matplotlib.pylab.show()


















