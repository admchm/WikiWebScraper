
#Metaclass for overriding __setattr__ not for instance but for class
class ImmutableAttributes(type): 
    __immutable_attributes__ = ('HTML_ATTRIB', 'HREF', 'WIKI_ENDPOINT', 'WIKI_GAME_DETAILS_TABLE_NAME', 'WIKI_BASE_ADDRESS', 'EMPTY_STRING')
        
    def __setattr__(self, name, value):
        if name in self.__immutable_attributes__:
            raise AttributeError(f"Cannot modify immutable attribute {name}")
        super().__setattr__(name, value)