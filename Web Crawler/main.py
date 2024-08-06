import requests
from bs4 import BeautifulSoup
import threading

target_url = "https://yaziturabarcade.com/"
foundLinks = set()
lock = threading.Lock()

def make_request(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers,timeout=5)

        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.RequestException as e:
        print(f"Error making request to {url}: {e}")
        return None

def crawl(url):
    soup = make_request(url)
    if not soup:
        return
    for link in soup.find_all('a'):
        found_link = link.get('href')
        if found_link:
            if "#" in found_link:
                found_link = found_link.split("#")[0]
            if target_url in found_link:
                with lock:
                    if found_link not in foundLinks:
                        foundLinks.add(found_link)
                        print(found_link)
                        threading.Thread(target=crawl, args=(found_link,)).start()

crawl(target_url)
