# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 08:41:45 2019

@author: srishti
"""

import requests
import json
url = "https://api.meaningcloud.com/summarization-1.0"

payload = "key=56dee7c0872448b1b09b2f4d8d339d66&txt=Hi! My name is Srishti. Life is cool.& sentences=1"
headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)
summary=json.loads(response.text)["summary"]
print(summary)