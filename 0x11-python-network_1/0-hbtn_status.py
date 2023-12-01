#!/bin/python3
""""code to fetch a url and print the response"""
from urllib import request

with request.urlopen("https://intranet.hbtn.io/status") as response:
    response = response.read()
    print("\t- utf8 content: {}".format(response.decode("utf-8")))
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    print("\t- utf8 content: {}".format(response.decode("utf-8")))
