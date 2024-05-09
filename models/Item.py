import re

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
        
        #if month was written like May-June, we're going to take the first part into consideration
        trimmed_text = re.sub(r'(January|February|March|April|May|June|July|August|September|October|November|December)-\w+\s+(\d{4})', r'\1 \2', trimmed_text)
        
        #removing square brackets with its content
        trimmed_text = re.sub(r'\[\d+\]', '', trimmed_text)
        
        #changing "Release" for "SNES" so it could be processed
        trimmed_text = re.sub(r'Release', 'Super NES', trimmed_text)
        
        pattern = r'(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)'
        trimmed_text = re.sub(pattern, lambda x: f"{x.group(2)} {x.group(1)},", trimmed_text)
        #print(trimmed_text)
        
        # adding missing day if needed
        trimmed_text = re.sub(r'(January|February|March|April|May|June|July|August|September|October|November|December)(?=\s+\d{4})', r'\1 01,', trimmed_text)
        
        #adding missing day and year if needed
        trimmed_text = re.sub(r'(?<!\d, )(?!January|February|March|April|May|June|July|August|September|October|November|December)(?<!\d)(\d{4})(?!\d)', r'December 01, \1', trimmed_text)
        
        #if region prefix is completely missing, add NA:
        months = "(January|February|March|April|May|June|July|August|September|October|November|December)"
        pattern = fr"(JP: |PAL: |EU: |NA: )?{months}"
        trimmed_text = re.sub(pattern, lambda m: f"{m.group(1) if m.group(1) else 'NA: '}{m.group(2)}", trimmed_text)
        trimmed_text = re.sub(r':NA', 'NA', trimmed_text)    
        
        #if region is preceeded by :
        trimmed_text = re.sub(r":(JP|PAL|EU|NA)\b", r"\1", trimmed_text)
        
        #if region is preceeded by space
        trimmed_text = re.sub(r'\s*(JP|NA|EU|PAL):', r'\1:', trimmed_text)
        
        #swap Super NES, SNES, Famicom etc. to SNES
        pattern = r'(:?\s*:?)(Super NES|SNES|Super Nintendo|Super Famicom)(:?\s*:)'
        trimmed_text = re.sub(pattern, 'SNES', trimmed_text)
        
        #use only SNES, because text will be altered to that keyword
        pattern = r"(Super NES|SNES|Super Famicom)(?:((?:JP|NA|PAL|EU): \w+ \d{1,2}, \d{4}))+"
        matches = re.finditer(pattern, trimmed_text)

        results = {}
        for match in matches:
            console_name = match.group(1)
            data_matches = re.findall(r"(JP|NA|PAL|EU): (\w+ \d{1,2}, \d{4})", match.group(0))
            results[console_name] = data_matches

        self.set_dates(results)  
            
    def set_dates(self, results):
        for console, dates in results.items():
            for region, date in dates:
                if region == "NA":
                    self.release_NA = date
                elif region == "JP":
                    self.release_JP = date
                else:
                    self.release_PAL = date