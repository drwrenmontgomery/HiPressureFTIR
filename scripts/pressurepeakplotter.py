from pylab import *
from numpy import *
from fnmatch import fnmatch
import os
import re
import sys

iwd=os.getcwd()


basedir = sys.argv[1]

dirlist=os.listdir(basedir)

os.chdir(basedir)


for arf in dirlist:
	if fnmatch(arf, 'allpeaksandamps.csv'):
		peaks=genfromtxt(arf, delimiter=',')
		pressure=peaks[:,0]
		maxp=max(pressure)

		for i in range(1, size(peaks, 1), 2):
			plot(pressure, peaks[:,i], 'ko')

	elif fnmatch(arf, 'allpeaksandamps_D.csv'):
		peaks=genfromtxt(arf, delimiter=',')
                pressure=peaks[:,0]
                
                for i in range(1, size(peaks, 1), 2):
                        plot(pressure, peaks[:,i], 'ro')#, mfc='none') 

xlim([0.5, maxp+0.5])

show()
savefig('allpeaks.pdf')

os.chdir(iwd)

