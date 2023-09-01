#!/usr/bin/python3

""" script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

from sys import argv
from urllib import request as r
from urllib import parse

if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: ././2-post_email.py <URL> <email>")
    else:
        # encoding email
        e_data = parse.urlencode({'email': argv[2]})
        e_data = e_data.encode('utf-8')

        req = r.Request(argv[1], data=e_data)
        with r.urlopen(req) as response:
            html = response.read().decode('utf-8')
            print(html)
