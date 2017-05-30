
"""
@author: Adams, Douglas

The Kernel Density Estimation:

    

"""


import numpy
import scipy
import scipy.stats
import random

#import Trash_NumpyKDE

#------------------------------------------------------------------------------
import Library_KernelDensityEstimation
import Library_OrderOfMagnitudeRatio
import Library_PrintFullTestSuccess
import Library_KernelDensityBandwidthSilverman
FullTestSuccess = True

#Set the seed for our tests - this we we generate random numbers the same way each time:
random.seed(0)
numpy.random.seed(0)


#Build fake datasets:
FakeDatasets = []

#Build a one dimentional fake dataset:
FakeDataset1 = {}
FakeDataset1["Title"] = "ONE DIMENSIONAL DATASET"
FakeDataset1["ExampleDatasetMean"] = numpy.array([0.0])
FakeDataset1["ExampleDatasetCovarianceMatrix"] = numpy.array([[2.0]])
FakeDataset1["ExampleDatasetShape"] = (10)
#ExampleDataset = 10.0 * numpy.random.multivariate_normal(Mean, Cov, ExampleDatasetShape)
FakeDataset1["ExamplePoint"] = numpy.array([0.9])
FakeDataset1["ExamplePointSet"] = numpy.array([[0.0],[0.1],[0.2]])

FakeDatasets.append(FakeDataset1)

#Build a two dimensional fake dataset:
FakeDataset2 = {}
FakeDataset2["Title"] = "TWO DIMENSIONAL DATASET"
FakeDataset2["ExampleDatasetMean"] = numpy.array([0.0,0.0])
FakeDataset2["ExampleDatasetCovarianceMatrix"] = numpy.array([[2.0,1.0],[1.0,2.0]])
FakeDataset2["ExampleDatasetShape"] = (10)
#ExampleDataset = 10.0 * numpy.random.multivariate_normal(Mean, Cov, ExampleDatasetShape)
FakeDataset2["ExamplePoint"]  = numpy.array([0.9,0.9])
FakeDataset2["ExamplePointSet"] = numpy.array([[0.0,0.0],[0.1,0.1],[0.2,0.1]])

FakeDatasets.append(FakeDataset2)


for FakeDataset in FakeDatasets:
    print "===================================================================="
    print FakeDataset["Title"]
    ExampleDataset = 10.0 * numpy.random.multivariate_normal(\
        FakeDataset["ExampleDatasetMean"],\
        FakeDataset["ExampleDatasetCovarianceMatrix"],\
        FakeDataset["ExampleDatasetShape"],\
        )

    ExamplePoint = FakeDataset["ExamplePoint"]
    ExamplePointSet = FakeDataset["ExamplePointSet"] 

    print "ExampleDataset.shape:  ", ExampleDataset.shape
    print "ExamplePoint.shape:    ", ExamplePoint.shape
    print "ExamplePointSet.shape: ", ExamplePointSet.shape


    print "SCIPY_RESULTS:"
    ScipyDensityKernelDensityEstimationFunction = scipy.stats.gaussian_kde(ExampleDataset.T, bw_method = 'silverman')
    ScipySinglePointDensity = ScipyDensityKernelDensityEstimationFunction(ExamplePoint)[0]
    print "ScipySinglePointDensity\n", ScipySinglePointDensity, "\n"  
    ScipyMutliplePointDensities = ScipyDensityKernelDensityEstimationFunction(ExamplePointSet.T)
    print "ScipyMutliplePointDensities\n", ScipyMutliplePointDensities, "\n"  


    print "RESULTS"
    SinglePointDensity = Library_KernelDensityEstimation.Main( \
        Point = ExamplePoint,\
        Dataset = ExampleDataset,\
        PrintExtra = False\
        )
    print "SinglePointDensity\n: ", SinglePointDensity , "\n" 
    MutliplePointDensities = []
    for Point in ExamplePointSet:
        Density = Library_KernelDensityEstimation.Main( \
            Point = Point,\
            Dataset = ExampleDataset,\
            PrintExtra = False\
            )
        MutliplePointDensities.append(Density)
    MutliplePointDensities = numpy.array(MutliplePointDensities)
    print "MutliplePointDensities\n", MutliplePointDensities, "\n"


    #COMPARE SCIPY_RESULTS TO RESULTS:
    #Check Single Result:
    OrderOfMagnitudeRatio = Library_OrderOfMagnitudeRatio.Main(
        ScipySinglePointDensity, 
        SinglePointDensity)
    if (OrderOfMagnitudeRatio < 0.01):
        print "Test Success: ", ScipySinglePointDensity, "~", SinglePointDensity
    else:
        FullTestSuccess = False
        print "Test Failure: ", ScipySinglePointDensity, "!=", SinglePointDensity


    #Check the mulitple results:
    k = 0 
    while k <  ExamplePointSet.shape[0]:
        #print k
        ScipyDensity = ScipyMutliplePointDensities[k]
        Density = MutliplePointDensities[k]
        OrderOfMagnitudeRatio = Library_OrderOfMagnitudeRatio.Main(ScipyDensity, Density)
        if (OrderOfMagnitudeRatio < 0.01):
            print "Test Success: ", ScipyDensity, "~", Density
        else:
            FullTestSuccess = False
            print "Test Failure: ", ScipyDensity, "!=", Density
        k = k + 1

#Try out the argument handling by passing in some cooky values which should be caught:
#TODO




Library_PrintFullTestSuccess.Main(FullTestSuccess)






"""

print "--Copied Scipy Implementation:"

ScipyDensityKernelDensityEstimationFunction2 = Trash_NumpyKDE.gaussian_kde(ExampleDataset.T, bw_method = 'silverman')

ScipySinglePointDensity2 = ScipyDensityKernelDensityEstimationFunction2(ExamplePoint)
print "ScipySinglePointDensity2\n", ScipySinglePointDensity2, "\n"  

#ScipyMutliplePointDensities2 = ScipyDensityKernelDensityEstimationFunction2(ExamplePointSet.T)
#print "ScipyMutliplePointDensities2\n", ScipyMutliplePointDensities2, "\n"  

"""























