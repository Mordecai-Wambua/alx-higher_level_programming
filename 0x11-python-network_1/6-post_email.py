#!/usr/bin/python3
"""Takes in a URL and email, sends a POST request and displays response."""


import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.post(url, data={'email': sys.argv[2]})
    print(r.text)
