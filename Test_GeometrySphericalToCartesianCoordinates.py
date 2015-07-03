import numpy
import pprint
#------------------------------------------------------------------------------
import Library_GeometrySphericalToCartesianCoordinates
import Library_TestLooper

pi = numpy.pi

ArgSetExpectedResultCombos = []

ArgSet1 = {
    "Radius" : 1.,
    "Inclination" : pi/2.,
    "Azimuth" : pi/2.,
}
ExpectedResult1 = [0,1,0]
ArgSetExpectedResultCombos.append( (ArgSet1, ExpectedResult1) )
"""
ArgSet2 = {
    "Radius"        : 1.,
    "Inclination"   : pi/4.,
    "Azimuth"       : pi/4.,
}
ExpectedResult2 = [0.,1.,0.]
ArgSetExpectedResultCombos.append( (ArgSet2, ExpectedResult2) )
"""

Library_TestLooper.Main(
    FunctionToTest = Library_GeometrySphericalToCartesianCoordinates.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = float('Inf'),
    HardDifferenceMax = 0.01,
    PrintExtra = False,
    )















