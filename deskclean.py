import os
from os import listdir
from os.path import isfile, join
import heapq
checkpath=os.environ["HOME"]+'/Desktop/'
mypath=os.environ["HOME"]+'/Documents/'
for f in listdir(checkpath):
	if isfile(join(checkpath, f))and f[0:2] != '._' and '.' in f:
		loc=f.find('.')
		foldname=f[loc+1:]
		nfn=join(mypath,foldname, f)
		directory =os.path.dirname(nfn)
		if not os.path.exists(directory):
		    os.makedirs(directory)
		os.rename(join(checkpath, f), nfn)