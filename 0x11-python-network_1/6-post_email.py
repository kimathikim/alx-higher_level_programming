#!/usr/bin/python3
"""Using requests to make post requests for an  email address"""
if __name__ == "__main__":
    import requests
    from sys import argv

    email = {"email": argv[2]}
    url = argv[1]
    with requests.post(url, data=email) as res:
        print(res.text)
