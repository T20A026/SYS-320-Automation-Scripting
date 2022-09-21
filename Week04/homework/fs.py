# A file to travers a directory recursivley, and return all its contents
import os, argparse


#parser
parser = argparse.ArgumentParser(

    description="Traverses directories and builds a forensic body file",
    epilog="Developed by Abijah 9/21/22"
)


# Add an argument to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")

# parse the arguments
args = parser.parse_args()

rootDir = args.directory

# Getting information from CMD
# print(sysargv)

# Directory Traversal

# Checking if passed argument is directory
if not os.path.isdir(rootDir):
    print("Invalid Directory => {} ".format(rootDir))
    exit()


flist = []

# Crawling the specified Directory
for root, subfolders, filenames in os.walk(rootDir):
    for f in filenames:
        #print(root + "\\" + f)
        fileList = root + "\\" + f
        #print(fileList)
        flist.append(fileList)

def statFile(toStat):
    # i is going to be the var, used for each metadata dumps
    i = os.stat(toStat, follow_symlinks=False)

    # mode
    mode = i[0]

    # inode
    inode = i[1]

    # uid
    uid = i[4]

    # gid
    gid = i[5]

    # file size
    fsize = i[6]

    # access time
    atime = i[7]

    # modification time
    mtime = i[8]
    
    # ctime => windows is the birth of the file
    # linux is the time scince last attribute change
    ctime = i[9]
    crtime = i[9]

    print("0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(toStat, inode, mode, uid, gid, fsize, atime, mtime, ctime, crtime))

for eachFile in flist:

    statFile(eachFile)