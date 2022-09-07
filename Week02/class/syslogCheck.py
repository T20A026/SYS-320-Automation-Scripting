# Create interface for searching through logs
import re, sys, yaml

# Open the yaml file
try:
    with open('searchTerms.yaml', 'r') as yf:
        keywords = yaml.safe_load(yf)
except EnvironmentError as e:
    print(e.strerror)

def _syslog(filename,service,term):

    #Query the Ymal for the terms specified inside
    #Service is main, term is sub
    terms = keywords[service][term]

    #Split the etries by the commas
    listOfKeywords = terms.split(",")

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
