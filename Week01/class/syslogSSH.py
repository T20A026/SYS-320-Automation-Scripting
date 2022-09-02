import syslogCheck
import importlib
importlib.reload(syslogCheck)

# SSH authentication failures
def ssh_fail(filename, searchTerms):

    #Call syslogCheck file
    is_found = syslogCheck._syslog(filename, searchTerms)

    #found list
    found = []
    
    #Loops results
    for eachFound in is_found:
        #Split Results
        sp_results = eachFound.split(" ")

        #Append the split values to found

        found.append(sp_results[8])

    #Removes Duplicates with set
    hosts = set(found)

    #print results
    for eachHost in hosts:

        print(eachHost)