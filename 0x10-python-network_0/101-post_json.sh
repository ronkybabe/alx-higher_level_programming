#!/bin/bash
# Write a Bash Script that sends a JSON POST request to a given URL passed as the first argument
curl -sL -X POST -H 'Content-Type: application/json' -d "$([ -f "$2" ] && cat "$2")" "$1"
