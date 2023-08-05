#! /usr/bin/env python

import requests
import sys
import json
#import click
import os
#import tabulate
import logging
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

os.system('cls')
logger = logging.getLogger(__name__)
SDWAN_IP = os.environ.get("SDWAN_IP")
SDWAN_USERNAME = os.environ.get("SDWAN_USERNAME")
SDWAN_PASSWORD = os.environ.get("SDWAN_PASSWORD")

if SDWAN_IP is None or SDWAN_USERNAME is None or SDWAN_PASSWORD is None:
    print("CISCO SDWAN details must be set via environment variables before running.")
    print("   export SDWAN_IP=10.10.20.90")
    print("   export SDWAN_USERNAME=admin")
    print("   export SDWAN_PASSWORD=C1sco12345")
    print("")
    exit("1")

