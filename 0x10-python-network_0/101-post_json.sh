#!/bin/bash
#sends a JSON POST request to an URL and displays the body of the response
curl -sX POST -H "content-type:application/json" -d @"$2" "$1"
