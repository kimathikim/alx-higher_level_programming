#!/bin/bash
# sends a JSON POST request as the first argument.
curl -X POST "${1}" -H "Content-Type: application/json" -d @"${2}"
