import time
import requests
from bs4 import BeautifulSoup

from models.Item import Item
from models.WikiHandler import WikiHandler

shared = WikiHandler()
start = time.time()

for url in shared.urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for element in soup.find_all('a', href=True):
        item = element['href']
        if item[0:6]=='/wiki/': 
            #TODO: - bad naming convention, to be fixed
            if not shared.keyword_not_forbidden(item):
                url = "https://en.wikipedia.org" + element['href']
                pageDetails = requests.get(url)
                soup = BeautifulSoup(pageDetails.content, 'html.parser')
                result = soup.find_all(class_='infobox ib-video-game hproduct')
                if result:
                    table_content = result[0].contents[0]    
                    single_item = Item(title = table_content.contents[0].get_text(), game_url= url)
                    single_item.prepare_dates(table_content.get_text())
                    single_item.show_item_details()
                    
                    shared.SNES_games_list.append(single_item)
                    
                    if single_item.release_JP=="———" and single_item.release_NA=="———" and single_item.release_JP=="———":
                        shared.counter += 1
                    
print(f'Edited {len(shared.SNES_games_list)} games for {round(time.time()-start,1)} seconds')

shared.calculate_objects_count
