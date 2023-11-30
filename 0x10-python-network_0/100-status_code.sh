#!/bin/bash
# Send request and purse arguments.
curl -s "${1}" -o /dev/null -w "%{http_code}"
