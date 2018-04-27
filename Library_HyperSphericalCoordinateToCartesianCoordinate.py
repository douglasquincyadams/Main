"""
SOURCE:
    http://www.ams.sunysb.edu/~wshih/mathnotes/n-D_Spherical_coordinates.pdf
    https://en.wikipedia.org/wiki/N-sphere#Spherical_coordinates
DESCRIPTION:
    Converts coordinate of form:
        (radius, azimuth, inclination1, inclination2, ..., inclination3 )  

        All angles are assumed to be in radians

    Into coordinate of form:
        (x,y,z,w, .... )
ARGS:
    CheckArguments
        Type:
            python boolean
        Description:
            if true, checks the arguments with conditions written in the function
            if false, ignores those conditions
    PrintExtra
        Type:
            python integer
        Description:
            if greater than 0, prints addional information about the function
            if 0, function is expected to print nothing to console
            Additional Notes:
                The greater the number, the more output the function will print
                Most functions only use 0 or 1, but some can print more depending on the number
    HyperSphericalCoordinate
        Type:
            <type 'tuple'>
        Description:
            (radius, azimuth, inclination1, inclination2, ..., inclination3 )  
RETURNS:
    Result
        Type:
            <type 'tuple'>
        Description:
            (x,y,z,w, .... )
"""
import sympy
#-------------------------------------------------------------------------------
def Main(
    HyperSphericalCoordinate= None,
    CheckArguments = True,
    PrintExtra = False,
    ):

    Result = None

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)


    #Extract the relevant pieces of the spherical coordinates:
    Radius = HyperSphericalCoordinate[0]
    Azimuth = HyperSphericalCoordinate[1]
    Inclinations = HyperSphericalCoordinate[2:]

    #Re-order the angles according to wiki:
    HyperSphericalCoordinateAnglesWikiOrder = []
    for Inclination in HyperSphericalCoordinate[2:]:
        print 'Inclination', Inclination
        HyperSphericalCoordinateAnglesWikiOrder.append(Inclination)
    Azimuth = HyperSphericalCoordinate[1]
    HyperSphericalCoordinateAnglesWikiOrder.append(Azimuth)
    print 'HyperSphericalCoordinateAnglesWikiOrder', HyperSphericalCoordinateAnglesWikiOrder


    #loop through each x-coord except for the last and do sins with a cos at the end
    Xall = []
    for Angle, AngleNumber in zip(HyperSphericalCoordinateAnglesWikiOrder, range(len(HyperSphericalCoordinateAnglesWikiOrder))):

        Xi = Radius 
        for Angle in HyperSphericalCoordinateAnglesWikiOrder[:AngleNumber] :
            Xi *= sympy.sin(Angle)

        Xi *= sympy.cos( HyperSphericalCoordinateAnglesWikiOrder[AngleNumber] )

        Xall.append(Xi)

    #Do one last cood with all sins
    Xlast = Radius
    for Angle in HyperSphericalCoordinateAnglesWikiOrder:
        Xlast *= sympy.sin(Angle)

    Xall.append(Xlast)


    if PrintExtra:
        for Xi, Number in zip(Xall, range(len(Xall))):
            print 'X' + str(Number) + ' =', Xi

    Result = Xall
    return Result 



























