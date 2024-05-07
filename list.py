import time
import requests
import re
from bs4 import BeautifulSoup

urls = [#"https://en.wikipedia.org/wiki/Category:Super_Nintendo_Entertainment_System_games", 
        #"https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Donkey+Kong+Country+2%3A+Diddy%27s+Kong+Quest#mw-pages",
        #"https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Kick+Off+%28Series%29%0AKick+Off+%28series%29#mw-pages",
        #"https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Phalanx+%28video+game%29#mw-pages",
        #"https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Super+Bonk#mw-pages",
        "https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Wwf+Wrestlemania%3A+The+Arcade+Game%0AWWF+WrestleMania%3A+The+Arcade+Game#mw-pages"]

def keyword_not_forbidden(url):
    forbidden_keyword = ["Wikipedia:", "Help:", "Category", "Special:", "Portal:", "Main_Page", "Nintendo_Entertainment"]
    
    for keyword in forbidden_keyword:
        if keyword in url:
            return True
            
    return False

def findNorthAmericaDate(text):
    pattern = r'Super NES[^G]+NA:\s*([A-Z][a-z]+ \d{1,2}, \d{4})'
    date = re.search(pattern, text)

    if date:
        print(date.group(1))
    else:
        print("No date found for Super NES NA release.")

SNES_games = []
start = time.time()

for url in urls:
    page = requests.get('https://en.wikipedia.org/wiki/Yoshi%27s_Island')
    soup = BeautifulSoup(page.content, 'html.parser')

    result = soup.find_all(class_='infobox ib-video-game hproduct')

    
    # print(result[0].get_text())
    



    #getting correct and full name
    table_content = result[0].contents[0]
    res = table_content.contents[0].get_text()
    #print(res)
    
    #getting release
    table_content = result[0].contents[0]
    
    for child in table_content:
        #print(child.get_text())
        if "Release" in child.get_text():
            print(child.get_text())
            if "Super NES" in child.get_text():
                print("contains")
                result = findNorthAmericaDate(child.get_text())

    #print(len(list(table_content.children)))

    #for child in table_content.descendants:
    #    print(child.get_text())
    
    
    # result[0].child
    # soup.findChild()
    # child - infobox-data

# for url in urls:
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')

#     for element in soup.find_all('a', href=True):
#         item = element['href']
#         if item[0:6]=='/wiki/': 
#             #TODO: bad naming convention, to be fixed
#             if not keyword_not_forbidden(item):
#                 SNES_games.append(item)


#                 gameURL = "https://en.wikipedia.org" + element['href']
#                 pageDetails = requests.get(gameURL)
#                 soup = BeautifulSoup(pageDetails.content, 'html.parser')
#                 print(gameURL)

# for url in SNES_games:
#     print(url)

#print(f'Edited {len(SNES_games)} games for {round(time.time()-start,1)} seconds')