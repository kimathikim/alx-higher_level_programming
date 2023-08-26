#!/bin/bash
#  bash script that prints out the methods that are Allowed
curl -siX OPTIONS "$1" | grep Allow | awk -F ': ' '{print $2}'
