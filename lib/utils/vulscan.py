# -*- coding: utf-8 -*-
import sys
import os

path = os.getcwd()
cache = (path+'/cache')

services = cache+'/services.log'

with open(services,'r') as foo:
	for line in foo.readlines():
    	if 'WebLogic' in line:
            print("[+] WebLogic service exists.")


