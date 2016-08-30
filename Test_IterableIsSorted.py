import Library_IterableIsSorted
import Library_TestLooper
import datetime
import itertools
import numpy

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {"Iterable": [1,2,3,4]}
        , 
        True
    )
)

ArgSetExpectedResultCombos.append(
    (
        {"Iterable": [1,5,3,4]}
        , 
        False
    )
)


LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_IterableIsSorted.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    PrintExtra = True,
)



print 'Time Tests'
Max = 1000
LargeList = range(Max)
LargeList[Max - 10] = 101

LargeList = list( numpy.random.random(10000))
#print LargeList

Start = datetime.datetime.utcnow()
Result = Library_IterableIsSorted.Main(LargeList ,   Method = 'iter')
End = datetime.datetime.utcnow()
print End - Start
print 'Result', Result



Start = datetime.datetime.utcnow()
Result = Library_IterableIsSorted.Main(LargeList ,   Method = 'all')
End = datetime.datetime.utcnow()
print End - Start
print 'Result', Result



Start = datetime.datetime.utcnow()
Result = Library_IterableIsSorted.Main(LargeList ,   Method = 'sorted')
End = datetime.datetime.utcnow()
print End - Start
print 'Result', Result





















