import time
import requests

from bs4 import BeautifulSoup
from models.Item import Item
from models.WikiHandler import WikiHandler
from models.TextResources import TextRes

shared = WikiHandler()
start = time.time()

def get_article_data_from_table(element):
    url = TextRes.get_wiki_base_adress() + element[TextRes.get_href()]
    page_details = requests.get(url)
                
    soup = BeautifulSoup(page_details.content, TextRes.get_html_attrib())
    result = soup.find_all(class_ = TextRes.get_wiki_game_details_table_name())
    return url,result

def propagate_data(shared, table_content, single_item):
    single_item.prepare_dates(table_content.get_text())
    single_item.show_item_details()
                    
    shared.SNES_games_list.append(single_item)

def increment_counter_if_dates_are_empty(shared, single_item):
    if single_item.release_JP==TextRes.empty_string and single_item.release_NA==TextRes.empty_string and single_item.release_JP==TextRes.empty_string:
        shared.counter += 1

for url in shared.urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, TextRes.get_html_attrib())

    for element in soup.find_all('a', href=True):
        url_item_name = element[TextRes.get_href()]
        
        if url_item_name[0:6]==TextRes.get_wiki_endpoint():
             
            if not shared.forbidden(url_item_name):
                url, result = get_article_data_from_table(element)
                
                if result:
                    table_content = result[0].contents[0]    
                    single_item = Item(title = table_content.contents[0].get_text(), game_url= url)
                    propagate_data(shared, table_content, single_item)
                    
                    increment_counter_if_dates_are_empty(shared, single_item)
                    
print(f"Edited {len(shared.SNES_games_list)} games for {round(time.time()-start,1)} seconds")

shared.calculate_objects_count
