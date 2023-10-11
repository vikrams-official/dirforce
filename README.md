# Directory Enumeration Tool

## Introduction

This Python script is a directory enumeration tool that helps you discover hidden directories and files on a target web application by testing a list of common directory and file names. It sends HTTP requests to the target URL and checks the HTTP status code and the page's title to determine if the directory or file exists.

## Features

- Enumerates directories and files on a target URL.
- Checks the HTTP status code and page title to identify existing directories/files.

## Requirements

- Python 3.x
- Libraries: `urllib3`, `requests`, `colorama`, `BeautifulSoup`

## Usage

1. Clone the repository:
git clone https://github.com/vikrams-official/dirforce.git
   
Install the required libraries:
-pip install urllib3 requests colorama beautifulsoup4

Run the script:
python dirforce.py

Example:
python dirforce.py
Enter target URL: https://example.com

##Note
-Use appropriate protocol before domain name like http:// or https://

Status Code | Request URL | Response
--- | --- | ---
[+] | [https://example.com/](https://example.com/) | Example Homepage
[!] 404 | [https://example.com/nonexistent](https://example.com/nonexistent) | Not Found
[+] | [https://example.com/about](https://example.com/about) | About Us

...

Author
Vikram S
License
This project is licensed under the MIT License - see the LICENSE file for details.

https://github.com/vikrams-official/dirforce.git 
