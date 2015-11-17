
import numpy
#------------------------------------------------------------------------------
import Library_KernelDensityBandwidthSilverman
import Library_OrderOfMagnitudeRatio
import Library_PrintFullTestSuccess

FullTestSuccess = True


#Build a fake dataset:
Mean = numpy.array([1,1])
Cov = numpy.array([[1,2],[-3,-4]])
Shape = (100)
ExampleDataset = 10 * numpy.random.multivariate_normal(Mean, Cov, Shape)

ExampleSilvermanCovarianceMatrix = Library_KernelDensityBandwidthSilverman.Main(ExampleDataset)

print "ExampleSilvermanCovarianceMatrix\n", ExampleSilvermanCovarianceMatrix, "\n"

print "This test suite only checks that errors are not thrown... Need better tests"

Library_PrintFullTestSuccess.Main(FullTestSuccess)
















