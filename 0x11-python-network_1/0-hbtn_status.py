#!/usr/bin/python3
'''
Write a Python script that fetches https://alx-intranet.hbtn.io/status and must use the package urllib
'''
import urllib.request


if __name__ == "__main__":
    with reqobj.urlopen('https://alx-intranet.hbtn.io/status/') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
