import pytest
from models.TextResources import TextRes

def test_static_methods():
    assert TextRes.get_html_attrib() == "html.parser"
    assert TextRes.get_href() == "href"
    assert TextRes.get_wiki_endpoint() == "/wiki/"
    assert TextRes.get_wiki_game_details_table_name() == "infobox ib-video-game hproduct"
    assert TextRes.get_wiki_base_address() == "https://en.wikipedia.org"
    assert TextRes.get_empty_string() == "———"

def test_resources_immutable():
    with pytest.raises(AttributeError):
        TextRes.HTML_ATTRIB = "A new message"