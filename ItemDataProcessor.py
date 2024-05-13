
import re

class ItemDataProcessor:
    
    @staticmethod
    def prepare_dates(data_from_wiki):
        months = r"(January|February|March|April|May|June|July|August|September|October|November|December)"
        console_names = r"(Super NES|SNES|Super Nintendo|Super Famicom)"
        region_codes = r"(JP|PAL|EU|NA)"

        # Cleaning up and processing the text from data_from_wiki
        # Remove all content before main release data or the word "Release"
        trimmed_text = re.sub(rf'.*?(?={console_names}|Release)', '', data_from_wiki, flags=re.S)

        # Remove content after "Genre" till the end of the line
        trimmed_text = re.sub(r'Genre.*$', '', trimmed_text, flags=re.S)

        # Simplify date range entries to just show the year
        trimmed_text = re.sub(fr'{months} [\-–] \w+ (\d{{4}})', r'\1', trimmed_text)

        # Remove square brackets and their numeric contents
        trimmed_text = re.sub(r'\[\d+\]', '', trimmed_text)

        # Replace all instances of "Release" with "Super NES"
        trimmed_text = re.sub(r'Release', 'Super NES', trimmed_text)

        # Format dates from "day month" to "month day,"
        pattern = rf'(\d{{1,2}})\s+{months}'
        trimmed_text = re.sub(pattern, lambda x: f"{x.group(2)} {x.group(1)},", trimmed_text)

        # Add missing day ("01,") to standalone month and year entries
        trimmed_text = re.sub(fr'({months})(?=\s+\d{{4}})', r'\1 01,', trimmed_text)
        
        #adding missing day and year if needed
        trimmed_text = re.sub(r'(?<!\d, )(?!January|February|March|April|May|June|July|August|September|October|November|December)(?<!\d)(\d{4})(?!\d)', r'December 01, \1', trimmed_text)
    
        # Add default region prefix if missing
        pattern = fr"(JP: |PAL: |EU: |NA: )?{months}"
        trimmed_text = re.sub(pattern, lambda m: f"{m.group(1) if m.group(1) else 'NA: '}{m.group(2)}", trimmed_text)
        trimmed_text = re.sub(r':NA', 'NA', trimmed_text)

        # Remove colon or extra spaces before region codes and ensure consistent formatting
        trimmed_text = re.sub(rf"\s*:?{region_codes}\b", r"\1", trimmed_text)
        trimmed_text = re.sub(rf"\s*{region_codes}:", r"\1:", trimmed_text)

        # Standardize and simplify console names to "SNES"
        trimmed_text = re.sub(rf"\s*:?{console_names}\s*:", "SNES", trimmed_text)
        trimmed_text = re.sub(console_names, "SNES", trimmed_text)

        # Search and group information about the console and regions
        pattern = rf"(SNES)(?:\s*{region_codes}: \w+ \d{{1,2}}, \d{{4}})+"
        matches = re.finditer(pattern, trimmed_text)

        results = {}
        for match in matches:
            console_name = match.group(1)
            data_matches = re.findall(rf"{region_codes}: (\w+ \d{{1,2}}, \d{{4}})", match.group(0))
            results[console_name] = data_matches

        return results
        #set_dates(results)
    
    @staticmethod    
    def set_dates(item, results):
        for console, dates in results.items():
            for region, date in dates:
                if region == "NA":
                    item.release_NA = date
                elif region == "JP":
                    item.release_JP = date
                elif region in ("EU", "PAL"):
                    item.release_PAL = date