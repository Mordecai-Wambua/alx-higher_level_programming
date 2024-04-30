#!/bin/bash
#sends a request to a URL and displays only the status code of the response.
curl -sIX GET "$1" | grep -i '^HTTP/1.1' | awk '{print $2}' 
