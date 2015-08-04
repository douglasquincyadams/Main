"""

DESCRIPTION:
    This file contains 
        some astronomy constants which are accepted for rule of thumb calcuations
        some unit conversions
        some dark matter assuptions in the dark matter J constants
    


"""

h = 0.70 #no units

H0 = 70.0 #km / (sec * MegaParsec) #HUBBLE CONSTANT

RhoCritical_in_gev_per_cm_cubed = 1.05 * (h ** 2.0) * 10.0**(-5.0) #GeV / cm^3

RhoCritical_in_grams_per_cm_cubed = 1.8791 * (h**2.0) * 10.0**(-29.0) #g / cm^3

MassSolar_in_grams = 1.989 * 10.0**33.0 #grams

MegaParsec_in_cm = 3.0856*(10.0**24.0) #cm

KilaParsec_in_cm = MegaParsec_in_cm / 1000.0 #cm

GeV_in_grams = 1.7827 * 10.0**(-24.0) #grams

Km_in_cm = 10.0 ** 5.0 #cm


#DARK MATTER CONSTANTS (These will change over time):

Jsmooth_NormalizationTerm = 1.0 / (  (8.5*KilaParsec_in_cm) * ((0.3 * GeV_in_grams )**2.0)  ) #grams^2 / cm^5
#print "Jsmooth_NormalizationTerm: \n", Jsmooth_NormalizationTerm , "\n"

JClumpyBoostFactor = 10.0 #no units





