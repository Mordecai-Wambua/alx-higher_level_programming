#!/bin/bash
#makes a request to a server causing it to respond with the message You got me!
curl -sL  -X PUT  -H 'Origin: School' localhost:5000/catch_me_3
