#coding:utf-8

import optparse
import dns.resolver
import console
import urllib3
from socket import *
from multiprocessing import Pool
import re
import time


def portsscan(host,port):
    
    try:
        connect = socket(AF_INET,SOCK_STREAM)
        connect.settimeout(0.3)
        connect.connect((host,port))
        banner = getbanner(host,port)
        print("[+] "+str(port)+" /tcp open "+banner)
    except:
        pass
def portscan(host,port):
    #单端口扫描
    port = int(port)
    try:
        connect = socket(AF_INET, SOCK_STREAM)
        connect.settimeout(0.2)
        connect.connect((host, port))
        banner = getbanner(host,port)
        print("[+] " + str(port) + " /tcp open "+banner)
    except:
        print("[-] %s /tcp close" % port)

def getbanner(host,port):
    
    connect = socket(AF_INET, SOCK_STREAM)
    connect.settimeout(0.1)
    connect.connect((host, port))
    
def getbanner(host,port):
    
    connect = socket(AF_INET, SOCK_STREAM)
    connect.settimeout(0.1)
    connect.connect((host, port))
    try:
        banner = str(connect.recv(100))[2:-5]
    except:
        if port == 80:
            banner = "http"
        elif port == 135:
            banner = "Microsoft Windows RPC"
        elif port == 443:
            banner = "https"
        elif port == 445:
            banner = "microsoft-ds"
        else:
            banner = "unknown"
    return banner
    
def domaintoip(domain):
    
    try:
        ip = getaddrinfo(domain,None)[0][4][0]
    except:
        return domain
    return ip
def getServer(url):
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    try:
        web = http.request("GET",url)
        if web.status == 200:
            Server = web.headers["Server"]
            return Server
    except:
        return "known server"
def ipordomain(host):
    
    if re.match(r"[a-z]+.\w+.[a-z]+", host):
        return "domain"
    elif re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",host):
        return "ip"
    else:
        print("Please enter the correct address")
        exit(4)
def check_argv(host,port):
    
    if host == None or port == None:
        print(parser.usage)
        exit(0)
    if re.match('^http',host):
        print("example:www.google.com")
        exit(1)
    if ipordomain(host) == "domain":
        cdn_result = query_cname(host)
        if (cdn_result==False):
            pass
        else:
            if(check_cdn(cdn_result)):
                pass
        host = domaintoip(host)
    if ipordomain(host) == "ip":
        host = host
    server = getServer(host)
    print("[+] scanning for " + host + "......")
    print("[+] Server: " + str(server))
def check_port_or_ports(port,thread,start_time):
    
    if thread == None:
        thread = 20
    if re.findall('-',port):
        pool = Pool(thread)
        port1 = port.split('-')
        for port in range(int(port1[0]), int(port1[1])+1):
            pool.apply_async(portsscan,(host,port))
        pool.close()
        pool.join()
        end_time = float(time.time())
        print("[+] This scan took "+str(round((end_time-start_time),3))+" s")
    else:
        portscan(host,port)
        end_time = float(time.time())
        print("[+] This scan took " +str(round((end_time-start_time),3))+ "s")

def query_cname(domain):
    
    try:
        cname_query = dns.resolver.query(domain, 'CNAME')
    except:
        return False
    for i in cname_query.response.answer:
        for j in i.items:
            cname = str(j)[:-1]
            return cname


if __name__ == '__main__':

    
    parser = optparse.OptionParser("-H <target host> -p <target port>")
    parser.add_option('-H', dest='host', type='string')
    parser.add_option('-p', dest='port', type='string')
    parser.add_option('-t', dest='thread', type='int')
    (options, args) = parser.parse_args()
    host = options.host
    port = options.port
    thread = options.thread
    start_time = float(time.time())
    check_argv(host,port)
    check_port_or_ports(port, thread, start_time)