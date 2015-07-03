
"""
SOURCE:

    pp
        http://www.parallelpython.com/

    **kwargs
        http://stackoverflow.com/questions/1769403/understanding-kwargs-in-python
        NOTE-> these are also used in the `Test_TestLooper`



DESCRIPTION:
    This is a library built to parallize a loop of code for which each iteration of the loop
    is independent of the other iterations of the loop


    for `ArgSet` in 'ListOfArgSets':
        ResultList.append( 'Function'(`ArgSet`) )


ARGS:
    Function
        -> this is the function to be run with each iteration of the loop
    
    ListOfArgSets
        -> this is a list of args, of which each element is a combination of args 
            to call the 'Function' one time
            Looks like:
                [
                ArgSet1,
                ArgSet2,
                .
                .
                ArgSetN,
                ]
            Each `ArgSet` is a dictionary which contains the argument:
                ArgSet1 might look like:
                    {
                    'Arg1' : 'HelloWorld'
                    'Arg2' : 2
                    }

                ArgSet2 might have slightly different arguments (Presumably)
                    {
                    'Arg1' : 'HelloWorld'
                    'Arg2' : 3
                    }

    Algorithm
        Descirption:
            The way in which the loop is parallelized
    
        Default:
            None
                -> if this is the case then the loop isn't parallel at all




RETURNS:
    ResultList:
        Description:
            List of results, each element matches each element of the `ListOfArgSets`:
        [
        ArgSet1Result,
        ArgSet2Result,
        .
        .
        ArgSetNResult,
        ]
       

"""
import pp
import mpi4py
import copy
import Const_Parallel
import pprint



#TEMP HACK:
import Library_CopyFunction
import Library_IsPrime
import Library_SumPrimesBelowInteger
import Library_FunctionInvoker
import Library_LibraryDependencyTreeFlat

def Main(
    Function = None,
    ListOfArgSets = None,
    Algorithm = None,
    CheckArguments = True,
    PrintExtra = False,
    ):

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    ResultList = []


    if (Algorithm == 'loop'):
        for ArgSet in  ListOfArgSets:
            ResultList.append( Library_FunctionInvoker.Main( Function, ArgSet ) )

        
    elif ( Algorithm == 'pp'):
        ppservers = Const_Parallel.ppservers
        JobServer = pp.Server(ppservers=ppservers)

        #Determine the dependencies:
        FunctionDependencies = (
            Function, 
            Library_FunctionInvoker.Main,
            )

        ModuleDependencies = (   )      

        #Run a loop of job submissions:
        #   Note that this loop is allowed to finish before the jobs complete
        #   This throws the jobs on a queue
        Jobs = []
        for ArgSet in ListOfArgSets:
            Jobs.append(
                JobServer.submit( 
                    Library_FunctionInvoker.MainInvoker, #Gets confused by calling main function `Main`
                    (Function, ArgSet) , 
                    FunctionDependencies, 
                    ModuleDependencies  
                    ) 
                )

        #Run a loop of output extractions 
        #   The jobs can run in parallel, 
        #   This loop of extraction tells the master to wait here until they are all done
        #   Note that with our implemenation of this Library_ParllelLoop, 
        #       The lines of code in this file run as the master process. 
        #       Each `Job` is a child process
        #       The master code process is waiting here for all the children to finish
        #           before moving on with further execution -> this is similar to thread spawning
        #           However there is no shared memory through python
        #           So this is more scalable on arbitrary machine architecture
        for Job in Jobs:
            ResultList.append(Job())

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #!!     MASTER WAITS HERE FOR ALL CHILDREN TO COMPLETE
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        if (PrintExtra):
            print 'Job Stats:'
            JobServer.print_stats()



    elif ( Algorithm == 'mpi4py'):
        ErrMsg = 'Not Implemented Yet...'
        raise Exception()

    elif ( Algorithm == 'dougserver'):
        #dougserver.submitJob
        ErrMsg = 'Not Implemented Yet...'
        raise Exception()
    else:
        ErrMsg = 'Unrecognized `Algorithm`... Library_ParallelLoop  FAILED to execute'
        raise Exception(ErrMsg)

    return ResultList














    




