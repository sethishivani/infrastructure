import os
from os import listdir
from os.path import isfile, join
import heapq
mypath='/home'
onlyfiles =[]
onlyfold=[]
for f in listdir(mypath):
	#fetch all the files and folders in current dir
	if isfile(join(mypath, f))and f[0] != '.' and '.' in f:
		onlyfiles.append(join(mypath, f))
	elif not(isfile(join(mypath, f))) and f[0]!='.':
		onlyfold.append(os.path.join(mypath, f))
#now for each folder check all the files and append it to file list and all folders are appended to folder list
while(onlyfold):
	newfiles=[join(onlyfold[0], f) for f in listdir(onlyfold[0]) if isfile(join(onlyfold[0], f)) and f[0] != '.' and '.' in f]
	onlyfiles.extend(newfiles)
	newfiles=[]
	newfold=[os.path.join(onlyfold[0], f) for f in listdir(onlyfold[0]) if not(isfile(join(onlyfold[0], f))) and f[0]!='.']
	onlyfold.extend(newfold)
	newfold=[]
	del onlyfold[0]
#list of all the files
#print onlyfiles
#list of 10 largest files
big_files = heapq.nlargest(int(10), onlyfiles, key=os.path.getsize)
for i in big_files:
	print i,(os.path.getsize(i)/1048576.0)
