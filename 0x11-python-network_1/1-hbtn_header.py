#!/usr/bin/python3
"""Display the value of X-Request-Id from url request"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv as argv

    url = "https://alx-intranet.hbtn.io"
    with request.urlopen(url) as res:
        print(res.read())
