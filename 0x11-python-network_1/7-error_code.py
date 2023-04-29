#!/usr/bin/python3
'''
Script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)
'''
import requests as req
from sys import argv


if __name__ == '__main__':
    if len(argv) > 1:
        response = req.get(argv[1])
        if response.status_code >= 400:
            print('Error code: {}'.format(response.status_code))
        else:
            print(response.text)
