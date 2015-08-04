"""



"""
import numpy
import pprint
#------------------------------------------------------------------------------
import Library_NumpyArrayEqualMultipleArrays
import Library_PrintFullTestSuccess

FullTestSuccess = True

#SETUP SOME EXAMPLE ARRAYS:
A1 = numpy.array([[1,4],[2,5],[3,6]])
A2 = numpy.array([[1,4],[2,5],[3,6]])
A3 = numpy.array([[1,4],[2,5],[3,6]])

Aunsort1 = numpy.array([[2,5],[3,6], [1,4]])
Aunsort2 = numpy.array([[3,6], [1,4], [2,5]])

Anot = numpy.array([[1,4],[2,6],[3,5]])
B = numpy.array([[1,4],[3,6],[7,8]])
C = numpy.array([[1,4],[7,8],[9,10]])
D = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
E = numpy.array([[1,2,3],[4,5,6]])

#MATCH THE ARGS WITH OUR EXPECTED RESULTS:
ArgsExpectedResultListOrderMatters = [
    ((A1, A2, A3), True),
    ((A1, A2, B), False),
    ((A1, A3, A2 ), True),
    ((B, A2, A3), False),
    ((E, A3, A2 ), False), #Different Shape

    ((A1, A2, Aunsort1), False), #Only True if order does not matter
    ((A1, A2, Aunsort2), False), #Only True if order does not matter
]

ArgsExpectedResultListOrderDoesNotMatter = [
    ((A1, A2, A3), True),
    ((A1, A2, B), False),
    ((A1, A3, A2 ), True),
    ((B, A2, A3), False),
    ((E, A3, A2 ), False), #Different Shape
    ((A1, A2, Aunsort1), True), #Only True if order does not matter
    ((A1, Aunsort2, A2), True), #Only True if order does not matter
    ((A1, Anot), False ) #Contains same flattened elements, but regardless of sort should not be equal
]

#CHECK EACH SET OF ARGS AND MAKE SURE WE GET THE RESULT WE ARE EXPECTING:

for OrderMatters in [True, False]:
    if (OrderMatters):
        ArgsExpectedResultList = ArgsExpectedResultListOrderMatters
    else:
        ArgsExpectedResultList = ArgsExpectedResultListOrderDoesNotMatter
    for Arrays, ExpectedResult in ArgsExpectedResultList:
        Result = Library_NumpyArrayEqualMultipleArrays.Main(Arrays, OrderMatters = OrderMatters)
        if ( Result == ExpectedResult ):
            print "Single Test Success"
        else:
            print "Single Test Failure"
            print 'Arrays'
            pprint.pprint(Arrays,  indent=2)
            print 'OrderMatters     :', OrderMatters
            print 'Result           :', Result
            print 'ExpectedResult   :', ExpectedResult

        
            FullTestSuccess = False


Library_PrintFullTestSuccess.Main(FullTestSuccess)
