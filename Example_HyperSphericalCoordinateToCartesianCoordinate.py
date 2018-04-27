import numpy
import Library_HyperSphericalCoordinateToCartesianCoordinate


ExampleHyperSphericalCoordinate = (numpy.sqrt(3), .78, 0.955)


#ExampleHyperSphericalCoordinate = (100,1,2,3,4,5,6,7,8)
print 'ExampleHyperSphericalCoordinate', ExampleHyperSphericalCoordinate

Result = Library_HyperSphericalCoordinateToCartesianCoordinate.Main(
    HyperSphericalCoordinate= ExampleHyperSphericalCoordinate
    )
print Result , 'expected (1,1,1)'

















































