"""
DESCRIPTION:
    Returns a list of python files which are required for a given library to work.
    Assumes that all personally written files are in the current working directory
    The current working directory will be the same directory from which this library in invoked
    (odds are this will be something like ....../FullCodeBaseClean )
    Will search each file for additional depndencies and check if we have that dependency yet
    Will dig trhough the entire tree until every required file is found for a given library to run

ARGS:
    LibraryFileName

RETURNS:
    FileNames

"""
import Library_LibraryDependencyList
import Library_LibraryExists


Counter = 0

def Main( 
    LibraryName  = None,
    IncludeTestFiles = False,
    FlatDependencyTree = [], #Expected to be appendend and passed by reference
    ):
    #print "=======FN ST============="

    #FlatDependencyTree = []

    try:    

        FlatDependencyTree += [LibraryName]


        LibaryNameDependencyList = Library_LibraryDependencyList.Main(LibraryName = LibraryName)

        LibaryFileIdentifier = None
        try:
            LibaryFileIdentifier = LibraryName.split('_')[1]
        except:
            LibaryFileIdentifier = None

        #Add test file to the libraries dependency list
        if (LibaryFileIdentifier != None):
            if (IncludeTestFiles):
                PotentialTestLibraryName = 'Test_'+ LibaryFileIdentifier
                if (  Library_LibraryExists.Main(PotentialTestLibraryName) ):
                    if ( not PotentialTestLibraryName in LibaryNameDependencyList):
                        LibaryNameDependencyList.append(PotentialTestLibraryName)

        for Dependency in LibaryNameDependencyList:
            #print '   Dependency', Dependency
            DependencyFileType = Dependency.split('_')[0]

            if (DependencyFileType in ['Type', 'Library', 'Trash', 'Const', 'Test', 'DS', 'Example' ] ): #Filetypes which are allowed for inclusion
                if (not Dependency in FlatDependencyTree):

                    FlatDependencyTree = sorted( list( set(   
                        FlatDependencyTree
                        + Main(
                            LibraryName = Dependency,
                            IncludeTestFiles = IncludeTestFiles,
                            #FlatDependencyTree = FlatDependencyTree,
                            ) 
                        )  )  )

                FlatDependencyTree = sorted( list( set(   
                    FlatDependencyTree
                    + [Dependency] 

                    )  )  )




        #print "=======FN END============="
        return FlatDependencyTree

    except Exception, Except:
        print 'LibraryName', LibraryName
        print 'Exception', 
        print str( Except )
        return FlatDependencyTree
















    
    
