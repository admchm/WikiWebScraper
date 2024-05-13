import time
import asyncio
import aiohttp
from bs4 import BeautifulSoup

from models.Item import Item
from models.WikiHandler import WikiHandler
from models.TextResources import TextRes

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def get_article_data_from_table(session, element):
    url = TextRes.get_wiki_base_adress() + element[TextRes.get_href()]
    page_details = await fetch(session, url)
            
    soup = BeautifulSoup(page_details, TextRes.get_html_attrib())
    result = soup.find_all(class_ = TextRes.get_wiki_game_details_table_name())
    return url, result

def propagate_data(wiki_handler, table_content, single_item):
    single_item.prepare_dates(table_content.get_text())
    single_item.show_item_details()
                    
    wiki_handler.SNES_games_list.append(single_item)

def increment_counter_if_dates_are_empty(wiki_handler, single_item):
    if single_item.release_JP==TextRes.empty_string and single_item.release_NA==TextRes.empty_string and single_item.release_JP==TextRes.empty_string:
        wiki_handler.counter += 1

async def main():
    wiki_handler = WikiHandler()
    start = time.time()

    print("Processing game data, it might take a while...")
    async with aiohttp.ClientSession() as session:
        tasks = []
        
        for url in wiki_handler.urls:
            page_content = await fetch(session, url)
            soup = BeautifulSoup(page_content, TextRes.get_html_attrib())

            for element in soup.find_all('a', href=True):
                url_item_name = element[TextRes.get_href()]
                if url_item_name[0:6]==TextRes.get_wiki_endpoint() and not wiki_handler.forbidden(url_item_name):
                        tasks.append(get_article_data_from_table(session, element))
                        
                        
        results = await asyncio.gather(*tasks)
        
        for url, result in results:
            if result:
                table_content = result[0].contents[0]    
                single_item = Item(title = table_content.contents[0].get_text(), game_url= url)
                propagate_data(wiki_handler, table_content, single_item)
                            
                increment_counter_if_dates_are_empty(wiki_handler, single_item)
                            
        print(f"Edited {len(wiki_handler.SNES_games_list)} games for {round(time.time()-start,1)} seconds")
        wiki_handler.calculate_objects_count()

asyncio.run(main())
