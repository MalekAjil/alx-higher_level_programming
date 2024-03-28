#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print(f'Body response:\n\t- type:', type(html))
    print(f'\t- content:', html)
    print(f'\t- utf8 content:', html.decode('utf-8'))
