import Library_OuterProduct

List1 = [ 'one', 'two']
List2 = [ 'fish', 'wish']
List3 = [ 'blue', 'red']

ListOfLists = [List1, List2, List3]

DrSuessNovel = Library_OuterProduct.Main(
    ListOfLists= ListOfLists
    )

for Sentence in DrSuessNovel:
    print Sentence


#Prints out:
"""
['one', 'fish', 'blue']
['two', 'fish', 'blue']
['one', 'wish', 'blue']
['two', 'wish', 'blue']
['one', 'fish', 'red']
['two', 'fish', 'red']
['one', 'wish', 'red']
['two', 'wish', 'red']
"""

#LOL THIS WORKS....
"""
ApproximationOrder = 3
ApproximationVariableNames = ['x', 'y', 'z']

PossibleValuesPerVariable = [range(ApproximationOrder) for VariableName in range(len(ApproximationVariableNames))]
print 'PossibleValuesPerVariable', PossibleValuesPerVariable

TermIndices = Library_OuterProduct.Main(
    PossibleValuesPerVariable
    )
print 'TermIndices', TermIndices
"""







































