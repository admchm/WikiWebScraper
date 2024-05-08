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
        
        #removing square brackets with its content
        trimmed_text = re.sub(r'\[\d+\]', '', trimmed_text)

        #changing "Release" for "SNES" so it could be processed; It might be problematic, so testing might be needed
        trimmed_text = re.sub(r'Release', 'Super NES', trimmed_text)

        # adding missing day if needed
        trimmed_text = re.sub(r'(January|February|March|April|May|June|July|August|September|October|November|December)(?=\s+\d{4})', r'\1 01,', trimmed_text)
        
        #TODO: - adding missing day and year if needed
        #trimmed_text = re.sub(r'(?<!\d)(?<!\w)(\d{4})(?!\d)', r'December 01, \1', trimmed_text) - not working correctly, but could be fixed
    
        pattern = r"(Super NES|SNES|Super Famicom)(?:((?:JP|NA|PAL|EU): \w+ \d{1,2}, \d{4}))+"
        matches = re.finditer(pattern, trimmed_text)

        results = {}
        for match in matches:
            console_name = match.group(1)
            data_matches = re.findall(r"(JP|NA|PAL|EU): (\w+ \d{1,2}, \d{4})", match.group(0))
            results[console_name] = data_matches

            
        for console, dates in results.items():
            print(f"{console}:")
            for region, date in dates:
                print(f"  {region}: {date}")
            
    def get_dates(self, text):
        self.handle_NA_release(text)
        self.handle_PAL_release()
        self.handle_JP_release()        
    
    def handle_NA_release(self, text):
        # NA non-exclusive day & month & year release - done https://en.wikipedia.org/wiki/ClayFighter_(video_game)
        # NA exclusive day & month & year release
        # NA exclusive month & year release - done https://en.wikipedia.org/wiki/Super_R.B.I._Baseball
        # NA exclusive single year release - done https://en.wikipedia.org/wiki/Super_3D_Noah%27s_Ark
        
        #self.release_NA = "01.01.1991"
        #pattern = r'(Super NES|SNES)[^G]+NA:\s*([A-Z][a-z]+ \d{1,2}, \d{4})'
        
        pattern = r'ReleaseSuper NESNA:\s*([A-Z][a-z]+ \d{1,2}, \d{4})'
        date = re.search(pattern, text)
        if date:
            self.release_NA = date.group(1)
        
        pattern = r'\b([A-Z][a-z]+ \d{4})\b'
        date = re.search(pattern, text)
        print(date)
        
        if date:
            self.release_NA = date.group(1)
            
        pattern = r'ReleaseSNESNA:\s*(\d{4})'
        date = re.search(pattern, text)
        print(date)
        
        if date:
            self.release_NA = date.group(1)
        
        
    def handle_PAL_release(self):
        # PAL exclusive single year release
        # PAL exclusive month & year release
        # PAL exclusive day & month & year release
        self.release_PAL = "———"
        
    def handle_JP_release(self):
        # JP exclusive day & month & year release - https://en.wikipedia.org/wiki/Zenkoku_Kōkō_Soccer
        # JP exclusive month & year release
        # JP exclusive single year release
        self.release_JP = "———"
        
        
        
        
        
        
        
    #TODO: - combine function for getting release dates for three regions, for now it's duplicated
    def getNorthAmericaReleaseDate(text):
        #pattern = r'Super NES[^G]+NA:\s*([A-Z][a-z]+ \d{1,2}, \d{4})'
        pattern = r'(Super NES|SNES)[^G]+NA:\s*([A-Z][a-z]+ \d{1,2}, \d{4})'
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


# cases to handle:
# make sure that multiplatforms are also working correctly with specific format days

#TODO: - potential problem with urls that contain ' character
#TODO: - change back to the url variable; 
#TODO: - if only one platform exist under the release with only one region, the date won't be working correctly. Examples: https://en.wikipedia.org/wiki/Shiroi_Ringu_he or https://en.wikipedia.org/wiki/Super_R.B.I._Baseball
#TODO: - for some links, wrong platform is taken into consideration - https://en.wikipedia.org/wiki/Chrono_Trigger