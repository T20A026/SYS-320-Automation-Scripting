import syslogCheck
import importlib
importlib.reload(syslogCheck)

# SSH authentication failures
def su_open(filename, searchTerms):

    #Call syslogCheck file
    is_found = syslogCheck._syslog(filename, searchTerms)

    #found list
    found = []
    
    #Loops results
    for eachFound in is_found:
        #Split Results
        sp_results = eachFound.split(" ")

        #Append the split values to found

        found.append(sp_results[5])

    #Removes Duplicates with set
    returnedValues = set(found)

    #print results
    for eachValue in returnedValues:

        print(eachValue)