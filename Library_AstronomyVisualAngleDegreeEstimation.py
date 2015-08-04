
"""
DESCRIPTION:
    Calculates the visual angle on the sky for a given object
    Assume that distance and rvir have the same units
    
    Note that we are calculating the center of the galactic sphere 
    to be CLOSER than the projected visual sphere for this calculation

ARGS:

RETURNS:


"""
import numpy

def Main(Distance = None, Rvir = None):

    #sin(VisualAngle) = Rvir/Distance

    #VisualAngleRadians = numpy.arctan(Rvir / Distance)
    VisualAngleRadians = numpy.arcsin( Rvir/Distance )
    
    VisualAngleDegrees = numpy.degrees(VisualAngleRadians)

    return VisualAngleDegrees
