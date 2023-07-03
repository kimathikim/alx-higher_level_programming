#!/bin/bash
#  bash script that receives GET method with attributtes and displays
#  body
#
url="$1"
curl -sH "X-School-User-Id: 98" "$url"
