import time
import requests
from bs4 import BeautifulSoup

import re

from models.Item import Item
from models.WikiHandler import WikiHandler

#def count_objects_without_any_dates(SNES_games: list):
#    for game in SNES_games:
#        if game.

SNES_games = []
counter = 0
start = time.time()

shared = WikiHandler()
urls = shared.urls

for url in urls:
    print(f'Processing {url}')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    

    #getting correct and full name
    #table_content = result[0].contents[0]    
    #single_item = Item(title = table_content.contents[0].get_text(), platform = "SNES")
    
    #single_item.prepare_dates(table_content.get_text())
    #single_item.show_item_details()
    

    for element in soup.find_all('a', href=True):
        item = element['href']
        if item[0:6]=='/wiki/': 
            #TODO: - bad naming convention, to be fixed
        #     #if not WikiHandler.keyword_not_forbidden(item):
            if not shared.keyword_not_forbidden(item):
        #         #SNES_games.append(item)
                #print(f'Processing {item}')
                gameURL = "https://en.wikipedia.org" + element['href']
                pageDetails = requests.get(gameURL)
                soup = BeautifulSoup(pageDetails.content, 'html.parser')
                result = soup.find_all(class_='infobox ib-video-game hproduct')
                if result:
                    table_content = result[0].contents[0]    
                    single_item = Item(title = table_content.contents[0].get_text(), platform = "SNES")
                    single_item.prepare_dates(table_content.get_text())
                    single_item.show_item_details()
                    SNES_games.append(single_item)
                    
                    if single_item.release_JP=="" and single_item.release_NA=="" and single_item.release_JP=="":
                        counter += 1
                    
                    print(gameURL)
                    print('\n')
                
        #         #getting title
        #         if result:
        #             print("not empty")


print(f'Edited {len(SNES_games)} games for {round(time.time()-start,1)} seconds')

print("Calculating objects")

print("Count of games without any date")
print(counter)
