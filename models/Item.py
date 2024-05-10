import re

class Item:
    def __init__(self, title, platform="SNES", release_NA="———", release_PAL="———", release_JP="———", game_url=None):
        self.title = title
        self.platform = platform
        self.release_NA = release_NA
        self.release_PAL = release_PAL
        self.release_JP = release_JP
        self.game_url = game_url

    def show_item_details(self):
        print(f'Title: {self.title}')
        print(f'Platform: {self.platform}')
        print(f'NA release: {self.release_NA}')
        print(f'PAL release: {self.release_PAL}')
        print(f'JP release: {self.release_JP}')
        print(f'Wiki URL = {self.game_url}')
        print('\n')

    def prepare_dates(self, data_from_wiki):
        trimmed_text = self.initial_cleanup(data_from_wiki)
        trimmed_text = self.replace_dates(trimmed_text)
        trimmed_text = self.adjust_platform_names(trimmed_text)
        trimmed_text = self.normalize_regions(trimmed_text)
        results = self.extract_dates(trimmed_text)
        self.set_dates(results)

    def initial_cleanup(self, text):
        # Clean up text to extract relevant sections only
        text = re.sub(r'.*?(?=Release)', '', text, flags=re.S)
        text = re.sub(r'Genre.*$', '', text, flags=re.S)
        text = re.sub(r'\[\d+\]', '', text)  # Remove content in square brackets
        return text

    def replace_dates(self, text):
        # Standardize date formats and handle ranges
        text = re.sub(
            r'(January|February|March|April|May|June|July|August|September|October|November|December)-\w+\s+(\d{4})',
            r'\1 \2', text)
        text = re.sub(
            r'(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)',
            lambda x: f"{x.group(2)} {x.group(1)},", text)
        text = re.sub(
            r'(January|February|March|April|May|June|July|August|September|October|November|December)(?=\s+\d{4})',
            r'\1 01,', text)
        text = re.sub(
            r'(?<!\d, )(?!January|February|March|April|May|June|July|August|September|October|November|December)(?<!\d)(\d{4})(?!\d)',
            r'December 01, \1', text)
        return text

    def adjust_platform_names(self, text):
        # Normalize various platform names to "SNES"
        return re.sub(r'(:?\s*:?)(Super NES|SNES|Super Nintendo|Super Famicom)(:?\s*:)', 'SNES', text)

    def normalize_regions(self, text):
        # Normalize and add missing region prefixes
        months = "(January|February|March|April|May|June|July|August|September|October|November|December)"
        pattern = fr"(JP: |PAL: |EU: |NA: )?{months}"
        text = re.sub(pattern, lambda m: f"{m.group(1) if m.group(1) else 'NA: '}{m.group(2)}", text)
        text = re.sub(r':NA', 'NA', text)
        text = re.sub(r":(JP|PAL|EU|NA)\b", r"\1", text)
        text = re.sub(r'\s*(JP|NA|EU|PAL):', r'\1:', text)
        return text

    def extract_dates(self, text):
        # Extract dates for each console and region
        pattern = r"(Super NES|SNES|Super Famicom)((?:JP|NA|PAL|EU): \w+ \d{1,2}, \d{4})+"
        matches = re.finditer(pattern, text)
        results = {}
        for match in matches:
            console_name = match.group(1)
            data_matches = re.findall(r"(JP|NA|PAL|EU): (\w+ \d{1,2}, \d{4})", match.group(0))
            results[console_name] = data_matches
        return results

    def set_dates(self, results):
        # Update the release dates based on extracted results
        for console, dates in results.items():
            for region, date in dates:
                if region == "NA":
                    self.release_NA = date
                elif region == "JP":
                    self.release_JP = date
                elif region == "PAL":
                    self.release_PAL = date
