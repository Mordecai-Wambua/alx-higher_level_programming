#!/usr/bin/python3
"""Takes in my github credentials and displays my id."""


import requests
import sys


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    credentials = (sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=credentials)
    print(r.json().get('id'))
