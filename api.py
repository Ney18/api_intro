#!/usr/local/bin/python3
from pprint import pprint
import requests
import json 
r = requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas', auth=('a930ee62-5850-42a7-9889-1a9851c1737d', ''))


pprint(r.json()) 

