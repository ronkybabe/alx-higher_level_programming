#!/bin/bash
# A script that takes in url,sends request to that url and display the size
curl -sI "$1" | awk ' /Content-Length/{print $2}'

