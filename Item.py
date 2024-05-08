import re

class Item:
    def __init__(self, title, platform, release_NA, release_PAL, release_JP):
        self.title = title
        self.platform = platform
        self.release_NA = release_NA
        self.release_PAL = release_PAL
        self.release_JP = release_JP

    def show_item_details(self):
        print(f'Title: {self.title}')
        print(f'Platform: {self.platform}')
        print(f'NA release: {self.title}')
        print(f'PAL release: {self.title}')
        print(f'JP release: {self.title}')

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