"""

DESCRIPTION:
    Only works in 1 dimension (right now)

    Hence 'CovarianceMatrix' is really just the variance of a 1d gaussian

    Mean Point  is really just the mean of a 1d gaussian

    This could be fixed to allow for multi-dimensional case... 
        the indefinite integral would be different depending on which dimension is being integrated over
        not a trivial task to perform -> would have to return:
            `newfunction(points with dimensions not including integrated dimension)`
        this would be 
            kinda like a slice, 
            kinda like a marginalization, 
            but not the same thing as either one

ARGS:
        


RETURNS:


"""
import numpy
import scipy
import scipy.stats
import scipy.special
def Main(
    Point = None,
    MeanPoint = None, 
    CovarianceMatrix = None, 
    ):
    
    Part1 = ( 1./ 2. )

    Part2 = 1. + scipy.special.erf(  (Point - MeanPoint)/ (CovarianceMatrix * numpy.sqrt(2)) )

    Result = Part1 * Part2

    return Result















