import urllib3
import requests
import os
import subprocess
import colorama
from bs4 import BeautifulSoup
import argparse
import sys

#!/usr/bin/python

def banner():
    print(colorama.Style.BRIGHT, colorama.Fore.CYAN,"""     
         ____ ___ ____  _____ ___  ____   ____ _____ 
        |  _ \_ _|  _ \|  ___/ _ \|  _ \ / ___| ____|
        | | | | || |_) | |_ | | | | |_) | |   |  _|  
        | |_| | ||  _ <|  _|| |_| |  _ <| |___| |___ 
        |____/___|_| \_\_|   \___/|_| \_\\____|_____|
    
                Written By @vikram
    Try to add protocol before the target domain
    Example: https://targetdoamin.com
             http://targetdoamin.com\n""")
banner()

target_url = str(input("Enter target URL: "))

path = r"filenames.txt"
#print(os.path.isfile(path))

try:
    with open(path, "r") as f:
        read_result = f.readlines()

        cmd = "python3 dirforce.py >> diresearch.txt"
        print("Status Code\t\t\t\t\t", "Request URL\t\t\t\t\t\t", "Response", colorama.Style.BRIGHT)
        for dirs in read_result:
            dir_names = dirs.strip()
            http = urllib3.PoolManager()
            url = http.request('GET', target_url + dir_names)
            soup = BeautifulSoup(url.data, 'html.parser')
            contents = soup.find('title')
            list = []
            list.append(url.status)

            if 404 in list:
                print(colorama.Fore.RED, '[!]', url.status, '\t\t\t', target_url + dir_names, '\t\t\t\t', colorama.Style.BRIGHT, contents.string)
            else:
                print(colorama.Fore.GREEN, '[+]', contents.find('body'), '\t\t\t', target_url + dir_names, '\t\t\t\t', colorama.Style.BRIGHT, contents.string)

        subprocess.Popen(cmd, shell=True)

except urllib3.exceptions.RequestError as reqerr:
    raise SystemExit(reqerr)

except urllib3.exceptions.HTTPError as httperr:
    raise SystemExit(httperr)


