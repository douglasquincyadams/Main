"""
SOURCES:
    Common knowledge

DESCRIPTION:
    Start with two spheres
        SphereSuface:
             is the sphere which you are projecting onto, and it has a given radius
        ExternalSphere:
             is the sphere which is to be projected

    The method finds a new Sphere, we will denote `SphereNot` 

    SphereNot 
        has all the same proportions as Sphere2,
        has tangent line lies directly on Sphere1

    There exists a right angles:
        Sphere2Center|Sphere2TangentLine|Origin
        SphereNot|SphereNotTangentLine|Origin

    Because the SphereNotTangentLine connects to a point which lies on Sphere1, 
        it has radius == `SphereSurfaceRadius`
    

    NOTE:
        This projection is particularly useful in astronomy, 
        for determining the origin of photons from sources which are spherical in nature

ARGS:
    ExternalSphereCenterDistance

    ExternalSphereRadius

    SphereSurfaceRadius

    ReturnValuesRequired

RETURNS:
    ReturnValues
        Type: Python Dict of floats
        Description:
            Each key correponds to a key given in the arg `ReturnValuesRequired`
            Each value corresponds to the associated key,
            Obvious 2 values which are required for astronomy are default:
                "ProjectedSphereRadius", 
                "ProjectedSphereCenterDistance",

            Others:
                ExternalSphereTangentLineDistance
                ProjectedSphereTangentLineDistance == SphereSurfaceRadius 

                ExternalSphereRadius
                ExternalSphereCenterDistance

                ExternalSphereCentralRadialAngle #This is a visual angle in astronomy
"""
import numpy

def Main(
    ExternalSphereCenterDistance = None, #d
    ExternalSphereRadius = None,         #r
    SphereSurfaceRadius = 1.,          #1
    ReturnValuesRequired = [
        "ProjectedSphereRadius", 
        "ProjectedSphereCenterDistance",
        ],
    CheckArguments = True,
    PrintExtra = False,
    ):


    if (CheckArguments):

        ArgumentErrorMessage = ""
        if (None in  [ExternalSphereCenterDistance, ExternalSphereRadius, SphereSurfaceRadius]):
            ArgumentErrorMessage += "(None in [ExternalSphereCenterDistance, ExternalSphereRadius, SphereSurfaceRadius] )\n"
            ArgumentErrorMessage += 'ExternalSphereCenterDistance==' + str(ExternalSphereCenterDistance) + "\n"
            ArgumentErrorMessage += 'ExternalSphereRadius==' + str(ExternalSphereRadius) + "\n"
            ArgumentErrorMessage += 'SphereSurfaceRadius==' + str(SphereSurfaceRadius) + "\n"

        #Do some type checking:
        FloatType = type(0.0) 
        NumpyArrayType = type(numpy.array([]))
        ExternalSphereCenterDistanceType = type(ExternalSphereCenterDistance)
        ExternalSphereRadiusType = type(ExternalSphereRadius)
        SphereSurfaceRadiusType = type(SphereSurfaceRadius)

        if (not FloatType in [ExternalSphereCenterDistanceType, ExternalSphereRadiusType]):
            if (ExternalSphereCenterDistanceType != ExternalSphereRadiusType):
                ArgumentErrorMessage += "ExternalSphereCenterDistanceType != ExternalSphereRadiusType\n"
            if (ExternalSphereCenterDistanceType != NumpyArrayType ):
                ArgumentErrorMessage += "ExternalSphereCenterDistanceType != NumpyArrayType \n"
            if (ExternalSphereRadiusType != NumpyArrayType ):
                ArgumentErrorMessage += "ExternalSphereRadiusType != NumpyArrayType \n"
            if (ExternalSphereCenterDistance.shape != ExternalSphereRadius.shape):
                ArgumentErrorMessage += "ExternalSphereCenterDistance.shape != ExternalSphereRadius.shape\n"
            if (SphereSurfaceRadiusType != FloatType):
                if (SphereSurfaceRadiusType != NumpyArrayType):
                    ArgumentErrorMessage += ' `ExternalSphereCenterDistance` and `ExternalSphereRadius` are numpy arrays  \n'
                    ArgumentErrorMessage += '   `SphereSurfaceRadiusType` should either be float, or numpy array. \n'
                    ArgumentErrorMessage += '   `SphereSurfaceRadiusType` == ' + str(SphereSurfaceRadiusType) + "\n"
        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)


    
    ReturnValues = {}
    #The following are equal:
    #   ExternalSphereRadius                / ProjectedSphereRadius 
    #   ExternalSphereCenterDistance        / ProjectedSphereCenterDistance
    #   ExternalSphereTangentLineDistance   / ProjectedSphereTangentLineDistance

    #Angles:
    if ("ExternalSphereCentralRadialAngle" in ReturnValuesRequired):
        ExternalSphereCentralRadialAngle = numpy.arctan(ExternalSphereRadius/ ExternalSphereCenterDistance)
        ReturnValues["ExternalSphereCentralRadialAngle"] = ExternalSphereCentralRadialAngle

    #TangentLines    
    ExternalSphereTangentLineDistance = numpy.sqrt(ExternalSphereRadius**2. + ExternalSphereCenterDistance**2.)
    if ("ExternalSphereTangentLineDistance" in ReturnValuesRequired):
        ReturnValues["ExternalSphereTangentLineDistance"] = ExternalSphereTangentLineDistance


    ProjectedSphereTangentLineDistance = SphereSurfaceRadius 
    """
    if (
        type(ExternalSphereCenterDistance) == type(numpy.array([]))
        and
        type(SphereSurfaceRadius) == type(0.0)
        ):
        ProjectedSphereTangentLineDistance = numpy.ones(shape = (len(ExternalSphereCenterDistance), ))
    """  
    if ("ProjectedSphereTangentLineDistance" in ReturnValuesRequired):
        #Should be the SphereSurfaceRadius every time 
        ReturnValues["ProjectedSphereTangentLineDistance"] = ProjectedSphereTangentLineDistance

    #Radii
    if ("ExternalSphereRadius" in ReturnValuesRequired):
        ReturnValues["ExternalSphereRadius"] = ExternalSphereRadius

    ProjectedSphereRadius = ExternalSphereRadius * ProjectedSphereTangentLineDistance / ExternalSphereTangentLineDistance
    if ("ProjectedSphereRadius" in ReturnValuesRequired):
        ReturnValues["ProjectedSphereRadius"] = ProjectedSphereRadius



    #Distances
    if ("ExternalSphereCenterDistance" in ReturnValuesRequired):
        ReturnValues["ExternalSphereCenterDistance"] = ExternalSphereCenterDistance

    if ("ProjectedSphereCenterDistance" in ReturnValuesRequired):
        ReturnValues["ProjectedSphereCenterDistance"] = numpy.sqrt(ProjectedSphereRadius**2. + ProjectedSphereTangentLineDistance**2 )
    


    return ReturnValues

















    












