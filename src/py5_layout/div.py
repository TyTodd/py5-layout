from py5_layout.element import Element
import py5
class Div(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def draw(self):
        # print(f"drawing div {self._id}", self.x, self.y, self.width, self.height)
        self.draw_background()
        py5.rect(self.x, self.y, self.width, self.height)
        