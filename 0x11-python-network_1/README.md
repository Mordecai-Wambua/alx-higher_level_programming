0x11. Python - Network #1
Python Scripting Back-end API

Task 00:(0-hbtn_status.py)
a Python script that fetches https://alx-intranet.hbtn.io/status

Task 01:(1-hbtn_header.py)
a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

Task 02:(2-post_email.py)
a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

Task 03:(3-error_code.py)
a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

Task 04:(4-hbtn_status.py)
a Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package requests

Task 05:(5-hbtn_header.py)
a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
You must use the packages requests and sys

Task 06:(6-post_email.py)
a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
The email must be sent in the variable email
You must use the packages requests and sys

task 07:(7-error_code.py)
a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
You must use the packages requests and sys

Task 08:(8-json_api.py)
a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys

Task 09:(10-my_github.py)
a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a personal access token as password)
You must use the package requests and sys
