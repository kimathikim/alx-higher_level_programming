#!/bin/bash
#  bash script that receives GET method with attributtes and displays body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
