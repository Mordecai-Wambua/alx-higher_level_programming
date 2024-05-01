#!/usr/bin/python3
""" Takes in a URL, sends a request and displays
the value of the X-Request-Id variable.
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
