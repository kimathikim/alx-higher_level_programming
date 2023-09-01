#!/usr/bin/python3

"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: ./10-my_github.py <username> <access token/password")
    url = 'https://api.github.com/users/{}'.format(argv[1])
    auth = {'Authorization': 'token {}'.format(argv[2]),
            'Accept': 'application/vnd.github.v3+json'}
    req = requests.get(url, headers=auth)
    if req.status_code == 200:
        print(req.json().get('id'))
    else:
        print('None')
