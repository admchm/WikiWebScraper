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
            
    def get_dates(self):
        self.handle_NA_release()
        self.handle_PAL_release()
        self.handle_JP_release()        
    
    def handle_NA_release(self):
        self.release_NA = "01.01.1991"
        
    def handle_PAL_release(self):
        self.release_PAL = "01.02.1992"
        
    def handle_JP_release(self):
        self.release_JP = "03.07.2001"
        
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
# make sure that multiplatforms are also working correctly with specific format days

#TODO: - potential problem with urls that contain ' character
#TODO: - change back to the url variable; 
#TODO: - if only one platform exist under the release with only one region, the date won't be working correctly. Examples: https://en.wikipedia.org/wiki/Shiroi_Ringu_he or https://en.wikipedia.org/wiki/Super_R.B.I._Baseball
#TODO: - for some links, wrong platform is taken into consideration - https://en.wikipedia.org/wiki/Chrono_Trigger