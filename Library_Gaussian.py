# -*- coding: utf-8 -*-
"""

SOURCE:

    On Singular Cov:
        Why is a sample covariance matrix singular when sample size is less than number of variables?
        http://stats.stackexchange.com/questions/60622/why-is-a-sample-covariance-matrix-singular-when-sample-size-is-less-than-number

DESCRIPTION:
    The multivariate gaussian:

        Outputs a gaussian density value given a mean and a covariance

        N-Dimensional in nature - thus the args need to be input with logical dimmensions
            * Point.shape == (N,)
            * MeanPohttp://stats.stackexchange.com/questions/60622/why-is-a-sample-covariance-matrix-singular-when-sample-size-is-less-than-numberint.shape == (N,)
            * CovarianceMatrix.shape == (N, N)

    The covariance calculation:

        Covariance calculation in Numpy is based on a different standard of dataset manipulation
           The covariance matrix expects data to look like:
               Alpha = [[Xcoord1, Xcoord2,...Xcoord3], [Ycoord1, Ycoord2, Ycoord3]... ]

           By convention in our code, we have data of the form:
               Beta = [point1 = [Xcoord1, Xcoord2,...], point2, pointN]
        
           Note: 
                Alpha == Beta.Transpose
        
           Because of this data convention difference:
               We will have to massage the data carefully for each function call


    Scipy:

        Scipy Gaussian Source code is here:
            https://github.com/scipy/scipy/blob/master/scipy/stats/_multivariate.py

        Scipy Gaussian Source Code was written by the following engineers:
            Evgeni Burovski     - Physics at Lancaster University Lecturer
            Florian Wilhelm     - KIT Math (Math degree from an engineering technical school)
            Ralf Gommers        - MIT Engineering 
            ChadFulton          - No Info
            Johannes Kulick     - Ph.D Student at Machine Learning and Robotics Lab of Uni Stuttgart
            Joris Vankerschaver - Joris has a Ph.D. in applied mathematics from Ghent University in Belgium


ARGS:


RETURNS:


"""
import numpy
import scipy
import scipy.stats

