#!/bin/bash
# Write a Bash script that sends a request to a URL passed as an argument.
curl -s -w "%{response_code}" -o /dev/null "$1"
