import py5
from typing import Callable, Tuple, Optional
from py5_markup.style import Style
from py5_markup.element import Element
class Button(Element):
    def __init__(
        self, 
        x: int, 
        y: int, 
        width: int, 
        height: int, 
        label: str, 
        on_click: Callable,
        **kwargs
        ):
        super().__init__(**kwargs)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.on_click = on_click
        self.draw()

    def draw(self):
        py5.fill(self.style.background_color)
        py5.rect(self.x, self.y, self.width, self.height)
        py5.fill