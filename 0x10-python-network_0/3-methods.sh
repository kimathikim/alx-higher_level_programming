#!/bin/bash
# displat all the methods available
curl -sI "$1" | awk '/Allow/' | cut -d " " -f2-
