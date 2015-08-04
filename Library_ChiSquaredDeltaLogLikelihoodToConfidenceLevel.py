"""
#Note:
#   Description:
#       Chi-Squared CDF
        
        -2 * DeltaLogLikelihood      !!!   -> Minus Two is in here
#
#   This is NOT the same thing as a "regularlized gamma function"
#   This function is very close to the "regularlized gamma function"
#       but divides the args by 2 -> thus formatting it to be exactly == 
#       the CDF of the Chi-Squared
#
"""

import Library_GammaIncompleteRegularized

def Main(NumDimensions, DeltaLogLikelihood):
    return Library_GammaIncompleteRegularized.Main(NumDimensions/2.0, (-2.0*DeltaLogLikelihood)/2.0)


    
