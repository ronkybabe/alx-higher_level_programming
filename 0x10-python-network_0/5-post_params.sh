#!/bin/bash
# Write a Bash script that takes in a URL, sends a POST
curl -sL -X POST -d 'email=test@gmail.com&subject=I+will+always+be+here+for+PLD' "$1"
