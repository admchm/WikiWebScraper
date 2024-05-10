import time
import requests
from bs4 import BeautifulSoup

from models.Item import Item
from models.WikiHandler import WikiHandler
from models.TextResources import TextRes

shared = WikiHandler()
start = time.time()

for url in shared.urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, TextRes.get_html_attrib())

    for element in soup.find_all('a', href=True):
        item = element[TextRes.get_href()]
        if item[0:6]==TextRes.get_wiki_endpoint(): 
            #TODO: - bad naming convention, to be fixed
            if not shared.keyword_not_forbidden(item):
                url = TextRes.get_wiki_base_adress() + element[TextRes.get_href()]
                page_details = requests.get(url)
                soup = BeautifulSoup(page_details.content, TextRes.get_html_attrib())
                result = soup.find_all(class_ = TextRes.get_wiki_game_details_table_name())
                
                if result:
                    table_content = result[0].contents[0]    
                    single_item = Item(title = table_content.contents[0].get_text(), game_url= url)
                    single_item.prepare_dates(table_content.get_text())
                    single_item.show_item_details()
                    
                    shared.SNES_games_list.append(single_item)
                    
                    if single_item.release_JP==TextRes.empty_string and single_item.release_NA==TextRes.empty_string and single_item.release_JP==TextRes.empty_string:
                        shared.counter += 1
                    
print(f"Edited {len(shared.SNES_games_list)} games for {round(time.time()-start,1)} seconds")

shared.calculate_objects_count
