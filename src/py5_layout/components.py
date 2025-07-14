from py5_layout.element import Element
import py5
from typing import Literal
class Div(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def draw(self):
        self.draw_background()
        py5.rect(self.x, self.y, self.width, self.height)
