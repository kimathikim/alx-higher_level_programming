#!/usr/bin/python3

"""script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter"""

import requests
from sys import argv

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        letter = argv[1]
        req = requests.post(url, data={'q': letter})
        if req.status_code == 200:
            try:
                res = req.json()
                if res:
                    print("[{}] {}".format(res["id"], res["name"]))
                else:
                    print("No result")
            except ValueError:
                print("Not a valid JSON")
    else:
        print("No result")
