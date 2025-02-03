import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Back, Style, init
init(autoreset=True)

def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        return None

def check_subdomain(word, target_input, protocol):
    word = word.strip()
    url = f"{protocol}://{word}.{target_input}"
    response = make_request(url)
    if response:
        print(Fore.GREEN + "Found subdomain:", url)

choose = input(Fore.GREEN + "https(1) or http(2): ")
if choose == "1":
    protocol = "https"
elif choose == "2":
    protocol = "http"
else:
    print(Fore.RED+"Invalid choice.")
    exit()

target_input = input(Fore.GREEN + "Target website: ")

with open("subdomainlist.txt", "r") as subdomainlist:
    words = subdomainlist.readlines()

with ThreadPoolExecutor(max_workers=10) as executor:
    for word in words:
        executor.submit(check_subdomain, word, target_input, protocol)
