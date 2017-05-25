import Library_OuterProduct
import Library_TestLooper

List1 = [ 'one', 'two']
List2 = [ 'fish', 'wish']
List3 = [ 'blue', 'red']

ListOfLists = [List1, List2, List3]


ExpectedResult1 = \
[
['one', 'fish', 'blue'],
['two', 'fish', 'blue'],
['one', 'wish', 'blue'],
['two', 'wish', 'blue'],
['one', 'fish', 'red'],
['two', 'fish', 'red'],
['one', 'wish', 'red'],
['two', 'wish', 'red'],
]

ArgSetExpectedResultCombos = []
ArgSetExpectedResultCombos.append(
    (
        
        {
            "ListOfLists": ListOfLists
        }
        , 
        ExpectedResult1
    )
)



LoopResult = Library_TestLooper.Main(
    FunctionToTest = Library_OuterProduct.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.1,
    HardDifferenceMax = 1.0,
    DoEqualityCheck = True,
    DoContainmentCheck = False,
    MinFlatResultLength = None,
    MaxFlatResultLength = None,
    ResultOrderMatters = True, 
    EqualityCheckFunction = None,
    PrintExtra = True,
)

































