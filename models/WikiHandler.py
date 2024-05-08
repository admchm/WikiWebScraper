from utility import singleton

@singleton
class WikiHandler:
    def __init__(self):
        pass

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