# -*- coding: utf-8 -*-
import os
import json

#PATH
path = os.getcwd()
syscache = (path+'/cache')
drupal = (path+'/core/poc/drupal')

os.system("cp %s/standard %s/final_execute"%(drupal,drupal))

target = open(syscache + '/url.log','r')
target = target.read()
print("[+] Target:",target)

port = input("[+] Please input port:")
print("[+] Port:",port)



os.system("sed -i 's/<url>/%s/g' %s/final_execute"%(target,drupal))
os.system("sed -i 's/<port>/%s/g' %s/final_execute"%(port,drupal))



os.system("sh %s/final_execute"%(drupal))
os.system("rm -rf %s/final_execute"%(drupal))