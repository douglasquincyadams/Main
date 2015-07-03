"""
SOURCE:
    Written by Stephan Zimmer -> Feb 2015 -> Oskar Klein Center For Theoretical Physics

DESCRIPTION:
    Makes some quick plots and pulls data from the fermi files on the local disk




"""


import pyfits
import matplotlib.pylab
import matplotlib.pyplot as plt
import numpy as np

import Const_LocalDirectoriesFermiFiles
import Const_MiscellaneousDirectories
folderpath = Const_LocalDirectoriesFermiFiles.DataFilesCutsDirectory
filename = "filtered_events_10GeV_1TeV_zmax100_GTI_ultraclean.fits"
filepath = folderpath + "/" + filename

pp, header = pyfits.getdata(filepath,1,header=True)
evfile = np.array(pp)
pp.columns


highEdata = evfile[np.where(evfile["ENERGY"]>=4e4)]

plane_cut = np.where(np.abs(highEdata['B'])>=20.)


fig, ax = plt.subplots(ncols=1,nrows=1)

bins = 100
ax.hist(np.log10(highEdata["ENERGY"]),bins=bins,log=True,label='all sky n=%i'%len(highEdata),histtype='step')
ax.hist(np.log10(highEdata["ENERGY"][plane_cut]),bins=bins,log=True,label='|b|>20 n=%i'%len(highEdata[plane_cut]),histtype='step')
ax.legend(loc='best')
#ax.set_xlabel('Log10Energy')
#ax.set_ylabel('Log10Counts')
plt.draw()

_3fgl = pyfits.getdata( Const_LocalDirectoriesFermiFiles.DataPointSourcesDirectory +"/gll_psc_v14.fit",1)


sigma = np.array(_3fgl["Signif_Avg"],dtype=float)
sigma = sigma[np.where(np.isfinite(sigma))]

bins = np.linspace(np.min(sigma),np.max(sigma),100)

fig, ax = plt.subplots(ncols=1,nrows=1)
plt.hist(sigma,bins=bins,log=True)

plt.draw()


plt.show()



















