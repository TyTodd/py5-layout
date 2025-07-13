from py5_layout.style import Style
from dataclasses import asdict
from typing import Literal, Optional, List, TYPE_CHECKING
from py5_layout.parent_manager import ParentManager
from py5_layout.layout_manager import LayoutManager
from poga.libpoga_capi import YGNodeNew
from abc import ABC, abstractmethod
import py5

if TYPE_CHECKING:
    from py5_layout.py5_layout import Py5Layout
    
class Element(ABC):
    _py5_layout: "Py5Layout" = None
    _node_type: Literal["Default", "Text"] = "Default"
    def __init__(self, style: Optional[Style] = None, root: bool = False, **kwargs):
        if style is None:
            style = Style()
        self.style = style
        self._py5_layout.register(self, root)
        
    @staticmethod
    def set_py5_layout(py5_layout: "Py5Layout"):
        Element._py5_layout = py5_layout
        
    def __enter__(self):
        Element._py5_layout.parent_manager.enter_context(self)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        Element._py5_layout.parent_manager.exit_context()
    
    def get_parent(self):
        return Element._py5_layout.parent_manager.get_parent(self)
    
    def get_children(self):
        return Element._py5_layout.parent_manager.get_children(self)
    
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
        
    def draw(self):
        self.draw_background()
        py5.rect(self.x, self.y, self.width, self.height)
    
    def set_parent_manager(self, parent_manager: ParentManager):
        self._parent_manager = parent_manager
    def set_layout_manager(self, layout_manager: LayoutManager):
        self._layout_manager = layout_manager
    
    def draw_background(self):
        background_color = self.style.background_color
        value_type, value = self.style.parse_value(background_color)
        if value != "transparent":
            if value_type == "tuple":
                py5.fill(*value[1])
            else:
                py5.fill(value)
        else:
            py5.no_fill()
    
    @property
    def x(self):
        return self._py5_layout.layout_manager.get_x(self)
    
    @property
    def y(self):
        return self._py5_layout.layout_manager.get_y(self)
    
    @property
    def width(self):
        return self._py5_layout.layout_manager.get_width(self)
    
    @property
    def height(self):
        return self._py5_layout.layout_manager.get_height(self)
    
    def padding(self, edge: Literal["left", "right", "top", "bottom"]):
        return self._py5_layout.layout_manager.get_padding(self.node, edge)
            
    
    
            
class Text(Element):
    _node_type = "Text"
    def __init__(self, text: str, **kwargs):
        super().__init__(**kwargs)
        self.text = text