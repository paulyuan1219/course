from os import listdir
from os.path import isfile, join
import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("tool must accept only one argument")
        exit(0)

    mypath = sys.argv[1]
    onlyfiles = sorted([f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith('png')])
    prefix = "image"
    start = 1
    for filename in onlyfiles:
        os.rename(os.path.join(mypath,filename), os.path.join(mypath, '{}_{:03d}.png'.format(prefix, start)))
        start += 1

    newfiles = sorted([join(mypath,f) for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith('png')])
    for x in newfiles:
        print("![]({})".format(x))




 


