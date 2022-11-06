# A file to travers a directory recursivley, and return all its contents
from logging import root
import os, sys

# Getting information from CMD
# print(sysargv)

# Dir to travers
rootDir = '/'

# Directory Traversal

# Checking if passed argument is directory
if not os.path.isdir(rootDir):
    print("Invalid Directory => {} ".format(rootDir))
    exit()


flist = []

# Crawling the specified Directory
for root, subfolders, filenames in os.walk(rootDir):
    for f in subfolders:
        if '/bin/' in f:
        #print(fileList)
            with open ('/home/bins.body', 'a') as file:
                file.write(f)
                file.write('\n')

