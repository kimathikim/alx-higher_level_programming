#!/usr/bin/python3

"""Script that fetch url,
send request and displays the value of X-Request-Id variable"""

import sys
import urllib.request as r

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
    else:
        req = r.Request(sys.argv[1])
        with r.urlopen(req) as response:
            print(response.headers.get('X-Request-Id'))
