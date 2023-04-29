#!/usr/bin/python3
'''
Script that fetches https://alx-intranet.hbtn.io/status
'''
import requests


if __name__ == "__main__":
    """ fetches http://0.0.0.0:5050/status"""
    res = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(res.text)))
    print('\t- content: {}'.format(res.text))
