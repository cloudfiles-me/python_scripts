#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth
for x in (44,45):
  url = "https://192.168.1.220/api/4.0/edges/edge-%d" %(x)
  print url
  r = requests.delete(url, verify=False, auth=HTTPBasicAuth('admin', 'VMware1!VMware1!'))
  print r.status_code