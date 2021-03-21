# -*- coding: utf-8 -*-
import os
import json

#PATH
path = os.getcwd()
syscache = (path+'/cache')
jboss = (path+'/core/poc/jboss')

os.system("cp %s/standard %s/final_execute"%(jboss,jboss))

target = open(syscache + '/url.log','r')
target = target.read()
print("[+] Target:",target)

port = input("[+] Please input port:")
print("[+] Port:",port)



os.system("sed -i 's/<url>/%s/g' %s/final_execute"%(target,jboss))
os.system("sed -i 's/<port>/%s/g' %s/final_execute"%(port,jboss))



os.system("sh %s/final_execute"%(jboss))
os.system("rm -rf %s/final_execute"%(jboss))
