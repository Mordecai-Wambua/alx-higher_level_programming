#!/usr/bin/python3
"""Takes in a URL, sends a request and displays variable value."""


import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    try:
        print(r.headers['X-Request-Id'])
    except KeyError as e:
        pass
