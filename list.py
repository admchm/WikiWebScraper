import time
import requests
import re
from bs4 import BeautifulSoup

# cases to handle:
# JP exclusive single year release
# NA exclusive single year release
# PAL exclusive single year release
# JP exclusive month & year release
# NA exclusive month & year release
# PAL exclusive month & year release
# JP exclusive day & month & year release
# NA exclusive day & month & year release
# PAL exclusive day & month & year release

def keyword_not_forbidden(url):
    forbidden_keyword = ["Wikipedia:", "Help:", "Category", "Special:", "Portal:", "Main_Page", "Nintendo_Entertainment"]
    
    for keyword in forbidden_keyword:
        if keyword in url:
            return True
            
    return False

#TODO: - combine function for getting release dates for three regions, for now it's duplicated
def getNorthAmericaReleaseDate(text):
    pattern = r'Super NES[^G]+NA:\s*([A-Z][a-z]+ \d{1,2}, \d{4})'
    date = re.search(pattern, text)

    if date:
        print(f"NA release: {date.group(1)}")
    else:
        pattern = r'\b([A-Z][a-z]+ \d{4})\b' #TODO: works only for single month
        date = re.search(pattern, text)
        print(text)
        if date:
            print(f"NA release: {date.group(1)}")
        else:
            print("No date found for NA release.")

def getJapanReleaseDate(text):
    pattern = r'Super NESJP:\s*([A-Z][a-z]+ \d{1,2}, \d{4})'
    date = re.search(pattern, text)

    if date:
        print(f"JP release: {date.group(1)}")
    else:
        #print("No date found for Super NES JP release.")
        #if won't be found, look for default date
        pattern = r'\b([A-Z][a-z]+ \d{1,2}, \d{4})\b'
        date = re.search(pattern, text)

        if date:
            print(f"JP release: {date.group(1)}")
        else:
            print("No date found for JP release.")

def getEuropeReleaseDate(text):
    pattern = r'Super NES[^G]+EU:\s*([A-Z][a-z]+ \d{1,2}, \d{4})'
    date = re.search(pattern, text)

    if date:
        print(f"PAL release: {date.group(1)}")
    else:
        print("No date found for Super NES EU release.")

urls = [#"https://en.wikipedia.org/wiki/Category:Super_Nintendo_Entertainment_System_games", 
        #"https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Donkey+Kong+Country+2%3A+Diddy%27s+Kong+Quest#mw-pages",
        #"https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Kick+Off+%28Series%29%0AKick+Off+%28series%29#mw-pages",
        #"https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Phalanx+%28video+game%29#mw-pages",
        #"https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Super+Bonk#mw-pages",
        "https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Wwf+Wrestlemania%3A+The+Arcade+Game%0AWWF+WrestleMania%3A+The+Arcade+Game#mw-pages"]


SNES_games = []
start = time.time()

for url in urls:
    #TODO: - potential problem with urls that contain ' character
    #TODO: - change back to the url variable; 
    #TODO: - if only one platform exist under the release with only one region, the date won't be working correctly. Examples: https://en.wikipedia.org/wiki/Shiroi_Ringu_he or https://en.wikipedia.org/wiki/Super_R.B.I._Baseball
    #TODO: - for some links, wrong platform is taken into consideration - https://en.wikipedia.org/wiki/Chrono_Trigger
    page = requests.get('https://en.wikipedia.org/wiki/Super_R.B.I._Baseball') 
    soup = BeautifulSoup(page.content, 'html.parser')

    result = soup.find_all(class_='infobox ib-video-game hproduct')

    
    #getting correct and full name
    table_content = result[0].contents[0]
    res = table_content.contents[0].get_text()
    print(res)
    
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