#!/bin/bash
#  bash script that prints out the methods that are Allowed
url="$1"
curl -sI "$url" | awk '/Allow:/ {print $2}'
