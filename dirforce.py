import requests
import os
import colorama
from bs4 import BeautifulSoup

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

path = os.path.abspath("filenames.txt")

try:
    with open(path, "r") as f:
        read_result = f.readlines()

        print("Status Code\t\t\t\t\t", "Request URL\t\t\t\t\t\t", "Response", colorama.Style.BRIGHT)
        for dirs in read_result:
            dir_names = dirs.strip()
            url = requests.get(target_url + dir_names)
            soup = BeautifulSoup(url.content, 'html.parser')
            contents = soup.find('title')
            status_code = url.status_code

            if status_code == 404:
                print(colorama.Fore.RED, '[!]', status_code, '\t\t\t', target_url + dir_names, '\t\t\t\t', colorama.Style.BRIGHT, contents.string)
            else:
                print(colorama.Fore.GREEN, '[+]', contents.find('body'), '\t\t\t', target_url + dir_names, '\t\t\t\t', colorama.Style.BRIGHT, contents.string)

except requests.exceptions.RequestException as reqerr:
    raise SystemExit(reqerr)
