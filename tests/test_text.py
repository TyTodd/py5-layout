from py5_layout import Py5Layout, Div, Style, Text
import py5

def test_text_1():
    layout = Py5Layout(style=Style(background_color=(255,255,255), width="100%", height="100%"), width=500, height=500)
    with layout:
        with Div(style=Style(background_color=(0, 0, 255), width="50%", height="50%")):
            Text("The quick brown fox jumps over the lazy dog")
            with Div(style=Style(background_color=(0,255,0))):
                Div(style=Style(background_color=(255,0,0)))