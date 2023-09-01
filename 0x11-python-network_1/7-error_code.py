#!/usr/bin/python3

"""Python script that takes in a URL,
sends a request to the URL and displays the body of the response."""

import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.text is not None and req.status_code == 200:
        print('{}'.format(req.text))
    else:
        code = req.status_code
        if code >= 400:
            print('Error code: {}'.format(code))
