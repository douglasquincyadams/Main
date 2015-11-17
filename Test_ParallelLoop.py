
"""
#To avoid some hokey loop-ception 
    -> we are going to avoid using the Library_TestLooper for this test suite
"""
import pprint
import datetime
import Library_ParallelLoop
import Library_SumPrimesBelowInteger






ExampleFunction = Library_SumPrimesBelowInteger.Main 
ListOfArgSets = []
for x in range(30):
    ListOfArgSets.append(
            {
                "Integer"  :  x*1000 , 
            }
        )


def Test0():


    """
        Run as a basic loop (as though there was no parallelization: )
    """

    start = datetime.datetime.utcnow()
    ResultList = Library_ParallelLoop.Main(
        Function = ExampleFunction,
        ListOfArgSets = ListOfArgSets,
        Algorithm = 'loop',
        PrintExtra = True
        )
    end = datetime.datetime.utcnow()
    TimeTaken = end - start

    #[5736396, 454396537, 454396537, 454396537]

    #print 'ResultList loop'
    #pprint.pprint(ResultList)

    print 'TimeTaken', TimeTaken

    #print '\n\n\n'

    assert(ResultList[1] == 76127)
    assert(ResultList[2] == 277050)

    """
        Run using pp module:
    """

    start = datetime.datetime.utcnow()
    ResultList = Library_ParallelLoop.Main(
        Function = ExampleFunction,
        ListOfArgSets = ListOfArgSets,
        Algorithm = 'pp',
        PrintExtra = False
        )
    end = datetime.datetime.utcnow()
    TimeTaken = end - start

    #[5736396, 454396537, 454396537, 454396537]

    #print 'ResultList pp'
    #pprint.pprint(ResultList)

    print 'TimeTaken', TimeTaken
    assert(ResultList[1] == 76127)
    assert(ResultList[2] == 277050)
    print'Test0 Results Same'



def ExampleFunction2( 
    Arg1 = None,
    Arg2 = None,
    ):
    return Arg1 + Arg2
ListOfArgSets2 = []
for x in range(30):
    ListOfArgSets2.append(
            {
                "Arg1"  :  x*1000 , 
                "Arg2"  :  x*20 , 
            }
        )

"""
    Run ExampleFunction2 using pp module :

"""
def Test1():


    #print 'ListOfArgSets2'
    #pprint.pprint(ListOfArgSets2)

    start = datetime.datetime.utcnow()
    ResultList = Library_ParallelLoop.Main(
        Function = ExampleFunction2,
        ListOfArgSets = ListOfArgSets2,
        Algorithm = 'pp',
        PrintExtra = False
        )
    end = datetime.datetime.utcnow()
    TimeTaken = end - start

    #[5736396, 454396537, 454396537, 454396537]

    #print 'ResultList pp'
    #pprint.pprint(ResultList)

    print 'TimeTaken', TimeTaken


    assert(ResultList[1] == 1020)
    assert(ResultList[2] == 2040)


def Test3():
    #Most compact function call:
    ResultList = Library_ParallelLoop.Main(
        Function = ExampleFunction2,
        ListOfArgSets = ListOfArgSets2,
        Algorithm = 'pp',
        )


    #print ResultList
    assert(ResultList[1] == 1020)
    assert(ResultList[2] == 2040)

Test0()


Test1()


Test3()

print 'Full Test Success'





















