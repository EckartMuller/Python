from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://news.ycombinator.com/"

#request
httpRequest = requests.get(URL)
html = httpRequest.text

parseHtml = BeautifulSoup(html, 'html.parser')
titles = parseHtml.find_all('span', {'class':'titleline'})

for title in titles:
    a_tag = title.find('a')
    if a_tag:
        print(a_tag.get_text(strip=True))