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
        There will be loops
        There will be redudant multiplication which could be worked out by hand and avoided
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

def Main(\
    Point = None, \
    Dataset = None, \
    KernelFunction = Library_Gaussian.Main, \
    BandwidthEstimator = Library_KernelDensityBandwidthSilverman.Main, \
    BandwidthIsVariable = False, \
    PrintExtra = False, \
    CheckArguments = True ,\
    ):

    
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
        if (Dataset == None):
            ArgumentErrorMessage += "(Dataset == None)" + "\n"

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

    CovarianceMatrix = None
    if( BandwidthIsVariable == False ):
        CovarianceMatrix = BandwidthEstimator(Dataset)

    DensityNotNormalized = 0.0
    for Datapoint in Dataset:
        k = 0
        if (BandwidthIsVariable): 
            CovarianceMatrix = BandwidthEstimator(Dataset = Dataset, Point = Point)

        DensityNotNormalized += KernelFunction(\
            Point = Datapoint, \
            MeanPoint = Point, \
            CovarianceMatrix = CovarianceMatrix, \
            PrintExtra = False\
            )
        #print "DensityNotNormalized", DensityNotNormalized

    #print "NumPointsDataset\n", NumPointsDataset, "\n"

    #print "ADAMS DensityNotNormalized\n", DensityNotNormalized, "\n"

    DensityNormalized = DensityNotNormalized*(1.0/NumPointsDataset)

    #print "Function Ended"

    return DensityNormalized
























