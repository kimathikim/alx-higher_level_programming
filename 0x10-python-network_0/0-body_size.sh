#!/bin/bash
#  Bash script that takes in a URL send a request and display the size of the response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
