# -*- coding: utf-8 -*-
import os
import json

#PATH
path = os.getcwd()
syscache = (path+'/cache')
solr = (path+'/core/poc/solr')

os.system("cp %s/standard %s/final_execute"%(solr,solr))

target = open(syscache + '/url.log','r')
target = target.read()
print("[+] Target:",target)

port = input("[+] Please input port:")
print("[+] Port:",port)



os.system("sed -i 's/<url>/%s/g' %s/final_execute"%(target,solr))
os.system("sed -i 's/<port>/%s/g' %s/final_execute"%(port,solr))



os.system("sh %s/final_execute"%(solr))
os.system("rm -rf %s/final_execute"%(solr))