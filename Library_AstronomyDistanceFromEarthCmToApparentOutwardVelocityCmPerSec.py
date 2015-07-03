

import Config_AstronomyConstants as astroconst 

#def Velocity_From_Distance(distance_in_cm):
def Main(DistanceCm = None):
    distance_in_cm = DistanceCm
    distance_in_MegaParsecs = distance_in_cm / astroconst.MegaParsec_in_cm
    velocity_in_km_per_sec = distance_in_MegaParsecs * astroconst.H0
    velocity_in_cm_per_sec = velocity_in_km_per_sec * astroconst.Km_in_cm
    return velocity_in_cm_per_sec

