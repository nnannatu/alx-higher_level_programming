#!/bin/bash

# Check if URL is provided as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send GET request to the URL and capture the response body
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Check if the request was successful (status code 200)
if [ "$response" -eq 200 ]; then
    # Display the body of the response
    curl -s "$1"
else
    echo "Request failed with status code: $response"
fi
