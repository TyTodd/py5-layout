# Py5 Layout

Py5 Layout is a library that extends Py5 with a python based markup language. Styles are mirrored from CSS. The library is compatible with your normal python workflow/libraries. You can use logic defined in python to control the layout and the styles. The library uses Yoga as its layout engine, the same engine used by React Native. Special thanks to [dzhsurf/poga](https://github.com/dzhsurf/poga) for the Yoga bindings.

Example:

```python
import py5
from py5_layout import Py5Layout, Div, Style
from math import sin, cos
from time import time
width_ = 500
height_ = 500
layout = None
def setup():
    global width_, height_, layout
    py5.size(width_, height_)
    layout = Py5Layout(style=Style(background_color=(255,255,255), width="100%", height="100%"), width=width_, height=height_)

count = 0
def draw():
    global count, last_print_time
    count += 1
    with layout:
        with Div(style=Style(background_color=(127*sin(count/10), 0, 127*cos(count/10)), width=count//2, height="50%")):
            with Div(style=Style(background_color=(0,255,0))):
                Div(style=Style(background_color=(255,0,0)))

py5.run_sketch()
```

This creates the following animated layout:

![animated layout](./examples/simple_example.gif)

## Installation

Install the library:

```bash
pip install py5-layout
```

Follow instructions to install Java 17 from py5's website [here](https://py5coding.org/content/install.html#install-java)

## Usage

In this library, the with statement is used to create a hierarchical layout context, where each nested with block defines a child node within its parent container.

```python
from py5_layout import *

layout = None
def setup():
    py5.size(500, 500)
    global layout
    layout = Py5Layout(style=Style(background_color=(255,255,255), width="100%", height="100%"), width=width_, height=height_)
def draw():
    with layout:
        with Div(style=Style(background_color="red", width="100%", height="100%")):
            with Div(style=Style(background_color="green")):
                Div(style=Style(background_color="blue"))
```

is equivalent to:

```html
<div style="background-color: red; width: 100%; height: 100%;">
  <div style="background-color: green;">
    <div style="background-color: blue;"></div>
  </div>
</div>
```

You can use python logic to control the layout and styles.

```python
from py5_layout import *
count = 0
layout = None
def setup():
    global layout
    layout = Py5Layout(style=Style(background_color=(255,255,255), width="100%", height="100%"), width=width_, height=height_)
def draw():
    global count
    count += 1
    show_green = count % 50 < 25
    with layout:
        with Div(style=Style(background_color="red", width=f"{count%100}%", height="100%")):
            if show_green:
                with Div(style=Style(background_color="green")):
                    Div(style=Style(background_color="blue"))
```

You can also embed custom animations and renderings into the layout. See the [custom sketch example](./examples/custom_sketch.py)

```python
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
```

this renders the following:
![custom sketch](./examples/custom_sketch.gif)

## Reference

- Div: A container element that can contain other elements.
- Text: A text element that can be used to display text.
- Style: A style object that can be used to style the layout.
- Py5Layout: The main layout object that can be used to create the layout.
- Element: The base class for all elements.

### Style Reference

Style closely follows React Native's style system. Since the py5-layout uses Yoga.

```python
GlobalType = Literal["inherit", "initial"]
AlignType = Literal["auto", "flex-start", "center", "flex-end", "stretch", "baseline", "space-between", "space-around"]
JustifyType = Literal["flex-start", "center", "flex-end", "space-between", "space-around", "space-evenly"]
PositionMarginType = str | float | Literal["auto"]
SizeType = float | str | Literal["auto"]
MaxSizeType = float | str | Literal["none"]
MinSizeType = float | str | Literal["auto"]
PaddingType = float | str
ColorType = str | Tuple | int | float

class Style():
    align_content: AlignType | GlobalType = field(default="auto", metadata=gen_metadata(inherited=False))
    align_items: AlignType | GlobalType = field(default="auto", metadata=gen_metadata(inherited=False))
    align_self: AlignType | GlobalType = field(default="auto", metadata=gen_metadata(inherited=False))
    all: Any = NotImplemented
    # Animation properties are not included and there is no current plan to include them
    background_attachment = NotImplemented
    background_blend_mode = NotImplemented
    background_clip = NotImplemented
    background_color: ColorType = field(default="transparent", metadata=gen_metadata(inherited=False))
    background_image: str = NotImplemented
    background_origin = NotImplemented
    background_position = NotImplemented
    background_repeat = NotImplemented
    background_size = NotImplemented
    border: str = NotImplemented
    border_bottom: str = NotImplemented
    border_bottom_color: str = NotImplemented
    border_bottom_left_radius: str = NotImplemented
    border_bottom_right_radius: str = NotImplemented
    border_bottom_style: str = NotImplemented
    border_bottom_width: str = NotImplemented
    border_collapse: str = NotImplemented
    border_color: str = NotImplemented
    border_image = NotImplemented
    border_image_outset = NotImplemented
    border_image_repeat = NotImplemented
    border_image_slice = NotImplemented
    border_image_source = NotImplemented
    border_image_width = NotImplemented
    border_left: str = NotImplemented
    border_left_color: str = NotImplemented
    border_left_style: str = NotImplemented
    border_left_width: str = NotImplemented
    border_radius: str = NotImplemented
    border_right_color: str = NotImplemented
    border_right: str = NotImplemented
    border_right_style: str = NotImplemented
    border_right_width: str = NotImplemented
    border_top_color: str = NotImplemented
    border_top: str = NotImplemented
    border_top_left_radius: str = NotImplemented
    border_top_right_radius: str = NotImplemented
    border_top_style: str = NotImplemented
    border_top_width: str = NotImplemented
    border_style: str = NotImplemented
    border_spacing: str = NotImplemented
    border_width: int | str | Tuple = NotImplemented
    bottom: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    box_shadow = NotImplemented
    box_sizing = NotImplemented
    color: ColorType = field(default=(0,0,0), metadata=gen_metadata(inherited=True))
    column_gap = NotImplemented
    direction: Literal["ltr", "rtl", "inherit", "initial"] = field(default="ltr", metadata=gen_metadata(inherited=True))
    display: Literal["flex", "none"] = field(default="flex", metadata=gen_metadata(inherited=False))
    filter = NotImplemented
    flex: int = field(default=0, metadata=gen_metadata(inherited=False))
    flex_basis: str = NotImplemented
    flex_direction: Literal["row", "row-reverse", "column", "column-reverse"] = field(default="column", metadata=gen_metadata(inherited=False))
    flex_grow: float = field(default=0, metadata=gen_metadata(inherited=False))
    flex_shrink: float = field(default=0, metadata=gen_metadata(inherited=False))
    flex_wrap: Literal["nowrap", "wrap", "wrap-reverse"] = field(default="nowrap", metadata=gen_metadata(inherited=False))
    font_family: str = field(default="Serif", metadata=gen_metadata(inherited=True))
    font_size: int | str = field(default=16, metadata=gen_metadata(inherited=True))
    font_style: str = field(default="normal", metadata=gen_metadata(inherited=True))
    font_variant = NotImplemented
    font_weight = NotImplemented
    height: SizeType = field(default="auto", metadata=gen_metadata(inherited=False))
    hyphens = NotImplemented
    isolation = NotImplemented
    justify_content: JustifyType | GlobalType = field(default="flex-start", metadata=gen_metadata(inherited=False))
    left: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    letter_spacing = NotImplemented
    line_height: float | str = field(default=1.2, metadata=gen_metadata(inherited=True))
    margin_bottom: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    margin_left: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    margin_right: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    margin_top: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    max_height: MaxSizeType = field(default="none", metadata=gen_metadata(inherited=False))
    max_width: MaxSizeType = field(default="none", metadata=gen_metadata(inherited=False))
    min_height: MinSizeType = field(default="auto", metadata=gen_metadata(inherited=False))
    min_width: MinSizeType = field(default="auto", metadata=gen_metadata(inherited=False))
    mix_blend_mode = NotImplemented
    object_fit = NotImplemented
    outline_color = NotImplemented
    outline_offset = NotImplemented
    outline_style = NotImplemented
    outline_width = NotImplemented
    overflow = NotImplemented
    padding_bottom: PaddingType = field(default=0, metadata=gen_metadata(inherited=False))
    padding_left: PaddingType = field(default=0, metadata=gen_metadata(inherited=False))
    padding_right: PaddingType = field(default=0, metadata=gen_metadata(inherited=False))
    padding_top: PaddingType = field(default=0, metadata=gen_metadata(inherited=False))
    pointer_events = NotImplemented
    position: Literal["static", "relative", "absolute"] = field(default="static", metadata=gen_metadata(inherited=False))
    resize = NotImplemented
    right: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    scroll_behavior = NotImplemented
    text_align: Literal["left", "center", "right"] = field(default="left", metadata=gen_metadata(inherited=True))
    text_decoration = NotImplemented
    text_decoration_color = NotImplemented
    text_decoration_line = NotImplemented
    text_decoration_style = NotImplemented
    text_transform = NotImplemented
    text_shadow_color = NotImplemented
    text_shadow_offset = NotImplemented
    text_shadow_radius = NotImplemented
    top: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    # Transform properties are not included and there is no current plan to include them
    unicode_bidi: str = NotImplemented
    user_select = NotImplemented
    vertical_align = NotImplemented
    visibility = NotImplemented
    width: SizeType = field(default="auto", metadata=gen_metadata(inherited=False))
    z_index: str = NotImplemented
```

**coming soon**

- Button
- Switch
- Slider
- Checkbox

Todo:

- [x] Style inheritance
- [x] Style Merging
- [x] Text element
- [x] color keyword arguments (black, white, red, green, blue, etc.)
- [ ] hover, focus, etc. pseudo-classes
- [ ] Button element
- [ ] rem, em, vw, vh, etc. units
- [ ] CSS Classes and ids
- [ ] CSS Files
- [ ] CSS Variables
- [ ] Style type checking

```

```
