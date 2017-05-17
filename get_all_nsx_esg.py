#!/usr/bin/env python

import requests
import xml.dom.minidom
from requests.auth import HTTPBasicAuth
r = requests.get('https://192.168.1.220/api/4.0/edges/',verify=False, auth=HTTPBasicAuth('admin', 'VMware1!VMware1!'))
# Print request output unformatted
#print r.text
# Pretty print xml output 
# We can use this: xml.dom.minidom.parse(xml_fname) to pass an xml file to the function
xml = xml.dom.minidom.parseString(r.text)
pretty_xml_as_string = xml.toprettyxml()
print pretty_xml_as_string