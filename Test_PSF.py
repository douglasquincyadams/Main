#!/usr/bin/env python


import Library_PSF
import matplotlib.pyplot as plt
import numpy as np

def Main():

    PSFspline100GeV=Library_PSF.Main(DMMass=1e5,ConfidenceLevel=0.95)
    PSFspline1GeV=Library_PSF.Main(DMMass=1e5,ConfidenceLevel=0.90)

    r200=np.linspace(0,2,100)
    plt.plot(r200,PSFspline100GeV(r200),c='blue')
    plt.plot(r200,PSFspline1GeV(r200),c='green')
    plt.show()
    

    

    





if __name__ == '__main__':
    Main()
