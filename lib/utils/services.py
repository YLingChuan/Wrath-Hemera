# -*- coding: utf-8 -*-
import os
import nmap

path = os.getcwd()
cache = (path+'/cache')

f = open(cache+'/ip.log')
ip = f.read()

f = open(cache+'/port.log')
port = f.read()


#print(port)


nm = nmap.PortScanner()
nm.scan(ip, port, '-sV')

print(nm.csv())

with open(cache + '/servers_tmp.log', 'w') as f:
    f.write(nm.csv())

os.popen("ggrep -Po '(?<=;)O.*?(?=;)' %s/servers_tmp.log > %s/servers.log" %(cache,cache)).read()

