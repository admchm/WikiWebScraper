import pytest
import re

from src.ItemDataProcessor import ItemDataProcessor
    
@pytest.mark.parametrize("input_string, expected_result", [
    ("""Wing CommanderDeveloper(s)Origin SystemsPublisher(s)Origin SystemsDirector(s)Chris RobertsProducer(s)Chris Roberts  Warren SpectorDesigner(s)Chris RobertsWriter(s)Jeff GeorgeComposer(s)George Alistair Sanger  David GovettPlatform(s)MS-DOSSuper NES, Amiga, Amiga CD32, Sega CD, 3DO, PlayStation, PlayStation Portable, FM Towns, Macintosh, Windows 95ReleaseSeptember 26, 1990September 26, 1990 (MS-DOS)March 1, 1992 (SNES)September 1992 (Amiga)[1]June 1, 1993 (Amiga CD32)March 1994 (Sega CD)August 1995 (Mac)[2]November 30, 1996 (Windows 95)Genre(s)Space flight simulationMode(s)Single-player""",
     """Wing CommanderDeveloper(s)Origin SystemsPublisher(s)Origin SystemsDirector(s)Chris RobertsProducer(s)Chris Roberts  Warren SpectorDesigner(s)Chris RobertsWriter(s)Jeff GeorgeComposer(s)George Alistair Sanger  David GovettPlatform(s)MS-DOSSuper NES, Amiga, Amiga CD32, Sega CD, 3DO, PlayStation, PlayStation Portable, FM Towns, Macintosh, Windows 95ReleaseSeptember 26, 1990September 26, 1990 (MS-DOS)March 1, 1992 (SNES)September 1992 (Amiga)June 1, 1993 (Amiga CD32)March 1994 (Sega CD)August 1995 (Mac)November 30, 1996 (Windows 95)Genre(s)Space flight simulationMode(s)Single-player"""),
    ("Zero4 ChampDeveloper(s)Media RingsPublisher(s)Media RingsDirector(s)Yutaka KaminagaPlatform(s)PC EngineReleaseJP: 1991Genre(s)Racing video gameMode(s)Single-player, multiplayer",
     "Zero4 ChampDeveloper(s)Media RingsPublisher(s)Media RingsDirector(s)Yutaka KaminagaPlatform(s)PC EngineReleaseJP: 1991Genre(s)Racing video gameMode(s)Single-player, multiplayer"),
    ("[2022] New data released", " New data released"),
    ("s$$$@[342]##a", "s$$$@##a")
])
def test_remove_square_brackets(input_string, expected_result):
    result = ItemDataProcessor.remove_square_brackets(input_string)
    
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
    result = ItemDataProcessor.replace_release_keyword_with_platform_name(input_string)
    
    assert result == expected_result
    
@pytest.mark.parametrize("input_string, expected_result", [
    ("World League SoccerNorth American cover artDeveloper(s)C-LabPublisher(s)JP: ImagineerNA: MindscapeComposer(s)Kazuo SawaPlatform(s)Super NES, Sharp X68000Super NESSuper NESJP: 20 September 1991NA: April 1992Sharp X68000JP: 29 November 1991Genre(s)SportsMode(s)Single-player, multiplayer",
     "World League SoccerNorth American cover artDeveloper(s)C-LabPublisher(s)JP: ImagineerNA: MindscapeComposer(s)Kazuo SawaPlatform(s)Super NES, Sharp X68000Super NESSuper NESJP: September 20, 1991NA: April 1992Sharp X68000JP: November 29, 1991Genre(s)SportsMode(s)Single-player, multiplayer"),
])    
def test_format_dates(input_string, expected_result):
    months = r"(January|February|March|April|May|June|July|August|September|October|November|December)"
    result = ItemDataProcessor.format_dates(input_string, months)
    
    assert result == expected_result
    
