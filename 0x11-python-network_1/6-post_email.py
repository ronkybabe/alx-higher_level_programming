#!/usr/bin/python3
'''
Script that takes in a URL and an email address, sends a
POST request to the passed URL with the email as a parameter.
'''
import requests as req
from sys import argv


if __name__ == '__main__':
    if len(argv) > 2:
        r = req.post(argv[1], data={'email': argv[2]})
        print(r.text)
