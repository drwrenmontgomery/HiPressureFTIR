from pylab import *
from numpy import *

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import fnmatch
import os

def nrmlze(data, scalefactor): 
        return scalefactor+(data-min(data))/(max(data)-min(data))

def noise_to_nan(values):
	return [float('nan') if abs(x)==6 else x for x in values]


#dodecanol_amb=genfromtxt('Load 5 Dodecanol after vs cleaned diamond_0_AB.dpt', delimiter=',')
dodecanol_amb_gb=genfromtxt('Load 5 Dodecanol in air thin film glowbar negative vs cleaned diamond_0_AB.dpt', delimiter=',')

#dodecanol_gb_00=genfromtxt('Load 5 Dodecanol P1 1_5 GPa glowbar_0_AB.dpt', delimiter=',')
dodecanol_gb_01=genfromtxt('Load 5 Dodecanol P1 1_5 GPa glowbar_1_AB.dpt', delimiter=',')

#dodecanol1=genfromtxt('Load 5 Dodecanol P1 1_5 GPa_0_AB.dpt', delimiter=',')
#dodecanol2=genfromtxt('Load 5 Dodecanol P1 1_5 GPa_1_AB.dpt', delimiter=',')
#dodecanol3=genfromtxt('Load 5 Dodecanol P1 1_5 GPa_2_AB.dpt', delimiter=',')


ax = plt.axes()
#ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

#plot(dodecanol_amb[:,0], dodecanol_amb[:,1], 'k-')
plt.plot(dodecanol_amb_gb[:,0], nrmlze(noise_to_nan(dodecanol_amb_gb[:,1]), 0), 'k-')

#plot(dodecanol1[:,0], dodecanol1[:,1], 'k-')
#plot(dodecanol2[:,0], 1+dodecanol2[:,1], 'r-')
#plot(dodecanol3[:,0], 1+dodecanol3[:,1], 'm-')

#plot(dodecanol_gb_00[:,0], dodecanol_gb_00[:,1], 'k-')
plt.plot(dodecanol_gb_01[:,0], nrmlze(noise_to_nan(dodecanol_gb_01[:,1]),1), 'k-')

plt.xlim([600, 3800])
plt.ylim([-0.1, 2.1])
plt.xlabel('wavenumber, cm$^{-1}$')
plt.ylabel('absorbance, a.u.')
plt.grid(which='both')

text(3000, 1.9, 'dodecanol, in DAC, 1.5 GPa')
text(3000, 0.9, 'dodecanol, thin-film, STP')

ax.yaxis.set_major_formatter(plt.NullFormatter())

plt.show()
savefig('dodecanol_ftir_fig_v1.pdf')



