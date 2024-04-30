#!/bin/bash
#sends a request to an URL and displays the body size of the response
curl -s "$1" | wc -c
