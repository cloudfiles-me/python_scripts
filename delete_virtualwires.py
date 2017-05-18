#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth
for x in range (3,10):
  url = "https://192.168.1.220/api/2.0/vdn/virtualwires/virtualwire-%d" %(x)
  #print url
  r = requests.delete(url, verify=False, auth=HTTPBasicAuth('admin', 'VMware1!VMware1!'))
  print r.status_code
