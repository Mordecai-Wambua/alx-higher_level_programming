#!/bin/bash
#sends a DELETE request to an URL and displays the body of the response
curl -sLX DELETE "$1"
