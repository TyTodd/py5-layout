from py5_markup.style import Style
from dataclasses import asdict
from typing import Literal, Optional, List
from py5_markup.parent_manager import ParentManager
from layout_managers import LayoutManager
    
class Element:
    _layout_type: Literal["block", "inline"] = "block"
    _parent_manager: ParentManager = ParentManager()
    def __init__(self, style: Optional[Style] = None, **kwargs):
        if style is None:
            style = Style()
        self.style = style
        self._parent_manager.register(self)
        self._content_box = None
        self._padding_box = None
        self._border_box = None
        self._margin_box = None
        
        
        
    def get_layout_manager(self):
        return LayoutManager.get_layout_manager(self.style.display)
        
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
    
    def place_children(self):
        pass
    
    def get_content_size(self):
        if self._content_box is not None:
            return {
                "width": self._content_box.width,
                "height": self._content_box.height,
            }
        content_width = 0
        content_height = 0
        for child in self.get_children():
            content_width = max(content_width, child.get_content_size()["width"])
            content_height = max(content_height, child.get_content_size()["height"])
        return {
            "width": content_width,
            "height": content_height
        }
        
    
    @property
    def content_box(self):
        if self._content_box is None:
            self._content_box = 
    
            
        
        
        