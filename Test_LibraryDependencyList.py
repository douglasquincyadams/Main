import Library_LibraryDependencyList
import Library_PrintArray
import Library_NumpyArrayEqualMultipleArrays
import Library_PrintFullTestSuccess

FullTestSuccess = True

ExampleLibaryName = "Library_ExampleLibraryGood0"


DependencyList = Library_LibraryDependencyList.Main(LibraryName = ExampleLibaryName)

ExpectedDependencyList = [
"numpy",
"matplotlib.pyplot",
"matplotlib.pylab",
"matplotlib.asdf",
"matplotlib.importas",
"matplotlib.asimport",
"matplotlib.last",
"matplotlib.pylab",
"Library_ExampleLibraryGood1",
"Library_ExampleLibraryGood1",
"fromasimport.asimport",
"Library_ExampleLibraryGood1",
]

print 'DependencyList'
Library_PrintArray.Main(DependencyList)

print ''

print 'ExpectedDependencyList'
Library_PrintArray.Main(ExpectedDependencyList)

ResultGood = Library_NumpyArrayEqualMultipleArrays.Main( 
    ArrayTuple = (DependencyList, ExpectedDependencyList) ,
    OrderMatters = False
)
if (ResultGood):
    print "Single Test Success"
else:
    print "Single Test Failure"
    FullTestSuccess = False

Library_PrintFullTestSuccess.Main(FullTestSuccess)
