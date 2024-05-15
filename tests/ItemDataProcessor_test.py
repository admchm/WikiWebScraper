import pytest
from ItemDataProcessor import ItemDataProcessor

def test_remove_characters_before_release_output():
    data_from_wiki = "Virtual BartDeveloper(s)Sculptured SoftwarePublisher(s)Acclaim EntertainmentPlatform(s)Super NES, GenesisReleaseSuper NESNA: September 26, 1994JP: September 30, 1994PAL: 1994GenesisNA: 1994PAL: 1994JP: December 31, 1995Mode(s)Single-player"
    console_names = r"(Super NES|SNES|Super Nintendo|Super Famicom)"
    
    result = "Release" + ItemDataProcessor.remove_characters_before_release_keyword(data_from_wiki, console_names)
    output = "ReleaseSuper NESNA: September 26, 1994JP: September 30, 1994PAL: 1994GenesisNA: 1994PAL: 1994JP: December 31, 1995Mode(s)Single-player"

    assert result == output
    
def test_remove_characters_before_release_if_it_starts_with_release_keyword():
    data_from_wiki = "Virtual BartDeveloper(s)Sculptured SoftwarePublisher(s)Acclaim EntertainmentPlatform(s)Super NES, GenesisReleaseSuper NESNA: September 26, 1994JP: September 30, 1994PAL: 1994GenesisNA: 1994PAL: 1994JP: December 31, 1995Mode(s)Single-player"
    console_names = r"(Super NES|SNES|Super Nintendo|Super Famicom)"
    
    result = ItemDataProcessor.remove_characters_before_release_keyword(data_from_wiki, console_names)
    
    assert result[0:7] == "Release"
    
def simplify_date_ranges():
    data = ""
    months = ""
    
    pass
    
def remove_square_brackets():
    data = ""
    
    pass
    
def replace_release_keyword_with_platform_name():
    data = ""
    
    pass
    
def format_dates():
    data = ""
    months = ""
    
    pass
    
def add_missing_day_to_months():
    data = ""
    months = ""
    
    pass
    
def add_missing_day_and_year_if_needed():
    data = ""
    
    pass
    
def add_default_region_prefix():
    data = ""
    months = ""
    
    pass
    
def remove_colon_before_region_codes():
    data = ""
    region_codes = ""
    
    pass
    
def simplify_searched_console_names():
    data = ""
    console_names = ""
    
    pass
        
        
    

    
    
        