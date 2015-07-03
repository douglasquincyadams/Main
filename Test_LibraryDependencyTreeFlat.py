"""
DESCRIPTION:
    Trys out the methon on some exmaple libraries created for the explicit purpose
        of this kind of file parsing. If these example libraries are modified, then this test will break

DEPENDS ON:
    Library_ExampleLibraryGood0
    Library_ExampleLibraryGood1
    Library_ExampleLibraryGood2

"""

import Library_LibraryDependencyTreeFlat
import Library_PrintArray
import Library_NumpyArrayEqualMultipleArrays
import Library_PrintFullTestSuccess

FullTestSuccess = True

ExampleLibaryName = "Library_ExampleLibraryGood0"
#ExampleLibaryName = "Utility_AstronomyFermiEventsSkyMapGalaxyGroupsAndPointSourcesMask"
#ExampleLibaryName = 'Library_Gaussian'

DependencyTree = Library_LibraryDependencyTreeFlat.Main(
    LibraryName = ExampleLibaryName,
    IncludeTestFiles = True,
    )

ExpectedDependencyTree = [
"Library_ExampleLibraryGood0",
"Library_ExampleLibraryGood1",
"Library_ExampleLibraryGood2",
"Library_PrintFullTestSuccess",
"Library_PrintNumpyArrayInfo",
"Test_ExampleLibraryGood0",
"Test_NumpyTwoDimensionalDataset",
"Type_NumpyTwoDimensionalDataset",
]

print 'DependencyTree:\n'
Library_PrintArray.Main(DependencyTree)

print ''

print 'ExpectedDependencyTree:\n'
Library_PrintArray.Main(ExpectedDependencyTree)

ResultGood = Library_NumpyArrayEqualMultipleArrays.Main( 
    ArrayTuple = (DependencyTree, ExpectedDependencyTree) ,
    OrderMatters = False
)
if (ResultGood):
    print "Single Test Success"
else:
    print "Single Test Failure"
    FullTestSuccess = False

Library_PrintFullTestSuccess.Main(FullTestSuccess)










