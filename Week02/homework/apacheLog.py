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
        if term == 'QQ':
            found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[4] + " " + "sent" + " " + sp_results[7] + " " + "received")
        if term == 'QQOpened':
            found.append(sp_results[0] + " " + sp_results[3] + " " + sp_results[4]+ " " + sp_results[5])

    #Removes Duplicates with set
    hosts = set(found)

    #print results
    for eachHost in hosts:

        print(eachHost)