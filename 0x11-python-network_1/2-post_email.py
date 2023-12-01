#!/usr/bin/python3
"""Using post request to post an email to the server"""
if __name__ == "__main__":
    import urllib.request as request
    import urllib.parse as parse
    from sys import argv as argv

    url = argv[1]
    data = {"email": argv[2]}
    data = parse.urlencode(data)
    data = data.encode("ascii")
    req = request.Request(url, data)
    with request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
