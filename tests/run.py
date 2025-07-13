import py5
from py5_layout import Py5Layout, Div, Style
from poga.libpoga_capi import *
from math import sin, cos
from time import time
width_ = 500
height_ = 500
layout = None
last_print_time = 0
def setup():
    global width_, height_, layout
    py5.size(width_, height_)
    config = YGConfigNew()
    YGConfigSetPrintTreeFlag(config, True)
    layout = Py5Layout(style=Style(background_color=(255,255,255), width="100%", height="100%"), width=width_, height=height_)
    last_print_time = time()

count = 0
def draw():
    global count, last_print_time
    count += 1
    with layout:
        with Div(style=Style(background_color=(127*sin(count/10), 0, 127*cos(count/10)), width=count//2, height="50%")):
            with Div(style=Style(background_color=(0,255,0))):
                Div(style=Style(background_color=(255,0,0)))
 
    if time() - last_print_time > 1:
        print(f"FPS: {py5.get_frame_rate():.2f}")
        last_print_time = time()

py5.run_sketch()