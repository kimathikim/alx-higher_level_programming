#!/usr/bin/python3

"""script that fetches https://alx-intranet.hbtn.io/status
using requests module"""

import requests

if __name__ == "__main__":
    with requests.get('https://alx-intranet.hbtn.io/status') as response:
        req = response.text
        print("Body response:")
        print("\t- type: {}".format(type(req)))
        print("\t- content: {}".format(req))
