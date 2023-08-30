#!/bin/bash
# script to display the status code
curl -s -o "$temp_file" -w "%{http_code}" "$1"
