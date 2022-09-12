import syslogCheck
import importlib
import re
import yaml
importlib.reload(syslogCheck)

# SSH authentication failures
def proxy_closed(filename, service, term):

    #Call syslogCheck file
    is_found = syslogCheck._syslog(filename, service, term)

    #found list
    found = []
    
    #Loops results
    for eachFound in is_found:
        #Split Results
        sp_results = eachFound.split(" ")

        #Append the split values to found
        if bool(re.search(r"\(", sp_results[6])):
            sp_results.remove(sp_results[5])
            sp_results.remove(sp_results[5])
            found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[4] + " " + "sent" + " " + sp_results[7] + " " + "received")

        if bool(re.search(r"qq", sp_results[2])):
            pass
        else:
            found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[4] + " " + "sent" + " " + sp_results[7] + " " + "received")
        


    #Removes Duplicates with set
    hosts = set(found)

    #print results
    for eachHost in hosts:

        print(eachHost)

def proxy_opened(filename, service, term):

    #Call syslogCheck file
    is_found = syslogCheck._syslog(filename, service, term)

    #found list
    found = []
    
    #Loops results
    for eachFound in is_found:
        #Split Results
        sp_results = eachFound.split(" ")

        #Append the split values to found
        if bool(re.search(r"qq", sp_results[2])):
            pass
        else:
            found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[3] + " " + sp_results[4]+ " " + sp_results[5] + " " + sp_results[6])

    #Removes Duplicates with set
    #hosts = set(found)

    #print results
    for eachHost in found:

        print(eachHost)