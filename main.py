import time
import requests
from bs4 import BeautifulSoup

import re

from models.Item import Item
from models.WikiHandler import WikiHandler


SNES_games = []
start = time.time()

urls = WikiHandler().urls

for url in urls:
    #page = requests.get('https://en.wikipedia.org/wiki/The_Firemen')
    #page = requests.get('https://en.wikipedia.org/wiki/Shiroi_Ringu_he')
    #page = requests.get('https://en.wikipedia.org/wiki/Frogger')
    #page = requests.get('https://en.wikipedia.org/wiki/The_Mask_(video_game)')
    #page = requests.get('https://en.wikipedia.org/wiki/Super_R.B.I._Baseball')
    #page = requests.get('https://en.wikipedia.org/wiki/Chrono_Trigger')
    #page = requests.get('https://en.wikipedia.org/wiki/Super_3D_Noah%27s_Ark') #- TODO: - problematic, because it has strange date format
    soup = BeautifulSoup(page.content, 'html.parser')

    result = soup.find_all(class_='infobox ib-video-game hproduct')

    #getting correct and full name
    table_content = result[0].contents[0]    
    single_item = Item(title = table_content.contents[0].get_text(), platform = "SNES")
    
    single_item.prepare_dates(table_content.get_text())
    single_item.show_item_details()
     
    # for child in table_content:
    #    #getting release dates
    #    text = child.get_text()
       
    #    if "Release" in text:
    #            #print(text)
    #            print(child.get_text())
    #            if "Super NES" or "SNES" or "Super Famicom" in text:
    #                 print("Exists")
    #            else:
    #                print("Don't exist")
               
    #            #if "Super NES" or "SNES" or "Super Famicom" in text:
    #                #print(text)
    #                #single_item.get_dates(text)
    #                #single_item.show_item_details()
    #                #print("")
        
        
        
        
        #print(child.get_text())
        
            # #print(child.get_text())
            # #TODO: - if platform won't be visible, assume it was released only for one platform 
            # if "Super NES" in child.get_text():
                
            #     #single_item.get_dates()
                
            #     #multiplatform
            #     print("")
            #     #result = getNorthAmericaReleaseDate(child.get_text())
            #     #result = getJapanReleaseDate(child.get_text())
            #     #result = getEuropeReleaseDate(child.get_text())
            #     #TODO: - Super Famicom won't have Super NES as a child, so this won't be called - result = getJapanReleaseDate(child.get_text())
            # else: 
            #     #single platform
            #     print("")
            #     #result = getNorthAmericaReleaseDate(child.get_text())
            #     #result = getJapanReleaseDate(child.get_text())
            #     #result = getEuropeReleaseDate(child.get_text())
                



# for url in urls:
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')

#     for element in soup.find_all('a', href=True):
#         item = element['href']
#         if item[0:6]=='/wiki/': 
#             #TODO: - bad naming convention, to be fixed
#             if not keyword_not_forbidden(item):
#                 SNES_games.append(item)


#                 gameURL = "https://en.wikipedia.org" + element['href']
#                 pageDetails = requests.get(gameURL)
#                 soup = BeautifulSoup(pageDetails.content, 'html.parser')
#                 print(gameURL)

# for url in SNES_games:
#     print(url)

#print(f'Edited {len(SNES_games)} games for {round(time.time()-start,1)} seconds')