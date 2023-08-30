#!/bin/bash
temp_file="$(mktemp)"
curl -s -o "$temp_file" -w "%{http_code}" "$1"
rm "$temp_file"
