##First API over Python for NEtworking##

import requests
import json
import os 
import pandas as pd

requests.packages.urllib3.disable_warnings()
proxies = {
   'http': 'http://sub.proxy.att.com:8080',
   'https': 'http://sub.proxy.att.com:8080',
}

os.system("cls")

url_interface_status = "https://sandbox-iosxe-recomm-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces-state"
url = "https://sandbox-iosxe-recomm-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2"
url_config_interface = "https://sandbox-iosxe-recomm-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces"

payload_config_interface = json.dumps({
  "ietf-interfaces:interface": {
    "name": "Loopback104",
    "description": "Configured by RESTCONF",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "172.16.104.1",
          "netmask": "255.255.255.255"
        }
      ]
    }
  }
})
headers_config_interface = {
  'Authorization': 'Basic ZGV2ZWxvcGVyOmxhc3RvcmFuZ2VyZXN0b3JlYmFsbDg4NzY=',
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response_config_interface = requests.request("POST", url_config_interface, headers=headers_config_interface, data=payload_config_interface, verify=False, proxies=proxies)

print(response_config_interface.text)


#
payload_interface_status = {}
headers_interface_status = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOmxhc3RvcmFuZ2VyZXN0b3JlYmFsbDg4NzY='
}

response_interface_status = requests.request("GET", url_interface_status, headers=headers_interface_status, data=payload_interface_status, verify=False, proxies=proxies)
data_interface_status = response_interface_status.json()
#
for i in data_interface_status:
    #if "172.16.10" in data_interface_status[i]['interface'][3]['name']:
  print(data_interface_status)#['name'])
    #print(j)
    #j=j+1
