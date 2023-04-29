#!/usr/bin/python3
'''
Write a Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable.
'''
from urllib import request
from sys import argv


if __name__ == '__main__':
    if len(argv) > 1:
        with request.urlopen(argv[1]) as res:
            print(res.headers['X-Request-id'])
