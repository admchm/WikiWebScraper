from src.ImmutableAttributes import ImmutableAttributes

class ExampleClass(metaclass=ImmutableAttributes):
    HTML_ATTRIB = "example"
    mutable_attribute = "incorrect value"
    
import pytest

def test_immutable_attribute_modification():
    with pytest.raises(AttributeError) as exc_info:
        ExampleClass.HTML_ATTRIB = 'some new value'
        
    assert "Cannot modify immutable attribute HTML_ATTRIB" in str(exc_info.value)
    
def test_mutable_attribute_modification():
    original_value = ExampleClass.mutable_attribute
    
    try:
        ExampleClass.mutable_attribute = "correct value"
        assert ExampleClass.mutable_attribute == "correct value"
    finally:
        ExampleClass.mutable_attribute = original_value