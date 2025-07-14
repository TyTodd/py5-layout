from py5_layout.style import Style
from dataclasses import asdict
from typing import Literal, Optional, List, TYPE_CHECKING, Tuple
from py5_layout.parent_manager import ParentManager
from py5_layout.layout_manager import LayoutManager
from abc import ABC, abstractmethod
import py5
from poga.libpoga_capi import YGMeasureMode, YGSize
from contextlib import contextmanager

if TYPE_CHECKING:
    from py5_layout.py5_layout import Py5Layout
    
class Element(ABC):
    _py5_layout: "Py5Layout" = None
    _node_type: Literal["Default", "Text"] = "Default"
    def __init__(self, style: Optional[Style] = None, root: bool = False, name: Optional[str] = None, **kwargs):
        if style is None:
            style = Style()
        self.style = style
        self._py5_layout.register(self, root)
        self.line_height = None
        self.name = name
        self.x_ = None
        self.y_ = None
        self.width_ = None
        self.height_ = None
        
    @staticmethod
    def set_py5_layout(py5_layout: "Py5Layout"):
        Element._py5_layout = py5_layout
        
    def __enter__(self):
        Element._py5_layout.parent_manager.enter_context(self)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        Element._py5_layout.parent_manager.exit_context()
    
    def get_parent(self) -> Optional[Tuple["Element", int]]:
        return Element._py5_layout.parent_manager.get_parent(self)
    
    def get_children(self) -> List["Element"]:
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
        value_type, value = self.style.parse_value(background_color, color=True)
        if value != "transparent":
            if isinstance(value_type, tuple):
                py5.fill(*value)
            else:
                py5.fill(value)
        else:
            py5.no_fill()
    
    @contextmanager
    def canvas(self, set_origin: bool = True, clip: bool = True):
        py5.push_matrix()
        if set_origin:
            py5.translate(self.x, self.y)
        if clip:
            py5.clip(self.x, self.y, self.width, self.height)
        yield
        py5.no_clip()
        py5.pop_matrix()
    
    @property
    def x(self):
        if self.x_ is not None:
            return self.x_
        else:
            parent_result = self.get_parent()
            self.x_ = self._py5_layout.layout_manager.get_x(self) + parent_result[0].x if parent_result is not None else 0
            return self.x_
    
    @property
    def y(self):
        if self.y_ is not None:
            return self.y_
        else:
            parent_result = self.get_parent()
            self.y_ = self._py5_layout.layout_manager.get_y(self) + parent_result[0].y if parent_result is not None else 0
            return self.y_
    
    @property
    def width(self):
        if self.width_ is not None:
            return self.width_
        else:
            self.width_ = self._py5_layout.layout_manager.get_width(self)
            return self.width_
    
    @property
    def height(self):
        if self.height_ is not None:
            return self.height_
        else:
            self.height_ = self._py5_layout.layout_manager.get_height(self)
            return self.height_
    
    def padding(self, edge: Literal["left", "right", "top", "bottom"]):
        return self._py5_layout.layout_manager.get_padding(self.node, edge)
            
    
    
            
class Text(Element):
    _node_type = "Text"
    def __init__(self, text: str, debug: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.style = self.get_parent()[0].style
        self.font_size = None
        self.line_height = None
        self.debug = debug
    def draw(self):
        lines, max_width = self.wrap_lines(self.text, self.width)
        py5.text(self.text, self.x, self.y, self.width, self.height)
        
        if self.debug:
            py5.no_fill()
            py5.stroke(255,0,0)
            py5.rect(self.x, self.y, self.width, self.height)
        
    def measure_callback(
        self,
        width: float,
        width_mode: YGMeasureMode,
        height: float,
        height_mode: YGMeasureMode,
    ) -> YGSize:
        """
        Return a YGSize with the node’s desired (width, height)
        under the supplied constraints.
        """
        # 1. Determine max width the node is allowed to occupy
        if width_mode == YGMeasureMode.Undefined:
            max_w = float("inf")          # no constraint
        else:
            max_w = width                 # AtMost or Exactly give a numeric limit

        # 2. Wrap (or not) and measure
        lines, natural_w = self.wrap_lines(self.text, max_w)
        # line_h = py5.text_ascent() + py5.text_descent()
        # natural_h = len(lines) * line_h
        natural_h = (len(lines) - 1) * self.line_height + (py5.text_ascent() + py5.text_descent())

        # 3. Conform to width/height modes
        if width_mode == YGMeasureMode.Exactly:
            out_w = width                 # Yoga requires this exact width
        elif width_mode == YGMeasureMode.AtMost:
            out_w = min(natural_w, width)
        else:                             # Undefined
            out_w = natural_w

        if height_mode == YGMeasureMode.Exactly:
            out_h = height
        elif height_mode == YGMeasureMode.AtMost:
            out_h = min(natural_h, height)
        else:
            out_h = natural_h

        # 4. Pack into YGSize
        size = YGSize()
        size.width = out_w
        size.height = out_h
        return size
    
    def resolve(self):
        # Handle color
        value_type, value = self.style.parse_value(self.style.color, color=True)
        if isinstance(value_type, tuple):
            py5.fill(*value)
        else:
            py5.fill(value)
            
        # Handle text_align
        if self.style.text_align == "left":
            py5.text_align(py5.LEFT, py5.TOP)
        elif self.style.text_align == "center":
            py5.text_align(py5.CENTER, py5.TOP)
        elif self.style.text_align == "right":
            py5.text_align(py5.RIGHT, py5.TOP)
        else:
            raise ValueError(f"Invalid value for text_align: {self.style.text_align}")
        
        
        # Handle font_size
        value_type, value = self.style.parse_value(self.style.font_size)
        if value_type == "%":
            self.font_size = value * self.get_parent()[0].style.font_size
        elif value_type == "value":
            self.font_size = value
        else:
            raise ValueError(f"Invalid value for font_size: {value}")
        py5.text_size(self.font_size)
        
        # Handle font_family and font_style
        font_name = self.style.font_family
        font_style = self.style.font_style
        font_style = font_style.replace("italic", "Italic").replace("bold", "Bold")
        if font_style != "normal":
            font_obj = py5.create_font(f"{font_name}-{font_style}", self.font_size)
            py5.text_font(font_obj)
        else:
            font_obj = py5.create_font(font_name, self.font_size)
            py5.text_font(font_obj)
        
        # Handle line_height
        value_type, value = self.style.parse_value(self.style.line_height)
        if value_type == "%":
            self.line_height = value/100 * self.font_size
        elif value_type == "px":
            self.line_height = value
        elif value_type == "value":
            self.line_height = value * self.font_size
        else:
            raise ValueError(f"Invalid value for line_height: {value}")
        py5.text_leading(self.line_height)


    def wrap_lines(self, text: str, max_width: float):
        self.resolve()
        if max_width == float("inf"):                    
            width = py5.text_width(text)
            return [text], width

        words = text.split()
        if not words:
            return [""], 0.0

        lines, cur = [], words[0]
        for word in words[1:]:
            test = f"{cur} {word}"
            if py5.text_width(test) <= max_width:
                cur = test
            else:
                lines.append(cur)
                cur = word
        lines.append(cur)

        widest = max(py5.text_width(line) for line in lines)
        return lines, widest