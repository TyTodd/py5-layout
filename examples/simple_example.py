import py5
from py5_layout import Py5Layout, Div, Style, Text
from time import time
width_ = 500
height_ = 500
layout = None
last_print_time = 0
def setup():
    global width_, height_, layout
    py5.size(width_, height_)
    layout = Py5Layout(style=Style(background_color=(255,255,255), width="100%", height="100%"), width=width_, height=height_)
    last_print_time = time()

count = 0
def draw():
    global count, last_print_time
    count += 1
    with layout:
        with Div(style=Style(background_color="salmon", width="100%", height="100%", color=(255,0,255), justify_content="center", align_items="center", align_content="center", )):
                Text("The quick brown fox jumps over the lazy dog and sometimes he is a dog and sometimes he is a fox and then when he moves he reuns super fast because he is such as fast fox")
 
    if time() - last_print_time > 1:
        print(f"FPS: {py5.get_frame_rate():.2f}")
        last_print_time = time()

py5.run_sketch()