"""
DESCRIPTION:
    Estimates a density function based on observed datasets with a kernel. 

    Wiki:
        http://en.wikipedia.org/wiki/Kernel_density_estimation

    Scipy Implementation:
        https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.gaussian_kde.set_bandwidth.html

    The value add of this implementation, is to not specify or couple, methods, kernels, or datasets
    This function will only take the args and perform a density esitmation on a single point
    Speed of execution is sacrificed with the benefit of readability, and re-use.
        There are loops
        There is redudant multiplication which can be worked out by hand and avoided
        This code will be re-useable && re-tweakable for years to come
    
ARGS:
    Dataset:
        (Type): Type_NumpyTwoDimensionalDataset
        REQUIRED

    KernelFunction:
        (Type): Python Function
        Default: Gaussian
        Must have the following properities:
            ARGS:
                Point
                
            RETURNS:
                Density

    BandwidthEstimator:
        (Type): Python Function
        Default: Silverman Rule Of Thumb (because he invented KDE's)

    CheckArguments:

    PrintExtra:

RETURNS:
    Density:

"""

import numpy
#------------------------------------------------------------------------------
import Library_Gaussian
import Library_KernelDensityBandwidthSilverman
import Type_NumpyTwoDimensionalDataset

def Main(
    Point = None, 
    Dataset = None, 


    KernelFunctionIsGaussian = True,
    #For Gaussian Kernels, the following variables apply:
    BandwidthEstimator = Library_KernelDensityBandwidthSilverman.Main, 
    BandwidthIsVariable = False, 
    CovarianceMatrix = None,
    #CovarianceMatrixIdentityMultiple = None,
    #NumPointsDataset = None,
    #ReturnFunction = False,


    KernelFunction = Library_Gaussian.Main, 

    PrintExtra = False, 
    CheckArguments = True ,
    ):

    if (CheckArguments):
        NumDimPoint = Point.shape[0]
        NumDimDataset = Dataset.shape[1]
        NumPointsDataset = Dataset.shape[0]

    if (PrintExtra):
        print "NumDimPoint\n", NumDimPoint, "\n"
        print "NumDimDataset\n", NumDimDataset, "\n"
        print "NumPointsDataset\n", NumPointsDataset, "\n"

    if (CheckArguments):
        ArgumentErrorMessage = ""
        #Null Arguments:
        if (Point == None):
            ArgumentErrorMessage += "(Point == None)" + "\n"
        if (Dataset == None and CovarianceMatrix == None):
            ArgumentErrorMessage += "(Dataset == None )" + "\n"

        #Point Shape Checking:
        if ( len(Point.shape) != 1 ):
            ArgumentErrorMessage += "( len(Point.shape) != 1 )" + "\n"

        #Dimensions Match for Point and Dataset
        if (NumDimPoint != NumDimDataset):
            ArgumentErrorMessage += "(NumDimPoint != NumDimDataset)" + "\n"
        if (Type_NumpyTwoDimensionalDataset.Main(Dataset) != True):
            ArgumentErrorMessage += "(Type_NumpyTwoDimensionalDataset(Dataset) != True)" + "\n"

        #On any argument errors - throw a message:
        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ARGUMENTS:\n"
                print "-Point\n", Point, "\n"
                print "-Dataset.shape\n", Dataset.shape, "\n"
                print "-KernelFunction\n", KernelFunction , "\n"
                print "-BandwidthEstimator\n", BandwidthEstimator, "\n"
                print "-CheckArguments\n",CheckArguments , "\n"
                print "-PrintExtra\n",PrintExtra , "\n"
            raise Exception(ArgumentErrorMessage)

        if (PrintExtra):
            print "Passed Argument Checking"

    NumPointsDataset = Dataset.shape[0]

    
    DensityNotNormalized = 0.0
    if (KernelFunctionIsGaussian):

        if (CovarianceMatrix == None):
            if( BandwidthIsVariable == False ):
                CovarianceMatrix = BandwidthEstimator(Dataset)

            #raise Exception('Not Implemented')
            #DensityNotNormalized += Library_Gaussian.Main()

        if (PrintExtra):
            print 'CovarianceMatrix'
            print CovarianceMatrix

            print 'Point'
            print Point

        for DatasetPoint in Dataset:
            if (PrintExtra):
                print 'DatasetPoint'
                print DatasetPoint

            Density = Library_Gaussian.Main( 
                Point = Point, 
                MeanPoint = DatasetPoint, 
                CovarianceMatrix = CovarianceMatrix, 
                ) 
            if (PrintExtra):
                print 'Density', Density
            DensityNotNormalized += Density


    else:
        #for Datapoint in Dataset:
        #    #Integral of DensityNotNormalized from -inf kd ball to inf kd ball == 1:
        #    DensityNotNormalized += KernelFunction( Point = Datapoint )
        raise Exception('Not Implemented')

    DensityNormalized = DensityNotNormalized*(1.0/NumPointsDataset)
    
    return DensityNormalized
























