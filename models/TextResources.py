from src.ImmutableAttributes import ImmutableAttributes

class TextRes(metaclass=ImmutableAttributes):
    HTML_ATTRIB: str = "html.parser"
    HREF: str  = "href"
    WIKI_ENDPOINT: str  = "/wiki/"
    WIKI_GAME_DETAILS_TABLE_NAME: str  = "infobox ib-video-game hproduct"
    WIKI_BASE_ADDRESS: str  = "https://en.wikipedia.org"
    EMPTY_STRING: str  = "———"
    
    @classmethod
    def get_html_attrib(cls):
        return cls.HTML_ATTRIB
    
    @classmethod
    def get_href(cls):
        return cls.HREF
    
    @classmethod
    def get_wiki_endpoint(cls):
        return cls.WIKI_ENDPOINT
    
    @classmethod
    def get_wiki_game_details_table_name(cls):
        return cls.WIKI_GAME_DETAILS_TABLE_NAME
    
    @classmethod
    def get_wiki_base_address(cls):
        return cls.WIKI_BASE_ADDRESS
    
    @classmethod
    def get_empty_string(cls):
        return cls.EMPTY_STRING