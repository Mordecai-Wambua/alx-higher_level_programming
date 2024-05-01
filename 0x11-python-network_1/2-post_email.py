#!/usr/bin/python3
"""send an email to the input  url and print the response"""


import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    par = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(par)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
