#!/bin/bash
# A script that takes in url,sends request to that url and display the size
curl -sI "$1" | grep -iE 'Content-Length: [0-9]+' | cut -d '' -f2

