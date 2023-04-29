#!/usr/bin/python3
'''
Write a Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter.
'''
from urllib import request
from urllib import parse
from sys import argv


if __name__ == '__main__':
    if len(argv) > 2:
        data = parse.urlencode({'email': argv[2]})
        data = data.encode('ascii')
        req = urllib.request.Request(argv[1], data)
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
