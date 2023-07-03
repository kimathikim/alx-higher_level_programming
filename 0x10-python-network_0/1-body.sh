#!/bin/bash
#  Bash script that displays the body of the response
url="$1"
curl -sI "$url"
