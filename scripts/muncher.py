import os
import fnmatch
from pylab import *

iwd=os.getcwd()

variable='.peaks'

basedir = sys.argv[1]

f_handle = file(basedir+'/allpeaksandamps.csv', 'a')

dirlist=os.listdir(basedir)

os.chdir(basedir)

for i in dirlist:
	if fnmatch.fnmatch(i, '*.peaks'):
		filename=i.split(variable)[0]
		print i
		file = open(i)
		lines = [line.rstrip('\r\n') for line in file.readlines()]
		tokensets = [array(line.split()) for line in lines[1:] if len(line) > 0]
		pairs = array([tokens[[2,3]] for tokens in tokensets])
		values = array(map(float,pairs.reshape(-1))).reshape(-1,2)
#		print values
		data = array(sorted(values, cmp=lambda a,b: cmp(a[0],b[0])))
		savetxt(f_handle, data.reshape(1,-1), delimiter=',', newline='\n')

f_handle.close() 

os.chdir(iwd)
