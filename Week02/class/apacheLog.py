import syslogCheck
import importlib
importlib.reload(syslogCheck)

# SSH authentication failures
def appache_events(filename, service, term):

    #Call syslogCheck file
    is_found = syslogCheck._syslog(filename, service, term)

    #found list
    found = []
    
    #Loops results
    for eachFound in is_found:
        #Split Results
        sp_results = eachFound.split(" ")

        #Append the split values to found
        found.append(sp_results[0] + " " + sp_results[3] + " " + sp_results[1])

    #Removes Duplicates with set
    hosts = set(found)

    #print results
    for eachHost in hosts:

        print(eachHost)