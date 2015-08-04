"""
Description: 
    Evaluates multiple functions at multiple points, 
    
Returns:
    Result:
        Type: `Type_OneDimensionalNumpyDataset`
        Description:
            Each value is the Sum accross functions (datapoint )
            ==
            [ 
                F1(x1) + F2(x1) + ... + FN(x1),
                F1(x2) + F2(x1) + ... + FN(x1),
                .
                .
                .
                F1(xk) + F2(x1) + ... + FN(x1),                
            ]

"""


import numpy
#------------------------------------------------------------------------------
import Library_EvaluateFunctionAtNumpyDataPoint


def Main(
    DataPoints  = None, 
    Functions = None,
    Coefficients = None, 
    CheckArguments = True,
    PrintExtra = False,
    ):
    if (PrintExtra):
        print 'DataPoints', DataPoints

    if (CheckArguments):
        ArgumentErrorMessage = ""
        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage

            raise Exception(ArgumentErrorMessage)

    NumberFunctions = len(Functions)
    NumberDataPoints = len(DataPoints)
    if (PrintExtra):
        print 'NumberDataPoints', NumberDataPoints

    if (Coefficients == None):
        Coefficients = numpy.ones(shape = (NumberFunctions,))

    ResultMatrix = numpy.zeros(shape = ( NumberDataPoints, NumberFunctions ) )
    k = 0
    while (k < NumberDataPoints ): 
        DataPoint = DataPoints[k]
        j = 0
        while (j < NumberFunctions ) :
            Function = Functions[j]
            Coefficient = Coefficients[j]

            ResultMatrix[k][j]  = Library_EvaluateFunctionAtNumpyDataPoint.Main(
                Function = Function, 
                Coefficient = Coefficient, 
                DataPoint = DataPoint,
                PrintExtra = PrintExtra,
                )


            #if (ResultMatrix[k][j] == Coefficient):
            #    print 'FAIL'
            #    print 'Coefficient', Coefficient
            #    print 'Function',Function
            #    print 'DataPoint', DataPoint

            j = j + 1

        k = k + 1

    return ResultMatrix






























