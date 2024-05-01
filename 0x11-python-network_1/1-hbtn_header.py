#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""

from urllib.request import Request, urlopen
import sys


url = sys.argv[1]
req = Request(url)
with urlopen(req) as response:
    html = response.info()
    print(html['X-Request-Id'])
