from py5_layout.style import Style
from py5_layout.div import Div
from py5_layout.py5_layout import Py5Layout
from dataclasses import asdict
import pytest

def test_merge():
    style1 = Style(background_color=(255,0,0), width="100%")
    style2 = Style(background_color=(0,255,0), height="50%")
    merged = style1.merge(style2)
    assert merged.background_color == (0,255,0)
    assert merged.to_dict() == {"background_color": (0,255,0), "width": "100%", "height": "50%"}
    assert style1 | style2 == merged

def test_inherit_from():
    style1 = Style(background_color=(255,0,0), width="100%", align_content="center", color=(0,0,255))
    style2 = Style(background_color=(0,255,0), width="inherit", align_content="stretch", color=(0,255,0))
    style3 = Style(background_color=(0,255,0), width="50%", align_content="inherit")
    style4 = Style(background_color=(0,255,0), width="inherit", align_content="inherit", color="unset")
    style5 = Style(background_color=(0,255,0), width="inherit", align_content="unset", color="unset")
    
    inherited21 = style2.inherit_from(style1)
    inherited31 = style3.inherit_from(style1)
    inherited321 = style3.inherit_from(inherited21)
    inherited431 = style4.inherit_from(inherited31)
    inherited51 = style5.inherit_from(style1)
    
    assert inherited21.background_color == (0,255,0)
    assert inherited21.width == "100%"
    assert inherited21.align_content == "stretch"
    assert inherited21.color == (0,255,0)
    
    assert inherited31.color == (0,0,255)
    assert inherited31.width == "50%"
    
    assert inherited321.background_color == (0,255,0)
    assert inherited321.width == "50%"
    assert inherited321.align_content == "stretch"
    assert inherited321.color == (0,255,0)
    
    assert inherited431.color == (0,0,255)
    
    assert inherited51.color == (0,0,255)
    assert "align_content" not in inherited51.to_dict()
    
    

def test_not_implemented():
    with pytest.raises(NotImplementedError): # NotImplemented default and type set in Style (in progress)
        style = Style(background_color=(255,0,0), unicode_bidi="embed")
    with pytest.raises(TypeError): # NotImplemented default in Style but no type set (style prop not yet triaged)
        style = Style(background_color=(255,0,0), hyphens="embed")
    with pytest.raises(TypeError): # misspelled parameter 
        style = Style(background_colors=(255,0,0))
    
def test_incorrect_value(): #TODO: make it so the error is raised when the style is created, not when it's used
    style = Style(background_color=(255,0,0), width="full")
    with pytest.raises(ValueError):
        with Py5Layout():
            Div(style=style)