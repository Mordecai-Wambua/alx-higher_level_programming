#!/usr/bin/python3
"""Takes in a URL, sends a request and displays the value of X-Request-ID."""
import urllib.request
import sys


url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    html = response.info()
    print(html['X-Request-Id'])
