#!//usr/bin/python3
"""Getting a specific header and displaying its value"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    with requests.get(url) as res:
        print(res.headers["X-Request-Id"])
