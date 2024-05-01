#!/usr/bin/python3
"""
Send a POST request to the passed URL with the email as a parameter.

Usage: ./2-post_email.py <url> <email>
"""


import sys
import urllib.request
import urllib.parse


url = sys.argv[1]
par = {'email': sys.argv[2]}
data = urllib.parse.urlencode(par)
data = data.encode('ascii')

req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read().decode('utf-8')
    print(the_page)
