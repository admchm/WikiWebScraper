import pytest
from src.WikiHandler import WikiHandler

def test_forbidden_true():
    handler = WikiHandler()
    
    forbidden_urls = [
        "https://en.wikipedia.org/wiki/Category:Super_Nintendo_Entertainment_System_games",
        "https://en.wikipedia.org/wiki/Special:Random",
        "https://en.wikipedia.org/wiki/Wikipedia:About"
    ]
    
    for url in forbidden_urls:
        assert handler.forbidden(url) 
        
def test_forbidden_fales():
    handler = WikiHandler()
    
    forbidden_urls = [
        "https://en.wikipedia.org/wiki/Category:Super_Nintendo_Entertainment_System_games",
        "https://en.wikipedia.org/wiki/Special:Random",
        "https://en.wikipedia.org/wiki/Wikipedia:About"
    ]
    
    allowed_url = "https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_A_Link_to_the_Past"
    
    assert False == handler.forbidden(allowed_url)
        
def test_calculate_objects_count(capsys):
    handler = WikiHandler()
    handler.counter = 100
    
    handler.calculate_objects_count()
    captured = capsys.readouterr()
    expected_output = ("Count of games without any date: 100\n")
    
    assert captured.out == expected_output