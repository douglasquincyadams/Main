

import numpy
import pprint
import collections
#------------------------------------------------------------------------------
import Library_GeometrySphereSurfaceProjectExternalSphere
import Library_OrderOfMagnitudeRatio
import Library_TestLooper
import Library_PrintFullTestSuccess
FullTestSuccess = True

pi = numpy.pi


ArgSetExpectedResultCombos = []

ArgSet1 = {
"ExternalSphereCenterDistance"  : numpy.sqrt(3.), #d
"ExternalSphereRadius"          : 1., #r
"SphereSurfaceRadius"           : 1.,   #1
"ReturnValuesRequired" : [
    "ExternalSphereCentralRadialAngle", 
    "ExternalSphereTangentLineDistance",
    "ProjectedSphereCenterDistance",
    "ProjectedSphereRadius", 
    ]
}
ExpectedResult1 = {
    "ExternalSphereCentralRadialAngle" : 30 * pi / 180.,
    "ExternalSphereTangentLineDistance" : 2.0,
    "ProjectedSphereCenterDistance" : 1.118 ,
    "ProjectedSphereRadius" : 0.5, 
}
ArgSetExpectedResultCombos.append( (ArgSet1, ExpectedResult1) )

ArgSet2 = {
"ExternalSphereCenterDistance"  : numpy.array( [numpy.sqrt(3.), numpy.sqrt(3.)] ), #d
"ExternalSphereRadius"          : numpy.array( [1., 1.] ), #r
"SphereSurfaceRadius"           : numpy.array( [1., 1.] ),   #1
"ReturnValuesRequired" : [
    "ExternalSphereCentralRadialAngle", 
    "ExternalSphereTangentLineDistance",
    "ProjectedSphereCenterDistance",
    "ProjectedSphereRadius", 
    ]
}
ExpectedResult2 = {
    "ExternalSphereCentralRadialAngle" : numpy.array([30 * pi / 180., 30 * pi / 180.]),
    "ExternalSphereTangentLineDistance" : numpy.array([2.0, 2.0]) ,
    "ProjectedSphereCenterDistance" : numpy.array([1.118, 1.118]) ,
    "ProjectedSphereRadius" : numpy.array([ 0.5, 0.5 ]), 
}
ArgSetExpectedResultCombos.append( (ArgSet2, ExpectedResult2) )



ArgSet2 = {
"ExternalSphereCenterDistance"  : numpy.array( [numpy.sqrt(3.), numpy.sqrt(3.)] ), #d
"ExternalSphereRadius"          : numpy.array( [1., 1.] ), #r
"SphereSurfaceRadius"           : 1.,   # Expected to be broadcast accross arrays
"ReturnValuesRequired" : [
    "ExternalSphereCentralRadialAngle", 
    "ExternalSphereTangentLineDistance",
    "ProjectedSphereCenterDistance",
    "ProjectedSphereRadius", 
    ]
}
ExpectedResult2 = {
    "ExternalSphereCentralRadialAngle" : numpy.array([30 * pi / 180., 30 * pi / 180.]),
    "ExternalSphereTangentLineDistance" : numpy.array([2.0, 2.0]) ,
    "ProjectedSphereCenterDistance" : numpy.array([1.118, 1.118]) ,
    "ProjectedSphereRadius" : numpy.array([ 0.5, 0.5 ]), 
}
ArgSetExpectedResultCombos.append( (ArgSet2, ExpectedResult2) )


Library_TestLooper.Main(
    FunctionToTest = Library_GeometrySphereSurfaceProjectExternalSphere.Main,
    ArgSetExpectedResultCombos = ArgSetExpectedResultCombos,
    OrderOfMagnitudeRatioMax = 0.01,
    HardDifferenceMax = 0.001,
    PrintExtra = False,
    )














