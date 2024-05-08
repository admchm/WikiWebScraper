import time
import requests
from bs4 import BeautifulSoup

from models.Item import Item
from models.WikiHandler import WikiHandler


SNES_games = []
start = time.time()

for url in WikiHandler.urls:
    #TODO: - potential problem with urls that contain ' character
    #TODO: - change back to the url variable; 
    #TODO: - if only one platform exist under the release with only one region, the date won't be working correctly. Examples: https://en.wikipedia.org/wiki/Shiroi_Ringu_he or https://en.wikipedia.org/wiki/Super_R.B.I._Baseball
    #TODO: - for some links, wrong platform is taken into consideration - https://en.wikipedia.org/wiki/Chrono_Trigger
    page = requests.get('https://en.wikipedia.org/wiki/Super_R.B.I._Baseball') 
    soup = BeautifulSoup(page.content, 'html.parser')

    result = soup.find_all(class_='infobox ib-video-game hproduct')

    
    #getting correct and full name
    table_content = result[0].contents[0]
    single_item = table_content.contents[0].get_text()
    
    single_item = Item(title = single_item, platform = "SNES")
    #getting release dates
    table_content = result[0].contents[0]
    
    for child in table_content:
        #print(child.get_text())
        if "Release" in child.get_text():
            #print(child.get_text())
            #TODO: - if platform won't be visible, assume it was released only for one platform 
            if "Super NES" in child.get_text():
                #multiplatform
                result = getNorthAmericaReleaseDate(child.get_text())
                result = getJapanReleaseDate(child.get_text())
                result = getEuropeReleaseDate(child.get_text())
                #TODO: - Super Famicom won't have Super NES as a child, so this won't be called - result = getJapanReleaseDate(child.get_text())
            else: 
                #single platform
                result = getNorthAmericaReleaseDate(child.get_text())
                result = getJapanReleaseDate(child.get_text())
                result = getEuropeReleaseDate(child.get_text())
                



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