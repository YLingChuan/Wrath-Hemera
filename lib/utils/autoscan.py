#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import socket
import re
import time
import os


#path
path = os.getcwd()
cache = (path+'/cache')
poc = (path+'/core/poc')
exp = (path+'/core/exp')
backdoor = (path+'/core/backdoor')
utils = (path+'/lib/utils')

#get ip address
'''
print("[+] Get IP address..")
url = open(cache + '/url.log','r')
url = url.read()
print ( "[+] IP address:" , socket.gethostbyname(url))
ip = socket.gethostbyname(url)
with open(cache + '/ip.log', 'w') as f:
    f.write(ip)
'''

web = input("[*] Is the web page running on the target server? [Y/N]")
if web == "Y" and "y":
	from lib.utils import cms
else:
	print("[+] Ignore CMS scan.")



#port scan
ip = open(cache + '/ip.log','r')
ip = ip.read()
port_scan_thread = input("[*] Please enter the number of port scanning threads:")
print("[+] The port scan starts, please wait a moment.")
port_info = os.popen("python3 %s/portscan.py -H %s -t %s -p 1-65535"%(utils,ip,port_scan_thread)).read()
print(port_info)
with open(cache + '/port.log', 'w') as f:
    f.write(port_info)
os.system("awk '{print $2}' %s/port.log > %s/port_info.log "%(cache,cache))
os.popen("sed -i '/^[A-Z,a-z]/d' %s/port_info.log"%(cache)).read()
os.popen("bash %s/format_port.sh "%(cache)).read()

#path scan
if web == "Y" and "y":
	print("[+] Path scan:")
	#os.system("python3 %s/dirscan.py" %(utils))
else:
	print("[+] Ignore Path scan.")



#services scan
print("[+] Services scan:")
os.system("python3 %s/services.py" %(utils))


#vul scan
print("[+] Vulnerability Scan:")



