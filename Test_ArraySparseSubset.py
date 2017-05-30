import numpy
import Library_ArraySparseSubset
import Library_TestLooper


numpy.random.seed(seed = 0 )

ExampleArray = range(100)

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        {
            "Array"  :       ExampleArray                  , 
            "SubsetFraction"   : .1       ,
        }
        , 
        [  8, 13, 20, 27, 38, 52, 70, 72, 89 ]
    )
)


LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_ArraySparseSubset.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    HardDifferenceMax = 0.1,
    PrintExtra = False,
)
