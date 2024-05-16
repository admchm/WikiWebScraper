import pytest
import re
    
@pytest.mark.parametrize("input_string, expected_result", [
    ("""Wing CommanderDeveloper(s)Origin SystemsPublisher(s)Origin SystemsDirector(s)Chris RobertsProducer(s)Chris Roberts  Warren SpectorDesigner(s)Chris RobertsWriter(s)Jeff GeorgeComposer(s)George Alistair Sanger  David GovettPlatform(s)MS-DOSSuper NES, Amiga, Amiga CD32, Sega CD, 3DO, PlayStation, PlayStation Portable, FM Towns, Macintosh, Windows 95ReleaseSeptember 26, 1990September 26, 1990 (MS-DOS)March 1, 1992 (SNES)September 1992 (Amiga)[1]June 1, 1993 (Amiga CD32)March 1994 (Sega CD)August 1995 (Mac)[2]November 30, 1996 (Windows 95)Genre(s)Space flight simulationMode(s)Single-player""",
     """Wing CommanderDeveloper(s)Origin SystemsPublisher(s)Origin SystemsDirector(s)Chris RobertsProducer(s)Chris Roberts  Warren SpectorDesigner(s)Chris RobertsWriter(s)Jeff GeorgeComposer(s)George Alistair Sanger  David GovettPlatform(s)MS-DOSSuper NES, Amiga, Amiga CD32, Sega CD, 3DO, PlayStation, PlayStation Portable, FM Towns, Macintosh, Windows 95ReleaseSeptember 26, 1990September 26, 1990 (MS-DOS)March 1, 1992 (SNES)September 1992 (Amiga)June 1, 1993 (Amiga CD32)March 1994 (Sega CD)August 1995 (Mac)November 30, 1996 (Windows 95)Genre(s)Space flight simulationMode(s)Single-player"""),
    ("Zero4 ChampDeveloper(s)Media RingsPublisher(s)Media RingsDirector(s)Yutaka KaminagaPlatform(s)PC EngineReleaseJP: 1991Genre(s)Racing video gameMode(s)Single-player, multiplayer",
     "Zero4 ChampDeveloper(s)Media RingsPublisher(s)Media RingsDirector(s)Yutaka KaminagaPlatform(s)PC EngineReleaseJP: 1991Genre(s)Racing video gameMode(s)Single-player, multiplayer"),
    ("[2022] New data released", " New data released"),
    ("s$$$@[342]##a", "s$$$@##a")
])
def test_remove_square_brackets(input_string, expected_result):
    result = re.sub(r'\[\d+\]', '', input_string)
    
    assert result == expected_result

@pytest.mark.parametrize("input_string, expected_result", [
    ("""Wing CommanderDeveloper(s)Origin SystemsPublisher(s)Origin SystemsDirector(s)Chris RobertsProducer(s)Chris Roberts  Warren SpectorDesigner(s)Chris RobertsWriter(s)Jeff GeorgeComposer(s)George Alistair Sanger  David GovettPlatform(s)MS-DOSSuper NES, Amiga, Amiga CD32, Sega CD, 3DO, PlayStation, PlayStation Portable, FM Towns, Macintosh, Windows 95ReleaseSeptember 26, 1990September 26, 1990 (MS-DOS)March 1, 1992 (SNES)September 1992 (Amiga)June 1, 1993 (Amiga CD32)March 1994 (Sega CD)August 1995 (Mac)November 30, 1996 (Windows 95)Genre(s)Space flight simulationMode(s)Single-player""",
     """Wing CommanderDeveloper(s)Origin SystemsPublisher(s)Origin SystemsDirector(s)Chris RobertsProducer(s)Chris Roberts  Warren SpectorDesigner(s)Chris RobertsWriter(s)Jeff GeorgeComposer(s)George Alistair Sanger  David GovettPlatform(s)MS-DOSSuper NES, Amiga, Amiga CD32, Sega CD, 3DO, PlayStation, PlayStation Portable, FM Towns, Macintosh, Windows 95Super NESSeptember 26, 1990September 26, 1990 (MS-DOS)March 1, 1992 (SNES)September 1992 (Amiga)June 1, 1993 (Amiga CD32)March 1994 (Sega CD)August 1995 (Mac)November 30, 1996 (Windows 95)Genre(s)Space flight simulationMode(s)Single-player"""),
    ("Final FantasyRelease date: 1987Release info: Initially released in Japan. Success led to international releases.",
     "Final FantasySuper NES date: 1987Super NES info: Initially released in Japan. Success led to international releases."),
    ("Release", "Super NES"),
    ("#3#$#Release$", "#3#$#Super NES$")
])
def test_replace_release_keyword_with_platform_name(input_string, expected_result):
    result =  re.sub(r'Release', 'Super NES', input_string)
    
    assert result == expected_result
    
def test_format_dates():
    data = ""
    months = ""
    
    pass
    
def test_add_missing_day_to_months():
    data = ""
    months = ""
    
    pass
    
def test_add_missing_day_and_year_if_needed():
    data = ""
    
    pass
    
def test_add_default_region_prefix():
    data = ""
    months = ""
    
    pass
    
def test_simplify_searched_console_names():
    data = ""
    console_names = ""
    
    pass
        
def test_search_and_group_data():
    data = ""
    region_codes = ""
    item = ""
    
    pass

    
    
        