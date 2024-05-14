import time
import asyncio
import aiohttp

from aiohttp import ClientError
from bs4 import BeautifulSoup

from ItemDataProcessor import ItemDataProcessor
from models.Item import Item
from WikiHandler import WikiHandler
from models.TextResources import TextRes

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status() # Throw an exception if HTTP status will be 4xx/5xx
            return await response.text()
        
    except (ClientError, aiohttp.TimeoutError) as e:
        print(f"Error fetching URL {url}: {str(e)}")
        return None

async def get_article_data_from_table(session, element):
    url = TextRes.get_wiki_base_adress() + element[TextRes.get_href()]
    
    try: 
        page_details = await fetch(session, url)
        soup = BeautifulSoup(page_details, TextRes.get_html_attrib())
        result = soup.find_all(class_ = TextRes.get_wiki_game_details_table_name())
        return url, result
    
    except Exception as e:
        print(f"Error processing data from table for article: {str(e)}")
        return None

def propagate_data(wiki_handler, table_content, single_item, processor):
    data_from_wiki = table_content.get_text()
    
    processor.prepare_dates(data_from_wiki, single_item)
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
            
            if page_content is None:
                print("ERROR: page_content is empty!")
                continue
            
            soup = BeautifulSoup(page_content, TextRes.get_html_attrib())

            for element in soup.find_all('a', href=True):
                url_item_name = element[TextRes.get_href()]
                if url_item_name[0:6]==TextRes.get_wiki_endpoint() and not wiki_handler.forbidden(url_item_name):
                        tasks.append(get_article_data_from_table(session, element))
                        
        try:                        
            results = await asyncio.gather(*tasks, return_exceptions=True)
            for url, result in results:
                #if result is None or isinstance(result, Exception):
                
                if result and result[0]: #result might be empty at this point, because table in article might be collapsed
                    if result is None or isinstance(result, Exception):
                        continue
                
                    table_content = result[0].contents[0]    
                    single_item = Item(title = table_content.contents[0].get_text(), game_url= url)
                    processor = ItemDataProcessor()
                
                    propagate_data(wiki_handler, table_content, single_item, processor)
                    increment_counter_if_dates_are_empty(wiki_handler, single_item)
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
                            
        print(f"Edited {len(wiki_handler.SNES_games_list)} games for {round(time.time()-start,1)} seconds")
        wiki_handler.calculate_objects_count()

asyncio.run(main())
