

import numpy

import Library_PrintDatasetStatistics

#Test1
Dataset = numpy.random.random(size = (100,3) )
#print Dataset
Library_PrintDatasetStatistics.Main(Dataset = Dataset, PrintLineHeader = "Dataset", PrintLineBufferSize = 4 )



DatasetOfStrings = numpy.array(["a", "b"])
Library_PrintDatasetStatistics.Main(DatasetOfStrings, "Dataset" , 4)


DatasetOfStrings_2D = numpy.atleast_2d(DatasetOfStrings).T
Library_PrintDatasetStatistics.Main(DatasetOfStrings_2D, "Dataset", 4)

