#!/usr/bin/python3
"""Takes in a URL, sends a request and displays response."""


import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    code = r.status_code
    if (code >= 400):
        print('Error code:', code)
    else:
        print(r.text)
