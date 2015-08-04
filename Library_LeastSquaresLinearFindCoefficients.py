"""
SOURCE:
    http://en.wikipedia.org/wiki/Linear_least_squares_(mathematics)
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.lstsq.html

    http://en.wikipedia.org/wiki/Linear_least_squares_(mathematics)

DESCRIPTION:

    Intro:
        This is used to solve for a function of linear terms which best models some data
        The function is linear because it must be of the form:
            F = Af1(x) + Bf2(x) + Cf3(x) + ... Zfz(x) 
        Thus the function can be represented as a dot product between 
            the terms evaluated at x: f1(x), f2(x), ... etc
            AND
            the coefficients: A, B ... etc

            F = (A, B, C, ... , Z ) dot (f1(x),f2(x),f3(x), ... , fz(x) )

        We are Predeterimining the f's 
            (There is NO mathematical automagic smart choice for the f's)
        We are SOLVING for the Coefficients (A, B, C...Z)
            (There IS mathematical automagic smart choice for the ABC's)
    
        When finished, it is expected that the ABC's are the `best` choice for modeling the data
            given that the f's were predetermined
            these `best` ABC's are returned


    Args:
        The Dataset is N dimensions, and can be represented with by a `Type_NumpyTwoDimensionalDataset`
        The FitFunction is a function of datapoints with N - 1 dimensions and is a model for the whole Dataset


    Define `FunctionDimension`
        This dimension of the dataset is treated as a function of the other dimensions

        In probability:
            The natural cadidate for a `Function Dimension` is the probability density values
            The other dimensions would concrete observations

    Define `RealObservationInput`
        to return the DataPoint values in the dimeions not designated as `FunctionDimension`

    Define `RealObservationInputs`
        To be the evaluation of the `RealObservationInput` function
            for each of N datapoints
            for each of the M dimensions of the dataset minus the `FunctionDimension`
            shape = (N, M -1)

    Define `RealObservationValue( DataPoint )` 
        to return the DataPoint value in the `FunctionDimension`

    Define `RealObservationValues`
        To be the evaluation of the `RealObservationValue` function
            for each of N datapoints
            shape = (N,)


    Define `FitFunction( DataPoint )` 
        The function takes INPUT from the portion of a datapoint NOT from `FunctionDimension` 
            (uses the values from the other dimensions)
        The function returns OUTPUT data in the `FunctionDimension`    
            Denote this as `FitFunction OUTPUT`

        The other dimensions of the dataset are treated as inputs to the Function we search for.

    We are solving for the function which returns the least `Error` between:
        The observed `Function Dimension` Points
        AND
        The `FitFunction OUTPUT` 

    Error =  ( FitFunction(RealObservationInput1) - RealObservationValue(RealObservationInput1) ) ^ 2
            +( FitFunction(RealObservationInput2) - RealObservationValue(RealObservationInput2) ) ^ 2
            .
            .
            .
            +( FitFunction(RealObservationInputN) - RealObservationValue(RealObservationInputN) ) ^ 2

    In the linear coeficient case (Linear Least Squares)
        Define `CoefficientMatrix`
            To be the evaluation of the `FitFunction` 
                for each of K terms
                for each of N datapoints
                with coeficients all set to 1
                shape == (N, K)


        It can be shown that mathematically, the `FitFunction` with the least `Error` has:
            Coefficients == (CoefficientMatrix.Transpose * CoefficientMatrix).inverse* CoefficientMatrix.Transpose * RealObservationValues
            And, "numpy.linalg.lstsq"  performs these matrix multiplications efficiently


ARGS:

    Dataset:
        Type: `Type_NumpyTwoDimensionalDataset`
        Description:
            [
            [dim1_coord1, dim2_coord2, ... dimK_coordN]
            [dim1_coord1, dim2_coord2, ... dimK_coordN]
            .
            .
            .
            [dim1_coord1, dim2_coord2, ... dimK_coordN]
            ]

    FunctionDimension:
        Type: Python Int
        Description:
            A number between 1, and N inclusive
            Determines which dimension to be though of as a function of the others

    FitFunction:
        Type: Python List of Python Functions:
        Description:
            [function1(x), function2(x), ... functionN(x)]


RETURNS:
    Coefficients:
        type: numpy array of numpy float64's
        description: list of coeffiecients corresponding to the `FitFunction` s terms
            Should be exactly the same length as the `FitFunction` array

"""

import numpy
import pprint
#------------------------------------------------------------------------------
import Library_EvaluateFunctionsAtNumpyDataPoints
#def get_least_squares_coefs(dataset_transpose, lambda_list):
def Main(
    Dataset = None,
    FunctionDimension = None, 
    FitFunction = None,   
    PrintExtra = False,
    ):
    if (PrintExtra):
        print '\nSTARTING A LEAST SQUARES FIT...'

    #Extract the dataset values which we consider to be `outputs` from the function we are looking for
    RealObservationValues = Dataset.T[FunctionDimension]
    if (PrintExtra):
        print 'RealObservationValues'
        pprint.pprint( RealObservationValues )

    #Extract the dataset values which we consider to be `inputs` to the function we are looking for
    RealObservationInputs = numpy.delete( Dataset, (FunctionDimension), axis = 1 )
    if (PrintExtra):
        print 'RealObservationInputs'
        pprint.pprint(  RealObservationInputs     )

    #Generate the CoefficientMatrix (Evalutuate each of the functions on each of the datapoints):
    CoefficientMatrix = Library_EvaluateFunctionsAtNumpyDataPoints.Main(RealObservationInputs, FitFunction)
    if (PrintExtra):
        print 'CoefficientMatrix'
        pprint.pprint( CoefficientMatrix )

    #Built in numpy least squares to calculate:
    #Coefficients == (CoefficientMatrix.Transpose * CoefficientMatrix).inverse * CoefficientMatrix.Transpose * RealObservationValues
    #   NOTE: Built in least squares fucks up on small numbers.  ( 10^-30  * 10^-30 ) == 0 ... FUCK that
    #Coefficients = numpy.linalg.lstsq(CoefficientMatrix, RealObservationValues )[0]

    Step1 = numpy.dot( CoefficientMatrix.T, CoefficientMatrix )
    if (PrintExtra):
        print 'Step1'
        pprint.pprint( Step1 ) 

    Step2 = numpy.linalg.inv(Step1)
    if (PrintExtra):
        print 'Step2'
        pprint.pprint( Step1 ) 

    Step3 = numpy.dot( Step2 , CoefficientMatrix.T )
    if (PrintExtra):
        print 'Step3'
        pprint.pprint( Step1 ) 

    Step4 = numpy.dot( Step3 , RealObservationValues )
    if (PrintExtra):
        print 'Step4'
        pprint.pprint( Step1 ) 


    Coefficients = Step4

    if (PrintExtra):
        print 'Coefficients'
        pprint.pprint(  Coefficients )

    return Coefficients