#------------------------------------------------------------------------------
def Main( 
    Point = None, 
    MeanPoint = None, 
    CovarianceMatrix = None, 
    AllowSingular = True,
    PrintExtra = False, 
    CheckArguments = True,
    Log = False,
    ):

    if (Log):
        return scipy.stats.multivariate_normal.logpdf(
            Point, 
            MeanPoint,  
            CovarianceMatrix, 
            allow_singular = AllowSingular)
    else:
        return scipy.stats.multivariate_normal.pdf(
            Point, 
            MeanPoint,  
            CovarianceMatrix, 
            allow_singular = AllowSingular)

    return None

    if(PrintExtra):
        print '\n\nSTARTING GAUSSIAN EVALUATION\n\n'

    if (CheckArguments):
        ArgumentErrorMessage = ""

        #If floats or integers are passed in -> cast them to numpy arrays
        if (str(type(Point)) in ["<type 'float'>", "<type 'int'>"] ):
            Point = numpy.array([float(Point)])
            #print 'Changed point', Point.shape

        if (str(type(MeanPoint)) in ["<type 'float'>", "<type 'int'>"] ):
            MeanPoint = numpy.array([float(MeanPoint)])
            #print 'Changed MeanPoint', MeanPoint.shape

        if (str(type(CovarianceMatrix)) in ["<type 'float'>", "<type 'int'>"] ):
            CovarianceMatrix = numpy.atleast_2d( numpy.array([float(CovarianceMatrix)]) )
            #print 'Changed CovarianceMatrix', CovarianceMatrix.shape

        # N-dimensional guassians are possible: 
        #   Must assert the variables are in extendable form:
        #       The shape of a meanpoint must of shape == (N,)
        #       The shape of the input Covariance Matrix must be of shape == (N, N)

        if ( len(MeanPoint.shape) != 1 ):
            ArgumentErrorMessage += "( len(MeanPoint.shape) != 1 )" + "\n"
        if ( len(CovarianceMatrix.shape) != 2 ):
            ArgumentErrorMessage += "( len(CovarianceMatrix.shape) != 2 )" + "\n"

        # Shape of the data point passed in could either be many points or one single point
        if ( len(Point.shape) != 1 ):
            if (len(Point.shape) == 2 and Point.shape[1] == MeanPoint.shape[0] ):
                pass #things are ok -> we just have many points passed in to evaluate
            else:
                print 'Point:', Point
                ArgumentErrorMessage += "( len(Point.shape) != 1 )" + "\n"


        
        # Check that number dimensions Match for (Point, MeanPoint, CovarianceMatrix):
        #NumDimPoint = Point.shape[0]
        NumDimMeanPoint = MeanPoint.shape[0] 
        NumDimCovarianceMatrixDown = CovarianceMatrix.shape[0]
        NumDimCovarianceMatrixAcross = CovarianceMatrix.shape[1]
        NumDim = NumDimMeanPoint
        #if (NumDim != NumDimPoint):
        #    ArgumentErrorMessage += "(NumDim != NumDimPoint)"+ "\n"
        if (NumDim != NumDimMeanPoint):
            ArgumentErrorMessage += "(NumDim != NumDimMeanPoint)"+ "\n"
        if (NumDim != NumDimCovarianceMatrixDown ):
            ArgumentErrorMessage += " (NumDim != NumDimCovarianceMatrixDown )"+ "\n"
        if (NumDim != NumDimCovarianceMatrixAcross ):
            ArgumentErrorMessage += "(NumDim != NumDimCovarianceMatrixAcross )"+ "\n"

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
                print "Point", Point
                print "MeanPoint", MeanPoint
                print "CovarianceMatrix", CovarianceMatrix
                print "\n"
                print "NumDim",NumDim
                print "NumDimPoint", NumDimPoint
                print "NumDimMeanPoint", NumDimMeanPoint
                print "NumDimCovarianceMatrixDown", NumDimCovarianceMatrixDown
                print "NumDimCovarianceMatrixAcross", NumDimCovarianceMatrixAcross
                print "CovarianceMatrix.shape", CovarianceMatrix.shape
            raise Exception(ArgumentErrorMessage)

    if( PrintExtra ):
        print "Point", Point
        print "MeanPoint", MeanPoint
        print "CovarianceMatrix", CovarianceMatrix


    if ( len(Point.shape) == 1 ):
        PointDelta = numpy.atleast_2d( Point - MeanPoint ) #Could be many points
        if( PrintExtra ):
            print "PointDelta          \n",  PointDelta 

        PointDeltaTranspose = numpy.matrix.transpose(PointDelta) #Could be many points
        if( PrintExtra ):
            print"PointDeltaTranspose \n", PointDeltaTranspose 
        
        CovarianceMatrixInverse = numpy.linalg.inv(CovarianceMatrix) 
        if( PrintExtra ):    
            print "CovarianceMatrixInverse", CovarianceMatrixInverse

        #Multiple point evaluation good until this line
        Exponent = (-1.0/2.0) *  numpy.dot( 
                PointDelta,
                numpy.dot( 
                    CovarianceMatrixInverse, 
                    PointDeltaTranspose
                    ), 
                )[0][0]
                #axis = 1

        if( PrintExtra ):
            print "Exponent           \n", Exponent

        NormalizationTerm = 1.0 / numpy.sqrt( ((2*3.14159)**NumDim) * numpy.linalg.det(CovarianceMatrix) )
        if( PrintExtra ):    
            print "NormalizationTerm \n", NormalizationTerm

        ResultNotNormalized = numpy.exp( Exponent )
        if( PrintExtra ):    
            print "ResultNotNormalized\n", ResultNotNormalized

        Result = NormalizationTerm * ResultNotNormalized

    else:
        Result = scipy.stats.multivariate_normal.pdf(Point, MeanPoint,  CovarianceMatrix, False)

    return Result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
