# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 21:05:28 2019

@author: srishti
"""

# Ensure your pyOpenSSL pip package is up to date
# Example posting a text URL:

import requests
r = requests.post(
    "https://api.deepai.org/api/summarization",
    data={
        'text': 'YOUR_TEXT_URL',
    },
    headers={'api-key': '54e3a0c8-6bff-4dc3-a3ab-bf5f6842a0a6'}
)
print(r.json())


# Example posting a local text file:

import requests
r = requests.post(
    "https://api.deepai.org/api/summarization",
    files={
        'text': open('summary.txt'),
    },
    headers={'api-key': '54e3a0c8-6bff-4dc3-a3ab-bf5f6842a0a6'}
)
print(r.json())


# Example directly sending a text string:

import requests
r = requests.post(
    "https://api.deepai.org/api/summarization",
    data={
        'text': 'Hello. My name is Srishti. Life is cool',
    },
    headers={'api-key': '54e3a0c8-6bff-4dc3-a3ab-bf5f6842a0a6'}
)
print(r.json())