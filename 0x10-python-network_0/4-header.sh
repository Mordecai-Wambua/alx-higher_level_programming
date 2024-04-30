#!/bin/bash
#sends a GET request to an URL and displays the body of the response
curl -sLX GET -H "X-School-User-Id: 98" "$1"
