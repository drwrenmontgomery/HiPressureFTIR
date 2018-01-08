from pylab import *
from numpy import *
from fnmatch import fnmatch
import os
import re
import sys

def nrmlze(data, scalefactor): 
	return scalefactor+(data[:,1]-min(data[:,1]))/(max(data[:,1])-min(data[:,1]))

iwd=os.getcwd()

offset=0

basedir = sys.argv[1]

dirlist=os.listdir(basedir)
os.chdir(basedir)

# input skip files (easier to just take them out of directory)

# loop

# collect the file numbers
for i in dirlist:
	if fnmatch(i, '*.txt') or fnmatch(i, '*.dat'):
		datat=loadtxt(i, delimiter = ' ') 
		plot(datat[:,0], nrmlze(datat, offset), 'k-')		
		offset=offset+1

	elif fnmatch(i, '*.CSV'): # or fnmatch(i, '*.dat'):
		datat=loadtxt(i, delimiter = ',')
		plot(datat[:,0], nrmlze(datat, offset), 'k-')		
		offset=offset+1

	else:
		continue

xlim([-50+min(datat[:,0]), 200+max(datat[:,0])])
ylim([-.5, offset+1])

yticks([])

show()
# save file to user input file name?


#os.chdir(iwd)

