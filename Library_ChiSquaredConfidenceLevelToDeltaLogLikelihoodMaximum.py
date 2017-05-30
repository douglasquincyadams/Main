
"""

DESCRIPTION:
    Starts with a chi-squared function
        Number of Dimensions is an argument

    Starts with a Confidence Level
    
    Looks for x-values of the Chi-Squared which grant the desired Confidence Level


    Our Search is the same thing as taking the Inverse Chi-Squared ( Xvalue )

        scipy.stats.chi2.isf(q, df, loc=0, scale=1)
        df = degrees of freedom
        q = confidence level


ARGS:

    ConfidenceLevel
        Type: Python Float
        Description:
            The desired confidence level on which to look for input values 
            to the Chi-Squared density function

    NumDimensions
        Type: Python Int
        Description:
            Number of degrees of freedom describing the Chi-Squared cumulative distribution function

RETURNS:
    
    XValue(s):
        Type: Python Float 
        Description:
            x-values of the Chi-Squared which grant the desired Confidence Level

"""

#import Library_GammaIncompleteRegularized
import numpy
import scipy
import scipy.optimize
#from scipy.optimize import minimize


def Main(
    NumDimensions = None, 
    ConfidenceLevel = None
    ):
    XpointWhereChiSquaredCumulativeDistributionEqualsConfidenceLevel = scipy.stats.chi2.isf(ConfidenceLevel, NumDimensions, loc=0, scale=1)

    #XpointWhereChiSquaredCumulativeDistributionEqualsConfidenceLevel = 0
    return XpointWhereChiSquaredCumulativeDistributionEqualsConfidenceLevel
    





