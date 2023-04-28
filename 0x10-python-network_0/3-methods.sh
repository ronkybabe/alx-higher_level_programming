#!/bin/bash
# Write a Bash script that takes in a URL methods accepted by the server
curl -siLk -X OPTIONS "$1" | grep -oiE 'Allow: .+' | cut -d ' ' -f2-
