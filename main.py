from bs4 import BeautifulSoup
import requests

page_url = 'https://en.wikipedia.org/wiki/Main_Page'
page = requests.get(page_url)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

# 1. Counting all of the tags from the webpage
links_count = soup.find_all('a')
print(f'found {len(links_count)} links')