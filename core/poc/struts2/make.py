# -*- coding: utf-8 -*-
import os
import json

#PATH
path = os.getcwd()
syscache = (path+'/cache')
struts2 = (path+'/core/poc/struts2')

os.system("cp %s/standard %s/final_execute"%(struts2,struts2))

target = open(syscache + '/url.log','r')
target = target.read()
print("[+] Target:",target)

port = input("[+] Please input port:")
print("[+] Port:",port)



os.system("sed -i 's/<url>/%s/g' %s/final_execute"%(target,struts2))
os.system("sed -i 's/<port>/%s/g' %s/final_execute"%(port,struts2))



os.system("sh %s/final_execute"%(struts2))
os.system("rm -rf %s/final_execute"%(struts2))
