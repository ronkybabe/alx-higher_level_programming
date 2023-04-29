#!/usr/bin/python3
'''
Script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import requests as req
from sys import argv


if __name__ == '__main__':
    query = argv[1] if len(argv) > 1 else ""
    r = req.post('http://0.0.0.0:5000/search_user', data={'q': query})
    try:
        json_data = res.json()
        if json_data:
            print('[{}] {}'.format(json_data['id'], json_data['name']))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
