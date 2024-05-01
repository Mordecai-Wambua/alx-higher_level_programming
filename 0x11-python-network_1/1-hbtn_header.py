#!/usr/bin/python3
"""Takes in a URL, sends a request and displays the value of X-Request-ID."""


from urllib.request import Request, urlopen
import sys


url = sys.argv[1]
req = Request(url)
with urlopen(req) as response:
    html = response.info()
    print(html['X-Request-Id'])
