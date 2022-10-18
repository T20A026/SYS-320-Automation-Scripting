#Abijah Buttendorf, 
# A file to travers a directory recursivley, and searches the logs it contains for entries based on a specifies option
import os, argparse, re, sys, csv
import yaml

try:
    with open('searchTerms.yaml', 'r') as thefile:
        keywords = yaml.safe_load(thefile)
except EnvironmentError as e:
    print(e.strerror)

# Calling parser, and adding description
parser = argparse.ArgumentParser(

    description="Traverses directories and builds a forensic body file",
    epilog="Developed by Abijah 9/21/22"
)


# Add an arguments to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
parser.add_argument("-s", "--search", required="True", help="Specify Search Terms: 'powershell', 'javaSearch', 'reg'")

# parse the arguments
args = parser.parse_args()
rootDir = args.directory
searchTerms = keywords[args.search]

# Getting information from CMD
# Checking if passed argument is directory
if not os.path.isdir(rootDir):
    print("Invalid Directory => {} ".format(rootDir))
    exit()

# Define flist for outputs
flist = []

# Crawling the specified Directory
for root, subfolders, filenames in os.walk(rootDir):
    for f in filenames:
        fileList = root + "\\" + f
        flist.append(fileList)

def _syslog(filename,service):
    #Query the Ymal for the terms specified inside
    #Service is main, term is sub
    terms = service

    #Split the etries by the commas
    listOfKeywords = terms.split(", ")

    # Open a file 
    results = []

    with open(filename, encoding='utf-8') as file:
        
        contents = csv.reader(file)
        
        for _ in range(1):
            next(contents)
        for line in contents:
            
            for eachKeyword in listOfKeywords:
                #if the line contains the keyword it is printed out
                #if eachKeyword in line:
                x = re.findall(r''+eachKeyword+'', ' '.join(line))

                for found in x:

                    #Appending returned values to the results list
                    results.append(found)

    #Check to see if results are present

    #Sort the results by alphebetical 
    results = sorted(results)
    cleanResults = []

    #Print the results to the cli, in a nice format
    for line in results:
        print("""
            file: {}
            line: {}
        """.format(filename, line))
    
    return cleanResults
#call for _syslog
for f in flist:
    _syslog(f, searchTerms)