@pytest.mark.parametrize("input_string, expected_result", [
    ("Zero4 Champ RRCover artDeveloper(s)Media RingsPublisher(s)Media RingsDirector(s)Yasunori IsekiProgrammer(s)Ryoichi Sato  Hiroshi KatoComposer(s)Katsuhiro Hayashi  Jouji IijimaSeriesZero4 Champ seriesPlatform(s)Super FamicomSuper NESJP: July 22, 1994Genre(s)Arcade racingMode(s)Single-player, multiplayer",
     "Zero4 Champ RRCover artDeveloper(s)Media RingsPublisher(s)Media RingsDirector(s)Yasunori IsekiProgrammer(s)Ryoichi Sato  Hiroshi KatoComposer(s)Katsuhiro Hayashi  Jouji IijimaSeriesZero4 Champ seriesPlatform(s)Super FamicomSuper NESJP: July 22, 1994Genre(s)Arcade racingMode(s)Single-player, multiplayer"),
    ("Ys III: Wanderers from YsDeveloper(s)Nihon FalcomPublisher(s)Nihon FalcomComposer(s)Mieko IshikawaSeriesYsPlatform(s)PC-8801, PC-9801, MSX2, X68000, TurboGrafx-CD, Super NES, Famicom, Genesis, PlayStation 2Super NESPC-8801JP: July 21, 1989PC-9801JP: July 28, 1989MSX2JP: October 20, 1989X68000JP: March 24, 1990TurboGrafx-CDJP: March 22, 1991NA: November 1991Super NESJP: June 21, 1991NA: January 1992FamicomJP: September 27, 1991GenesisJP: November 1, 1991NA: 1991PlayStation 2JP: March 24, 2005Genre(s)Action role-playingMode(s)Single-player",
     "Ys III: Wanderers from YsDeveloper(s)Nihon FalcomPublisher(s)Nihon FalcomComposer(s)Mieko IshikawaSeriesYsPlatform(s)PC-8801, PC-9801, MSX2, X68000, TurboGrafx-CD, Super NES, Famicom, Genesis, PlayStation 2Super NESPC-8801JP: July 21, 1989PC-9801JP: July 28, 1989MSX2JP: October 20, 1989X68000JP: March 24, 1990TurboGrafx-CDJP: March 22, 1991NA: November 01, 1991Super NESJP: June 21, 1991NA: January 01, 1992FamicomJP: September 27, 1991GenesisJP: November 1, 1991NA: 1991PlayStation 2JP: March 24, 2005Genre(s)Action role-playingMode(s)Single-player")
])
def test_add_missing_day_to_months(input_string, expected_result):
    months = r"(January|February|March|April|May|June|July|August|September|October|November|December)"
    result = ItemDataProcessor.add_missing_day_to_months(input_string, months)
    
    assert result == expected_result
    
@pytest.mark.parametrize("input_string, expected_result", [
    ("Young MerlinDeveloper(s)Westwood StudiosPublisher(s)Virgin GamesComposer(s)Paul MudraFrank KlepackiDwight OkaharaPlatform(s)Super NESSuper NESNA: 1993EU: March 31, 1994Genre(s)Action-AdventureMode(s)Single-player",
     "Young MerlinDeveloper(s)Westwood StudiosPublisher(s)Virgin GamesComposer(s)Paul MudraFrank KlepackiDwight OkaharaPlatform(s)Super NESSuper NESNA: December 01, 1993EU: March 31, 1994Genre(s)Action-AdventureMode(s)Single-player")
])    
def test_add_missing_day_and_year_if_needed(input_string, expected_result):
    result = ItemDataProcessor.add_missing_day_and_year_if_needed(input_string)
    
    assert result == expected_result

@pytest.mark.parametrize("input_string, expected_result", [
    ("Zero the Kamikaze SquirrelCover art for the Genesis versionDeveloper(s)Iguana EntertainmentPublisher(s)SunsoftDirector(s)Neill GlancyTeam IguanaDesigner(s)Neill GlancyTeam ZeroComposer(s)Rick Fox (as Fox Productions)Platform(s)Sega GenesisSuper NESSuper NESGenesisNA: October 01, 1994UK: July 01, 1995Super NESNA: November 01, 1994Genre(s)PlatformMode(s)Single-player",
     "Zero the Kamikaze SquirrelCover art for the Genesis versionDeveloper(s)Iguana EntertainmentPublisher(s)SunsoftDirector(s)Neill GlancyTeam IguanaDesigner(s)Neill GlancyTeam ZeroComposer(s)Rick Fox (as Fox Productions)Platform(s)Sega GenesisSuper NESSuper NESGenesisNA: October 01, 1994UK: NA: July 01, 1995Super NESNA: November 01, 1994Genre(s)PlatformMode(s)Single-player")
])
def test_add_default_region_prefix(input_string, expected_result):
    months = r"(January|February|March|April|May|June|July|August|September|October|November|December)"    
    result = ItemDataProcessor.add_default_region_prefix(input_string, months)
    
    assert result == expected_result
    
@pytest.mark.parametrize("input_string, expected_result", [
    ("Yūyu no Quiz de Go! Go!Arcade flyerPublisher(s)TaitoComposer(s)Tamayo Kawamoto  Kiyohiro Sada  Masako InataPlatform(s)Arcade, Super FamicomSuper NESArcade: NA: December 01, 1990  Super Famicom: JP: July 10, 1992Genre(s)QuizMode(s)Single-player, multiplayer",
     "Yūyu no Quiz de Go! Go!Arcade flyerPublisher(s)TaitoComposer(s)Tamayo Kawamoto  Kiyohiro Sada  Masako InataPlatform(s)Arcade, SNESSNESArcade: NA: December 01, 1990SNES JP: July 10, 1992Genre(s)QuizMode(s)Single-player, multiplayer")
])    
def test_simplify_searched_console_names(input_string, expected_result):
    console_names = r"(Super NES|SNES|Super Nintendo|Super Famicom)"
    result = ItemDataProcessor.simplify_searched_console_names(input_string, console_names)
    
    assert result == expected_result