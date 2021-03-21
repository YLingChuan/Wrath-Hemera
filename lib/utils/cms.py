# -*- coding: utf-8 -*-
import os
import sys
import json

path = os.getcwd()
cache = (path+'/cache')

url = open(cache + '/url.log','r')
url = url.read()



try:
    cms_tmp = os.popen('curl -s -G https://whatcms.org/API/CMS \
    --data-urlencode key="5926b162fde6d3da25520ef5dc0512f8556e637009b72aed3b7576c527766c487a3510" \
    --data-urlencode url="%s"'%(url)).read()
    cms = json.loads(cms_tmp)
    cmslog = cms['result']['name']

    print("[+] CMS:",cms['result']['name'])
except:
    print("[+] Error,Ignore CMS Scan.")

# save cms log
try:
	with open(cache+'/cms.log','w') as f:
  		f.write(cmslog)
except:
	print("[!] CMS cache save failed.")
