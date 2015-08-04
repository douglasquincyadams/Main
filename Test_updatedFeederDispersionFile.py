#!/usr/bin/env python


import Library_DataGetFermiInstrumentResponseEnergyDispersionFunction as Reader

import matplotlib.pyplot as plt
import numpy as np


def main():


    DMMass=1.e5
    WindowMinimumEnergy=DMMass/3.
    WindowMaximumEnergy=DMMass*3.
    Spline=Reader.Main(     SourceEnergy=DMMass,
                            WindowMinimumEnergy=WindowMinimumEnergy,
                            WindowMaximumEnergy=WindowMaximumEnergy,
                            PrintExtra = False,
                      )
    xpoints=np.linspace(DMMass/1.3,DMMass*1.3,300)
    plt.plot(xpoints,Spline(Energy=xpoints))
    plt.show()
    return
    


if __name__ == '__main__':
    main()


