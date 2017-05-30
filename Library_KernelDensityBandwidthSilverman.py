
"""

ARGS:

RETURNS:

REFERENCES:

    https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.gaussian_kde.set_bandwidth.html
    References
    ----------
    .. [1] D.W. Scott, "Multivariate Density Estimation: Theory, Practice, and
           Visualization", John Wiley & Sons, New York, Chicester, 1992.
    .. [2] B.W. Silverman, "Density Estimation for Statistics and Data
           Analysis", Vol. 26, Monographs on Statistics and Applied Probability,
           Chapman and Hall, London, 1986.
    .. [3] B.A. Turlach, "Bandwidth Selection in Kernel Density Estimation: A
           Review", CORE and Institut de Statistique, Vol. 19, pp. 1-33, 1993.
    .. [4] D.M. Bashtannyk and R.J. Hyndman, "Bandwidth selection for kernel
           conditional density estimation", Computational Statistics & Data
           Analysis, Vol. 36, pp. 279-298, 2001.
"""
import numpy

def Main(
    Dataset = None, 
    Point = None, 
    PrintExtra = False, 
    CheckArguments = True ,
    ):
    if (PrintExtra):
        print "Dataset.shape", Dataset.shape

    if (CheckArguments):
        ArgumentErrorMessage = ""
        if (Point != None):
            ArgumentErrorMessage += "(Point != None)"
            ArgumentErrorMessage += "SILVERMAN RULE DOES NOT HAVE VARIABLE BANDWITH"
        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ARGUMENTS:\n"
            raise Exception(ArgumentErrorMessage)

    #print "Dataset", Dataset
    NumberDatapoints = Dataset.shape[0]
    NumberDimensions = Dataset.shape[1]
    SilvermanFactor = numpy.power(NumberDatapoints*(NumberDimensions+2.0)/4.0, -1./(NumberDimensions+4))
    if (PrintExtra):
        print "SilvermanFactor", SilvermanFactor
    CovarianceMatrix = (SilvermanFactor**2) *numpy.cov(Dataset.T, rowvar=1, bias=False)


    return numpy.atleast_2d(CovarianceMatrix)


























