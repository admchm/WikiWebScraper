import re

class ItemDataProcessor:
    
    @staticmethod
    def remove_characters_before_release_keyword(data, console_names):
        return re.sub(rf'.*?(?={console_names}|Release)', '', data, flags=re.S)

    @staticmethod
    def remove_content_after_genre(data):
        return re.sub(r'Genre.*$', '', data, flags=re.S)

    @staticmethod
    def simplify_date_ranges(data, months):
        return re.sub(fr'{months} [\-–] \w+ (\d{{4}})', r'\1', data)

    @staticmethod
    def remove_square_brackets(data):
        return re.sub(r'\[\d+\]', '', data)

    @staticmethod
    def replace_release_keyword_with_platform_name(data):
        return re.sub(r'Release', 'Super NES', data)

    @staticmethod
    def format_dates(data, months):
        pattern = rf'(\d{{1,2}})\s+{months}'
        return re.sub(pattern, lambda x: f"{x.group(2)} {x.group(1)},", data)

    @staticmethod
    def add_missing_day_to_months(data, months):
        return re.sub(fr'({months})(?=\s+\d{{4}})', r'\1 01,', data)

    @staticmethod
    def add_missing_day_and_year_if_needed(data):
        return re.sub(r'(?<!\d, )(?!January|February|March|April|May|June|July|August|September|October|November|December)(?<!\d)(\d{4})(?!\d)', r'December 01, \1', data)

    @staticmethod
    def add_default_region_prefix(data, months):
        pattern = fr"(JP: |PAL: |EU: |NA: )?{months}"
        data = re.sub(pattern, lambda m: f"{m.group(1) if m.group(1) else 'NA: '}{m.group(2)}", data)
        return re.sub(r':NA', 'NA', data)

    @staticmethod
    def remove_colon_before_region_codes(data, region_codes):
        data = re.sub(rf"\s*:?{region_codes}\b", r"\1", data)
        return re.sub(rf"\s*{region_codes}:", r"\1:", data)

    @staticmethod
    def simplify_searched_console_names(data, console_names):
        data = re.sub(rf"\s*:?{console_names}\s*:", "SNES", data)
        return re.sub(console_names, "SNES", data)

    @staticmethod    
    def set_dates(results, item):
        
        for region, date in results:
            if region == "NA":
                item.release_NA = date
            elif region == "JP":
                item.release_JP = date
            elif region in ("EU", "PAL"):
                item.release_PAL = date
 
    @staticmethod
    def search_and_group_data(data, region_codes, item):
        pattern = rf"(SNES)(?:\s*({region_codes}): (\w+ \d{{1,2}}, \d{{4}}))+"
        matches = re.finditer(pattern, data)
        results = {}
        for match in matches:
            console_name = match.group(1)
            results = re.findall(rf"{region_codes}: (\w+ \d{{1,2}}, \d{{4}})", match.group(0))

        ItemDataProcessor.set_dates(results, item)

    @staticmethod
    def prepare_dates(data_from_wiki, item):
        months = r"(January|February|March|April|May|June|July|August|September|October|November|December)"
        console_names = r"(Super NES|SNES|Super Nintendo|Super Famicom)"
        region_codes = r"(JP|PAL|EU|NA)"

        data = ItemDataProcessor.remove_characters_before_release_keyword(data_from_wiki, console_names)
        data = ItemDataProcessor.remove_content_after_genre(data)
        data = ItemDataProcessor.simplify_date_ranges(data, months)
        data = ItemDataProcessor.remove_square_brackets(data)
        data = ItemDataProcessor.replace_release_keyword_with_platform_name(data)
        data = ItemDataProcessor.format_dates(data, months)
        data = ItemDataProcessor.add_missing_day_to_months(data, months)
        data = ItemDataProcessor.add_missing_day_and_year_if_needed(data)
        data = ItemDataProcessor.add_default_region_prefix(data, months)
        data = ItemDataProcessor.remove_colon_before_region_codes(data, region_codes)
        data = ItemDataProcessor.simplify_searched_console_names(data, console_names)
        
        return ItemDataProcessor.search_and_group_data(data, region_codes, item)