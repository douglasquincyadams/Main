
import numpy
import matplotlib.pyplot as plt

import Library_Gaussian
import Library_KernelDensityEstimation
#------------------------------------------------------------------------------
import Library_GraphOneDimensionalKernelDensity

numpy.random.seed(0)

#Create a bimodal distribution:
MeanPoint = numpy.array([0.0])
CovarianceMatrix = numpy.array([[0.1]])
ExampleDatasetShape = (50,)
ExampleDatasetA = numpy.random.multivariate_normal(
    MeanPoint - 1,
    CovarianceMatrix,
    ExampleDatasetShape,
    ) 
ExampleDatasetB = numpy.random.multivariate_normal(
    MeanPoint + 1,
    CovarianceMatrix,
    ExampleDatasetShape,
    ) 
ExampleDataset = numpy.concatenate((ExampleDatasetA, ExampleDatasetB), axis=0) #axis is important



#Graph the Kernel Density Estimation:
Library_GraphOneDimensionalKernelDensity.Main(
    ObservedDataset = ExampleDataset, 
    Xlabel = 'Marbles',
    Ylabel = 'Chances Doug Lost `Em'
    )
plt.show()



#Graph the Kernel Density Estimation:
ExampleDataset2 = ExampleDataset.flatten()
Library_GraphOneDimensionalKernelDensity.Main(
    ObservedDataset = ExampleDataset2, 
    Xlabel = 'Marbles',
    Ylabel = 'Chances Doug Lost `Em'
    )
plt.show()

