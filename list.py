import time
import requests
from bs4 import BeautifulSoup

urls = ["https://en.wikipedia.org/wiki/Category:Super_Nintendo_Entertainment_System_games", 
        "https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Donkey+Kong+Country+2%3A+Diddy%27s+Kong+Quest#mw-pages",
        "https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Kick+Off+%28Series%29%0AKick+Off+%28series%29#mw-pages",
        "https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Phalanx+%28video+game%29#mw-pages",
        "https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Super+Bonk#mw-pages",
        "https://en.wikipedia.org/w/index.php?title=Category:Super_Nintendo_Entertainment_System_games&pagefrom=Wwf+Wrestlemania%3A+The+Arcade+Game%0AWWF+WrestleMania%3A+The+Arcade+Game#mw-pages"]

def keyword_not_forbidden(url):
    forbidden_keyword = ["Wikipedia:", "Help:", "Category:", "Special:", "Portal:", "Main_Page", "List_of_Super_Nintendo_Entertainment_System_games:"]
    
    for keyword in forbidden_keyword:
        if keyword in url:
            return True
            
    return False


SNES_games = []
start = time.time()

for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for element in soup.find_all('a', href=True):
        item = element['href']
        if item[0:6]=='/wiki/': 
            #TODO: bad naming convention, to be fixed
            if not keyword_not_forbidden(item):
                SNES_games.append(item)

for url in SNES_games:
    print(url)

print(f'Edited {len(SNES_games)} games for {round(time.time()-start,1)} seconds')