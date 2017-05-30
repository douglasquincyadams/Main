import astropy
import astropy.cosmology 
import Config_AstronomyConstants as astroconst 

def Main(Redshift = None):
    Z = Redshift
    cosmo = astropy.cosmology.FlatLambdaCDM(H0=70.0, Om0=0.3)
    Distance_in_MegaParsecs =  cosmo.comoving_distance(Z)  
    Distance_in_cm = Distance_in_MegaParsecs * astroconst.MegaParsec_in_cm * (1.0 + Z)
    return Distance_in_cm.value
