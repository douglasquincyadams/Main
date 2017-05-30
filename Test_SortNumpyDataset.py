import numpy


import Library_SortNumpyDataset
import Library_PrintFullTestSuccess
FullTestSuccess = True

#SETUP SOME EXAMPLE ARRAYS:
A1 = numpy.array([[1,4],[2,5],[3,6]])
A1list = A1.tolist()
#print 'A1', '\n',A1
Aunsort1 = numpy.array([[2,5],[3,6], [1,4]])
#print 'Aunsort1', '\n',Aunsort1

Aunsort1ReverseColumns = numpy.array([[5, 2],[6, 3], [4, 1]])

Aunsort1ReverseColumnsAxis0Sorted = numpy.array([ [4, 1], [5, 2],[6, 3]])
#print 'AReverseColumns', AReverseColumns

Aunsort2 = numpy.array([[3,6], [1,4], [2,5]])
#print 'Aunsort2', '\n',Aunsort2
Anot = numpy.array([[1,4],[2,6],[3,5]])
#print 'Anot', '\n',Anot

AOneDimmList = [1,2,3,0]
AOneDimmListSorted = [0,1,2,3]
AOneDimmListSortedIndexes = numpy.array( [3,0,1,2] )

B = numpy.array([[1,4],[3,6],[7,8]])
C = numpy.array([[1,4],[7,8],[9,10]])
D = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
E = numpy.array([[1,2,3],[4,5,6]])



ArgsExpectedResultListAxis0 = [
    (A1list, A1list),
    (Aunsort1,  A1),
    (Aunsort2,  A1),
    (A1, A1),
    (Aunsort1ReverseColumns, Aunsort1ReverseColumnsAxis0Sorted),
    (AOneDimmList, AOneDimmListSorted),
]


ArgsExpectedResultListAxis1 = [
    (Aunsort1,  Aunsort1),
    (Aunsort2,  Aunsort2),
    (A1, A1),
    (Aunsort1ReverseColumns, Aunsort1),
    (AOneDimmList,  AOneDimmList),
]

ArgsExpectedResultListAxis0PreserveOrder = [
    (Aunsort1, (A1,  numpy.array([2, 0, 1] ) )),
    (AOneDimmList, (AOneDimmListSorted, AOneDimmListSortedIndexes ) ),
]

ArgsExpectedResultListAxis1PreserveOrder = [
    (Aunsort1, (Aunsort1, numpy.array([0, 1])  )),
]


for PreserveOrder in [True, False]:
    for Axis in [0,1]:
        if (PreserveOrder):
            if (Axis == 0):
                ArgsExpectedResultList = ArgsExpectedResultListAxis0PreserveOrder
            elif (Axis == 1):
                ArgsExpectedResultList = ArgsExpectedResultListAxis1PreserveOrder
        else:
            if (Axis == 0):
                ArgsExpectedResultList = ArgsExpectedResultListAxis0
            elif (Axis == 1):
                ArgsExpectedResultList = ArgsExpectedResultListAxis1

        for Arg, ExpectedResult in ArgsExpectedResultList:
            Result = Library_SortNumpyDataset.Main(
                Dataset = Arg, 
                Axis = Axis, 
                PreserveOrder = PreserveOrder
                )
            #print Result
            #if ( numpy.array_equal(Result, ExpectedResult )  ):
            if (str(Result) == str(ExpectedResult)): #Lazy is sometimes better ...
                print " Single Test Success"
            else:
                print " Single Test Failure"
                print ' Axis: ', Axis
                print ' Arg\n', Arg
                print ' Result\n', Result

                print ' ExpectedResult\n', ExpectedResult
                FullTestSuccess = False



Library_PrintFullTestSuccess.Main(FullTestSuccess)


























