#!/bin/bash
#takes in an URL and displays all HTTP methods the server accepts
curl -sIX OPTIONS "$1" | grep -i '^Allow:' | cut -d " " -f2-
