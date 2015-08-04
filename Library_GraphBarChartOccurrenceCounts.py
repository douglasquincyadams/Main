
"""

DESCIPRTION:

    Gets the number of times elements show up N times, where N is a count
    so for the list:

        eglist = [1,1,2,3,4,5,6,6]
    
    should get the counts:
        


        [ 
        [1, 4 ]    -> 4 elements show up 1 time in the list
        [2, 2 ]     -> 2 elements show up 2 times in the list
        ]

        4*1 + 2*2 == 8 == len(eglist)


ARGS:
    PythonList -> python list


"""
import numpy
import collections
import matplotlib
import matplotlib.pyplot
def Main( 
    PythonList = None,
    SaveFigureFilePath = None,
    ):


    ListCounts =  numpy.atleast_2d( numpy.array(  collections.Counter( list( numpy.atleast_2d( numpy.array( collections.Counter(PythonList).most_common() ) )[:,1] ) ).most_common() ))

    Count       = list( ListCounts[:,0] )
    CountCount  = list( ListCounts[:,1] )

    left = numpy.array( Count ) - 0.25
    height = CountCount
    width = .5
    matplotlib.pyplot.bar(left, height, width)

    matplotlib.pyplot.grid()





    #matplotlib.pyplot.show()

    if (SaveFigureFilePath != None):
        matplotlib.pyplot.savefig( SaveFigureFilePath )












