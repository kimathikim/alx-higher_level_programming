#!/usr/bin/python3

""" script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""

from urllib import request, error
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./3-error_code.py <URL>.")
    else:
        try:
            url = request.Request(argv[1])
            with request.urlopen(url) as response:
                print(response.read().decode('utf-8'))
        except error.HTTPError as e:
            print('Error code: {}'.format(e.code))
