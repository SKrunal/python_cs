import nmap
import sys
import time
nm_scan = nmap.PortScanner()

print("\nRunning...\n")
nm_scanner = nm_scan.scan(sys.argv[1],'80',arguments = '-O')

host_is_up = "The host is " + nm_scanner['scan'][sys.argv[1]]['status']['state']+"\n"
port_open = "the port 80 is : "+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state']+"\n"
method_scan = "The method of sccaning is "+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason']+"\n"
guessd_os = "there is a %s percent chance is host is running %s" %(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'],nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name'])+"\n"

with open("%s.txt"%sys.argv[1],'w') as f:
    f.write(host_is_up+port_open+method_scan+guessd_os)
    f.write("\nReport generated "+time.strftime("%Y-%m-%d_%H:%M%S GMT",time.gmtime()))


print("\nFinished....")