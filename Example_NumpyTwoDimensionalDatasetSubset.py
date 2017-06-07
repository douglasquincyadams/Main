
#With this simple code:
#   There is no limitation on which order you drill down into the dataset.
#   You can make a choice for any column before making anotehr choice for any otehr column.
#   Avialiabe choices are the mathematical set of the datasetsubsets column values.
#   Each time you make a choice - you can simply re-subset && re-setify the remaning column choices
#   However -> I don't understand the purpose of building this into execl.
#   Native excel funcitonality already allows for a filter to be added on top of a datset.




import numpy
import Library_NumpyTwoDimensionalDatasetSubset

ExampleRequiredColumnValues = [None, 2, None, 4]
ExampleNumpyTwoDimensionalDataset = numpy.array([
    [1,2,3,4],
    [1,0,2,3],
    [0,0,0,0],
    [1,2,3,4],
    [1,1,3,4],
    [1,2,3,1],
    [0,2,0,4]
    ])


#TAKE A SUBSET:
DatasetSubset = Library_NumpyTwoDimensionalDatasetSubset.Main(
    RequiredColumnValues = ExampleRequiredColumnValues,
    NumpyTwoDimensionalDataset= ExampleNumpyTwoDimensionalDataset,
    )
print DatasetSubset
"""
[[1 2 3 4]
 [1 2 3 4]
 [0 2 0 4]]
"""

#SETIFY THE POSSIBLE COLUMN CHOICES:
for ColumnNumber in range(len(ExampleRequiredColumnValues)) :
    SubsetColumnSet = set(DatasetSubset[ :, ColumnNumber ])
    print 'ColumnNumber', ColumnNumber, ':', SubsetColumnSet
"""
ColumnNumber 0 : set([0, 1])
ColumnNumber 1 : set([2])
ColumnNumber 2 : set([0, 3])
ColumnNumber 3 : set([4])
"""





#Pretend now we want limit the dataset again by a choice of the 0th column:
SubsetColumn0Set = set(DatasetSubset[ :, 0 ])
print 'SubsetColumn0Set', SubsetColumn0Set
"""
set([0, 1])
"""


#Now take retake the subset of the dataset with column0 choice to 0:
ExampleRequiredColumnValues[0] = 0
DatasetSubset = Library_NumpyTwoDimensionalDatasetSubset.Main(
    RequiredColumnValues = ExampleRequiredColumnValues,
    NumpyTwoDimensionalDataset= ExampleNumpyTwoDimensionalDataset,
    )
print 'DatasetSubset', DatasetSubset
"""
[[0 2 0 4]]
"""

































