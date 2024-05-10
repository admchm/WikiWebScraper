class TextRes:
    html_attrib = "html.parser"
    href = "href"
    wiki_endpoint = "/wiki/"
    wiki_game_details_table_name = "infobox ib-video-game hproduct"
    wiki_base_address = "https://en.wikipedia.org"
    empty_string = "———"
    
    
    @classmethod
    def get_html_attrib(cls):
        return cls.html_attrib
    
    @classmethod
    def get_href(cls):
        return cls.href
    
    @classmethod
    def get_wiki_endpoint(cls):
        return cls.wiki_endpoint
    
    @classmethod
    def get_wiki_game_details_table_name(cls):
        return cls.wiki_game_details_table_name
    
    @classmethod
    def get_wiki_base_adress(cls):
        return cls.wiki_base_address
    
    @classmethod
    def get_empty_string(cls):
        return cls.empty_string