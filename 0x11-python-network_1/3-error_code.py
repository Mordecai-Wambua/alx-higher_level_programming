#!/usr/bin/python3
"""Takes in a  URL, sends a request and displays response body."""


from urllib.request import Request, urlopen
from sys import argv
from  urllib.error import HTTPError

if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    try:
        response = urlopen(req)
    except HTTPError as e:
        print('Error code: ',e.code)
    else:
        html = response.read().decode('utf-8')
        print(html)
