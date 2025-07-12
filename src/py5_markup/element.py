from style import Style
from dataclasses import asdict
from typing import Literal, Optional, List
class Element:
    layout_type: Literal["block", "inline"] = "block"
    def __init__(self, style: Optional[Style] = None, _parent: Optional["Element"] = None, _children: List["Element"] = [], **kwargs):
        # self._parent = _parent
        # self._children = _children
        # if _parent is not None:
        #     self.style = Style(**{**asdict(self._parent.style), **asdict(style)})
        # else:
        #     self.style = style or Style()
        
        # self.draw()
        pass
    
    def post_register(self):
        if self._parent is not None:
            self.style = Style(**{**asdict(self._parent.style), **asdict(self.style)})
        else:
            self.style = self.style or Style()
        self.draw()
        
    
    def register(self):
        pass

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
            
        
        
        