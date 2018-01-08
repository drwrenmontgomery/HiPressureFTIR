import os
import re
import fnmatch
from pylab import *

%these numbers change depending on the wavenumber region you need to truncate

start_num=7675
end_num=13898

basedir = sys.argv[1]

dirlist=os.listdir(basedir)

for i in dirlist:
        if fnmatch.fnmatch(i, '*.CSV'):

		f_handle=open(basedir+'truncated/'+i, 'a')
		
		data=loadtxt(basedir+i, delimiter=',')
		newdata=data[start_num:end_num]

		savetxt(f_handle, newdata, delimiter=',', newline='\n')

		f_handle.close()
		
