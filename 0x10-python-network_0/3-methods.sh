#!/bin/bash

# Extract the URL from the command line argument
url="$1"

# Display all HTTP methods the server of the given URL will accept
curl -sI "$url" | awk '/Allow/ {print $2}'