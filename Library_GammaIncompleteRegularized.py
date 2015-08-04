import scipy
import scipy.special


#  scipy.special.gammainc(a, x)  = incomplete gamma lower function(a,x) / gamma function(a)
#  scipy.special.gammaincc(a, x) = incomplete gamma upper function(a,x) / gamma function(a)
#  scipy.special.gamma(a)        = gamma function (a)      


def Main(a, x):
    #regularized gamma function = lower incomplete gamme function(a, x) / gamma function(a) 
    #regularized gamma function = scipy.special.gammainc(a, x) 
    return scipy.special.gammainc(a, x) 
    
