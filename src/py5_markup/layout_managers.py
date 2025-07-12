from py5_markup.element import Element
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple

@dataclass
class Box:
    width: int | str
    height: int | str
    x: int | str
    y: int | str
    z_index: int
    background_color: Tuple | int | float | str
    color: Tuple | int | str
    
class LayoutManager(ABC):
    """
    A layout manager is a class that is used to layout the elements in the document.
    It is responsible for calculating the position and size of the elements in the document.
    
    Naming convention is the name of the display type in CSS with all spaces replaced with underscores all dashes replaced with camel case
    for example 
    - "flex container" would be Flex_Container
    - "inline-block" would be InlineBlock
    - "grid" would be Grid
    
    """
    default_width: int | str = NotImplemented
    default_height: int | str = NotImplemented
    default_max_width: int | str = NotImplemented
    default_max_height: int | str = NotImplemented
    default_min_width: int | str = NotImplemented
    default_min_height: int | str = NotImplemented
    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated")
    
    @staticmethod
    def get_layout_manager(display: str):
        layout_manager_cls_name = display
        for c in layout_manager_cls_name: # stride through string with window size 2 stride 1
            if f"-{c}" in layout_manager_cls_name:
                layout_manager_cls_name = layout_manager_cls_name.replace(f"-{c}", c.upper())
            if f" {c}" in layout_manager_cls_name:
                layout_manager_cls_name = layout_manager_cls_name.replace(f" {c}",f"_{c.upper()}")
        layout_manager_cls_name = layout_manager_cls_name[0].upper() + layout_manager_cls_name[1:]
        return globals()[layout_manager_cls_name]
        
    
    @staticmethod
    def get_display_name(cls):
        display = cls.__name__
        for i, c in enumerate(display):
            if f"_{c}" in display:
                display = display.replace(f"_{c}", f" {c.lower()}")
            if i > 0 and display[i-1].islower() and c.isupper():
                prev = display[i-1]
                display = display.replace(f"{prev}{c}", f"{prev}-{c.lower()}")
        display = display[0].lower() + display[1:]
        return display

    @staticmethod
    def get_content_box(cls, element: "Element"):
        return Box(width = 0, height = 0, x = 0, y = 0, z_index = 0, background_color=element.style.background_color, color = element.style.color)
        
                


class Block(LayoutManager):
    default_width = "100%"
    default_height = "auto"
    default_min_width = "0"
    default_max_width = "none"
    default_min_height = "0"
    default_max_height = "none"
    
    @staticmethod
    def get_content_box(cls, element: "Element"):
        cls.__super__()
        
        
    
    

class Inline(LayoutManager):
    default_width # based on content
    default_height # based on content
    default_min_width # based on content
    default_max_width # based on parent
    default_min_height # based on content
    default_max_height # based on parent
    
        