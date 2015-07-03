"""
SOURCES:
    http://en.wikipedia.org/wiki/Atan2
    http://en.wikipedia.org/wiki/Spherical_coordinate_system#Coordinate_system_conversions

DESCRIPTION:

    Convertes spherical coordinates to cartesian coordinates
    Does NOT mention `Theta` or `Phi`
        Avoid convention confusion betweemn physics and mathematics
 
ARGS:
    Radius
        Type: 
            Python Float
        Description:
            Radius / distance from the origin
            [0 < R < inf]

    Inclination
        Type: 
            Python Float
        Description:
                Angle between XY plane and the Z+ axis
            [0 < Theta < pi]
    Azimuth
        Type: 
            Python Float
        Description:
                Angle between X+ axis and the XY coordinate of the point
                Rotates around the Z axis

            [0 < Phi < 2pi]

RETURNS:
    X:
        Type: Python Float
        Description: Coordinate along an X axis in 3D space
    Y:
        Type: Python Float
        Description: Coordinate along an Y axis in 3D space
    Z:
        Type: Python Float
        Description: Coordinate along an Z axis in 3D space
"""
import numpy


def Main(
    Radius              = None,
    Inclination         = None,
    Azimuth             = None,
    CheckArguments      = True,
    ):

    X = Radius * numpy.sin(Inclination) *  numpy.cos(Azimuth)
    Y = Radius * numpy.sin(Inclination) *  numpy.sin(Azimuth)
    Z = Radius * numpy.cos(Inclination)
    return X, Y, Z
























