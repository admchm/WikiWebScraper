import re
from typing import Self

class Item:
    def __init__(self, title, platform, release_NA="———", release_PAL="———", release_JP="———"):
        self.title = title
        self.platform = platform
        self.release_NA = release_NA
        self.release_PAL = release_PAL
        self.release_JP = release_JP

    def show_item_details(self):
        print(f'Title: {self.title}')
        print(f'Platform: {self.platform}')
        print(f'NA release: {self.release_NA}')
        print(f'PAL release: {self.release_PAL}')
        print(f'JP release: {self.release_JP}')
    
    def prepare_dates(self, data_from_wiki):
        #getting all release dates for all platforms
        trimmed_text = re.sub(r'.*?(?=Super NES|SNES|Super Famicom)', '', data_from_wiki, flags=re.S)
        trimmed_text = re.sub(r'.*?(?=Release)', '', trimmed_text, flags=re.S)
        trimmed_text = re.sub(r'Genre.*$', '', trimmed_text, flags=re.S)
        
        #print(trimmed_text)
        #if month was written like May-June, we're going to take the first part into consideration
        trimmed_text = re.sub(r'(January|February|March|April|May|June|July|August|September|October|November|December)-\w+\s+(\d{4})', r'\1 \2', trimmed_text)
        
        #removing square brackets with its content
        trimmed_text = re.sub(r'\[\d+\]', '', trimmed_text)

        #changing "Release" for "SNES" so it could be processed; It might be problematic, so testing might be needed
        trimmed_text = re.sub(r'Release', 'Super NES', trimmed_text)

        # adding missing day if needed
        trimmed_text = re.sub(r'(January|February|March|April|May|June|July|August|September|October|November|December)(?=\s+\d{4})', r'\1 01,', trimmed_text)
        
        #TODO: - adding missing day and year if needed
        #trimmed_text = re.sub(r'(?<!\d)(?<!\w)(\d{4})(?!\d)', r'December 01, \1', trimmed_text) - not working correctly, but could be fixed
        #trimmed_text = re.sub(r'(?<!\d)(\d{4})(?!\d)', r'December 01, \1', trimmed_text) - should be working ok
    
        pattern = r"(Super NES|SNES|Super Famicom)(?:((?:JP|NA|PAL|EU): \w+ \d{1,2}, \d{4}))+"
        matches = re.finditer(pattern, trimmed_text)

        results = {}
        for match in matches:
            console_name = match.group(1)
            data_matches = re.findall(r"(JP|NA|PAL|EU): (\w+ \d{1,2}, \d{4})", match.group(0))
            results[console_name] = data_matches

        self.set_dates(results)  
        # for console, dates in results.items():
        #     print(f"{console}:")
        #     for region, date in dates:
        #         print(f"  {region}: {date}")
            
    def set_dates(self, results):
        for console, dates in results.items():
            #print(results.item)
            #print(f"{console}:")
            for region, date in dates:
                print(region, date)
                if region == "NA":
                    self.release_NA = date
                elif region == "JP":
                    self.release_JP = date
                else:
                    self.release_PAL = date