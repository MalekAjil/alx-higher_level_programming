#!/usr/bin/python3
import sys
import urllib.request
with urllib.request.urlopen($0) as response:
    html = response.read()
    print(f'Body response:\n\t- type:', type(html))
