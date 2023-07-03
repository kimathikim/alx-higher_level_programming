#!/bin/bash
#  bash script that receives GET method with attributtes and displays
#  body
#
url="$1"
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$url"
