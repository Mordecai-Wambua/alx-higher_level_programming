#!/usr/bin/python3
"""Takes in a letter, sends a POST request and displays response."""


import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if (len(sys.argv) < 2):
        letter = ''
    else:
        letter = sys.argv[1]

    r = requests.post(url, data={'q': letter})
    try:
        output = r.json()
        if output == {}:
            print('No result')
        else:
            print('[{}] {}'.format(output.get('id'), output.get('name')))
    except ValueError:
        print('Not a valid JSON')
