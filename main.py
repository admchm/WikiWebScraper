from bs4 import BeautifulSoup
import requests

page_url = 'https://en.wikipedia.org/wiki/Super_Mario_World'
page = requests.get(page_url)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

# 1. Count all of the tags from the webpage
links_count = soup.find_all('a')
print(f'found {len(links_count)} links')

print(links_count[5].get_text())

# 2. Searching tags by classes or IDs
#game_title = soup.find_all(class_='infobox-above fn') #[0].get_text() - could use it on a nested element that has children
#print(game_title)

game_title = soup.find_all(id='firstHeading')
print(game_title[0].get_text())

#release_date = soup.find_all(class_='infobox_data')
#print(release_date)