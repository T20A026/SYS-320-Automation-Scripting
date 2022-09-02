# Create interface for searching through logs
import re, sys

def _syslog(filename,listOfKeywords):

    # Open a file 
    with open(filename) as f:
        #read in the file and save the output into a variable
        contents = f.readlines()

    # List of Results
    results = []

    # loop through the list and return the entries in each line
    for line in contents:

        # Loops through keywords
        for eachKeyword in listOfKeywords:

            #if the line contains the keyword it is printed out
            #if eachKeyword in line:
            x = re.findall(r''+eachKeyword+'', line)

            for found in x:
                #Appending returned values to the results list
                results.append(found)

    #Check to see if results are present
    if len(results) == 0:
        print("No Results")
        sys.exit(1)

    #Sort
    results = sorted(results)
    return results

            #print(x) 
