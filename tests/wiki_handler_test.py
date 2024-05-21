import pytest
from src.WikiHandler import WikiHandler
from models.Item import Item
from src.ReleaseRegion import ReleaseRegion

def test_forbidden_true():
    handler = WikiHandler()
    
    forbidden_urls = [
        "https://en.wikipedia.org/wiki/Category:Super_Nintendo_Entertainment_System_games",
        "https://en.wikipedia.org/wiki/Special:Random",
        "https://en.wikipedia.org/wiki/Wikipedia:About"
    ]
    
    for url in forbidden_urls:
        assert handler.forbidden(url) 
        
def test_forbidden_fails():
    handler = WikiHandler()
    
    allowed_url = "https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_A_Link_to_the_Past"
    
    assert False == handler.forbidden(allowed_url)
        
def test_calculate_objects_count(capsys):
    handler = WikiHandler()
    handler.counter = 100
    
    handler.calculate_objects_count()
    captured = capsys.readouterr()
    expected_output = ("Count of games without any date: 100\n")
    
    assert captured.out == expected_output
    
def test_sort_by():
    handler = WikiHandler()
    
    handler.SNES_games_list = [
        Item("The Addams Family", release_NA="December 01, 1992", release_PAL="———", release_JP="———", game_url="https://en.wikipedia.org/wiki/The_Addams_Family_(video_game)"),
        Item("Asterix & Obelix", release_NA="———", release_PAL="December 01, 1995", release_JP="———", game_url="https://en.wikipedia.org/wiki/Asterix_%26_Obelix_(video_game)"),
        Item("Bill Walsh College Football", release_NA="February 01, 1994", release_PAL="———", release_JP="———", game_url="https://en.wikipedia.org/wiki/Bill_Walsh_College_Football")
    ]
    
    handler.sort_by(ReleaseRegion.NA)
    assert [item.title for item in handler.SNES_games_list] == ["The Addams Family", "Bill Walsh College Football", "Asterix & Obelix"], "Sorting by NA release date failed"
    
    handler.sort_by(ReleaseRegion.PAL)
    assert [item.title for item in handler.SNES_games_list] == ["Asterix & Obelix", "The Addams Family", "Bill Walsh College Football"], "Sorting by PAL release date failed"
    
    handler.sort_by(ReleaseRegion.JP)
    assert [item.title for item in handler.SNES_games_list] == ["Asterix & Obelix", "The Addams Family", "Bill Walsh College Football"], "Sorting by JP release date failed"