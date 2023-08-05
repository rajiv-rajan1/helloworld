from ncclient import manager 
from getpass import getpass 
from xml.dom.minidom import parseString
import os

os.system('cls')

# username = input("Username :")
# password = getpass("Password :")

device = {
    'host':'sandbox-iosxe-recomm-1.cisco.com',
    'port':'830',
    'username':'developer',
    'password':'lastorangerestoreball8876',
    'hostkey_verify':False
}

netconf = manager.connect(**device)
## This filters only the interface section###
int_filter ="""
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    </interfaces>
</filter>
"""

running_configs = netconf.get_config(filter = int_filter, source ="running")
pretty_running = parseString(running_configs.xml).toprettyxml()
print(pretty_running)
