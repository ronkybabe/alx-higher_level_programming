#!/usr/bin/python3
'''
Write a Python script that fetches https://alx-intranet.hbtn.io/status and must use the package urllib
'''
import urllib.request as reqobj


if __name__ == "__main__":
    with reqobj.urlopen('https://alx-intranet.hbtn.io/status/') as response:
        the_page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page))
        print("\t- utf8 content: {}".format(the_page.decode("utf-8")))
