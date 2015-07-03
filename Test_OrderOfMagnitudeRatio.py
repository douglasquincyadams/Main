

import numpy

import Library_OrderOfMagnitudeRatio
import Library_PrintFullTestSuccess


FullTestSuccess = True

ArgCheckList = [
    [[1.0, 10.0, 100.0], [1.0, 1.0, 1.0]],
    [0.0, 1.0],
    [0.1, 1.0],
    [0.0,0.0],
    [1,10], 
    [10,10], 
    [10,1], 
    [1000,1], 
    [None, None], 
    [-1.0, 10], 
    [10,-1.0] , 
    [-1.0, -10000.0], 
    [numpy.array( [1.0,10.0,-10.]),numpy.array( [10.,1., -1.]) ],
    
    ]
ExpectedResultList = [
    [0., 1., 2.],
    float('Inf'),
    1.,
    0.,
    1.,
    0.,
    1.,
    3., 
    "(A == None)(B == None)", 
    float('Inf'), 
    float('Inf'), 
    4.0,
    [1.,1.,1.]
    ]

assert( len(ArgCheckList) == len(ExpectedResultList) )

NumTrials = len(ArgCheckList)

k = 0
while (k < NumTrials):
    print "Running Test ", k
    A = ArgCheckList[k][0]
    B = ArgCheckList[k][1]
    ExpectedResult = ExpectedResultList[k]

    #print "A", A
    #print "B", B
    #print "ExpectedResult   :", ExpectedResult

    Result = None
    try:
        Result = Library_OrderOfMagnitudeRatio.Main(A, B)
    except Exception, ErrorMessage:
        Result = str(ErrorMessage)

    #print 'Result', Result


    ExpectedResultTypeIsString = (str(type(ExpectedResult)) == "<type 'str'>")
    if (not ExpectedResultTypeIsString):
        ResultArr = numpy.array(Result).astype(numpy.float)
        #print 'ResultArr', ResultArr
        ExpectedResultArr = numpy.array( ExpectedResult ).astype(numpy.float)
        #print 'ExpectedResultArr', ExpectedResultArr

    if ( 
        ExpectedResultTypeIsString and (Result != ExpectedResult) 
        or  ( numpy.array_equal( ResultArr , ExpectedResultArr ) == False )
        ):
            print " A", A
            print " B", B
            print " Result           :", Result
            print " ExpectedResult   :", ExpectedResult
            print " Single Test Failed"
            FullTestSuccess = False


            #print "str(type(Result)): ", str(type(Result))
            #if ( str(type(Result)) == "<type 'str'>"):
            #    print "len(Result)", len(Result)
            #    print "len(ExpectedResult)", len(ExpectedResult)
            #else:
            #    print "Not a String"

    else:
        print " Single Test Succeded"


    
    k = k + 1


Library_PrintFullTestSuccess.Main(FullTestSuccess)


"""


        #Sign same for each pair of values:
        #if ( len( ElementwiseProduct[ElementwiseProduct < 0] ) > 0  ):
            #ArgumentErrorMessage += "AB pairs must each have the same sign"
            #return numpy.ones(shape = (len(Aarr),)) * float('Inf')

print Library_OrderOfMagnitudeDifference.Main(1, 10)
print Library_OrderOfMagnitudeDifference.Main(10, 1)



    #Take the absolute value of all elements (we know they all have the same sign)
    AB = numpy.absolute(AB)
    #print 'AB', AB

    #Sort each pair of values in place:
    AB.sort(axis = 0)
    #print 'AB', AB

    #Replace the 0 pairs with 1's, 
    #Replace the 0's that are not pairs with really really small numbers 100 orders of mag
    AB[AB == 0.0] = 10**(-100)
    #print 'AB.shape', AB.shape

    k = 0
    for k in range(len(AB) - 1):
        val0 = AB[0][k]
        #print 'val0', val0
        val1 = AB[1][k]
        #print 'val1', val1

        val0closeTo0 = ( val0 <= 10**(-100) )
        print 'val0closeTo0', val0closeTo0
        val1closeTo0 = ( val1 <= 10**(-100) )
        print 'val1closeTo0', val1closeTo0

        if (val0closeTo0 and val1closeTo0):
            AB[0][k] = 1.0
            AB[1][k] = 1.0
        elif (val0closeTo0 and not val1closeTo0):
            AB[0][k] = 10**(-100)
        elif (not val0closeTo0 and val1closeTo0):
            AB[1][k] = 10**(-100)
        elif (not val0closeTo0 and not val1closeTo0):
            pass
        else:
            pass


    #Take the inverse of numbers less than 1 so we can get useful comparison:
    #AB[AB == 0.0] = 1.0/AB[AB == 0.0]




"""




















