from py5_markup.style import Style
from dataclasses import asdict
from typing import Literal, Optional, List
from py5_markup.parent_manager import ParentManager

class Element:
    _layout_type: Literal["block", "inline"] = "block"
    _parent_manager: ParentManager = ParentManager()
    def __init__(self, style: Optional[Style] = None, **kwargs):
        self._parent_manager.register(self)
    
    def __enter__(self):
        Element._parent_manager.enter_context(self)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        Element._parent_manager.exit_context()
    
    def get_parent(self):
        return Element._parent_manager.get_parent(self)
    
    def get_children(self):
        return Element._parent_manager.get_children(self)
    
    def __hash__(self):
        return id(self)

    def draw(self):
        pass

    def update(self):
        pass
    
    def get_width(self):
        pass      
    
    def get_height(self):
        pass
        
    
    def set_child_positions(self):
        pass
            
    def justify_content(self, type: Literal["start", "end", "center", "space-between", "space-around", "space-evenly"]):
        pass
        
    
    def set_flex_position(self):
        pass
    
    def set_relative_position(self):
        pass
    
    def set_absolute_position(self):
        pass
            
        
        
        