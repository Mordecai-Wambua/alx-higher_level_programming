#!/usr/bin/python3
"""Interview challenge to find commits of a specific user."""


import requests
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            sys.argv[2], sys.argv[1])
    r = requests.get(url)
    output = r.json()
    for i in output[:10]:
        print('{}: {}'.format(
            i.get('sha'),
            i.get('commit').get('author').get('name')))
