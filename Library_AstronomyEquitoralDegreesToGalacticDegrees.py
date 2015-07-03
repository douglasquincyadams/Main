"""
DESCRIPTION:

    Takes in coordinates of J2000 equitorial in degrees
    Gives back galactic cooridnates in degrees

ARGS:
    RightAscensionDegrees
    DeclinationDegrees

RETURNS:
    (l, b) -> in degrees

"""







import astropy
from astropy import units
from astropy.coordinates import SkyCoord


def Main(\
    RightAscensionDegrees = None,   \
    DeclinationDegrees = None,      \
    ):
    Location = astropy.coordinates.SkyCoord(ra = RightAscensionDegrees*units.degree, dec = DeclinationDegrees*units.degree, equinox='J2000')
    return float( Location.galactic.l.degree ), float( Location.galactic.b.degree)



