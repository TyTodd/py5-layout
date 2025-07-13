from py5_layout.element import Element
from py5_layout.layout_manager import LayoutManager
from py5_layout.style import Style
from py5_layout.parent_manager import ParentManager

class Py5Layout:
    def __init__(self, style: Style = Style(), width: int = 500, height: int = 500):
        self.layout_manager = LayoutManager(width, height)
        self.parent_manager = ParentManager()
        # TODO: add BorderManager, ShadowManager, ColorManager, and BackgroundManager
        self.id_counter = 0
        self.style = style
        self.elements = []
    
    def register(self, element: Element, root: bool = False):
        self.parent_manager.register(element)
        element._id = self.id_counter
        self.id_counter += 1
        self.layout_manager.register(element, root)
        self.elements.append(element)
    
    def __enter__(self):
        Element.set_py5_layout(self)
        self.root = Element(style=self.style, root=True)
        self.root.__enter__()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.draw()
        self.root.__exit__(exc_type, exc_value, traceback)
        self.id_counter = 0
        self.elements.clear()
        Element.set_py5_layout(None)
    
    def draw(self):
        self.layout_manager.draw()
        for element in self.elements:
            element.draw()
        