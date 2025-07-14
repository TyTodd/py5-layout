import py5
from py5_layout import Py5Layout, Div, Style, Text, Element
from math import sin, cos
from time import time
width_ = 500
height_ = 500
layout = None
last_print_time = 0

class CustomSketch(Element):
    def __init__(self, circle_radius: int, circle_color: tuple, **kwargs):
        super().__init__(**kwargs)
        self.circle_radius = circle_radius
        self.circle_color = circle_color
    
    def draw(self):
        with self.canvas(set_origin=False, clip=True):
            py5.fill(*self.circle_color)
            py5.circle(py5.mouse_x, py5.mouse_y, self.circle_radius)
            
            
def setup():
    global width_, height_, layout
    py5.size(width_, height_)
    layout = Py5Layout(style=Style(background_color=(255,255,255), width="100%", height="100%"), width=width_, height=height_)

count = 0
def draw():
    py5.no_stroke()
    global count, last_print_time
    count += 1
    with layout:
        CustomSketch(circle_radius=100, 
                        circle_color=(255,0,0), 
                        style=Style(background_color=(255,255,255),flex=1), width=width_, height=height_)
        with Div(style=Style(background_color="cyan", width="100%", height="50%", justify_content="center", align_items="center", align_content="center", font_size=40), name="div2"):
            Text("Woah look at that circle go!!!!")
py5.run_sketch()