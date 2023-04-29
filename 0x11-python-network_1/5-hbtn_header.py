#!/usr/bin/python3
'''
Script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the header.
'''
import requests as req
from sys import argv


if __name__ == '__main__':
    if len(argv) > 1:
        res = requests.get(argv[1])
        if 'X-Request-Id' in res.headers:
            print(res.headers['X-Request-Id'])
