#!/usr/bin/python3

"""Script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request as req
if __name__ == "__main__":
    with req.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf8')))
