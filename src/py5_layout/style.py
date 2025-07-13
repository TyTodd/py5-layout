from typing import Tuple, Optional, Literal, Any, ClassVar, Iterable
from dataclasses import dataclass, field, InitVar, fields, MISSING
import py5
import time


def gen_metadata(inherited: bool = False, handler: Optional[str] = None, precedence: Optional[int] = None):
    return {"inherited": inherited, "handler": handler, "precedence": precedence}

GlobalType = Literal["inherit", "initial"]
AlignType = Literal["auto", "flex-start", "center", "flex-end", "stretch", "baseline", "space-between", "space-around"]
JustifyType = Literal["flex-start", "center", "flex-end", "space-between", "space-around", "space-evenly"]
PositionMarginType = str | float | Literal["auto"] # TODO: Add GlobalType
SizeType = float | str | Literal["auto"] # TODO: Add GlobalType
MaxSizeType = float | str | Literal["none"] # TODO: Add GlobalType
MinSizeType = float | str | Literal["auto"] # TODO: Add GlobalType
PaddingType = float | str # TODO: Add GlobalType

@dataclass(frozen=True)
class Style():
    align_content: AlignType | GlobalType = field(default="auto", metadata=gen_metadata(inherited=False))
    align_items: AlignType | GlobalType = field(default="auto", metadata=gen_metadata(inherited=False))
    align_self: AlignType | GlobalType = field(default="auto", metadata=gen_metadata(inherited=False))
    all: Any = NotImplemented
    # Animation properties are not included and there is no current plan to include them
    background_attachment = NotImplemented
    background_blend_mode = NotImplemented
    background_clip = NotImplemented
    background_color: Tuple | int | float | str = field(default="transparent", metadata=gen_metadata(inherited=False))
    background_image: str = NotImplemented
    background_origin = NotImplemented
    background_position = NotImplemented
    background_repeat = NotImplemented
    background_size = NotImplemented
    border = NotImplemented
    border_bottom = NotImplemented
    border_bottom_color = NotImplemented
    border_bottom_left_radius = NotImplemented
    border_bottom_right_radius = NotImplemented
    border_bottom_style = NotImplemented
    border_bottom_width = NotImplemented
    border_collapse = NotImplemented
    border_color = NotImplemented
    border_image = NotImplemented
    border_image_outset = NotImplemented
    border_image_repeat = NotImplemented
    border_image_slice = NotImplemented
    border_image_source = NotImplemented
    border_image_width = NotImplemented
    border_left = NotImplemented
    border_left_color = NotImplemented
    border_left_style = NotImplemented
    border_left_width = NotImplemented
    border_radius = NotImplemented
    border_right_color = NotImplemented
    border_right = NotImplemented
    border_right_style = NotImplemented
    border_right_width = NotImplemented
    border_top_color = NotImplemented
    border_top = NotImplemented
    border_top_left_radius = NotImplemented
    border_top_right_radius = NotImplemented
    border_top_style = NotImplemented
    border_top_width = NotImplemented
    border_style = NotImplemented
    border_spacing = NotImplemented
    border_width: int | str | Tuple = NotImplemented
    bottom: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    box_shadow = NotImplemented
    box_decoration_break = NotImplemented
    box_sizing = NotImplemented
    caption_side = NotImplemented
    caret_color = NotImplemented
    clear = NotImplemented
    clip = NotImplemented
    column_count = NotImplemented
    column_fill = NotImplemented
    column_gap = NotImplemented
    columns = NotImplemented
    column_rule_color = NotImplemented
    column_rule = NotImplemented
    column_rule_style = NotImplemented
    column_rule_width = NotImplemented
    column_span = NotImplemented
    column_width = NotImplemented
    content = NotImplemented
    cursor = NotImplemented
    counter_increment = NotImplemented
    counter_reset = NotImplemented
    direction: Literal["ltr", "rtl", "inherit", "initial"] = field(default="ltr", metadata=gen_metadata(inherited=True))
    display: Literal["flex", "none"] = field(default="flex", metadata=gen_metadata(inherited=False))
    empty_cells = NotImplemented
    filter = NotImplemented
    flex = NotImplemented
    flex_basis = NotImplemented
    flex_direction = NotImplemented
    flex_flow = NotImplemented
    flex_grow = NotImplemented
    flex_shrink = NotImplemented
    flex_wrap = NotImplemented
    font_family = NotImplemented
    font_kerning = NotImplemented
    font_size_adjust = NotImplemented
    font_size = NotImplemented
    font_stretch = NotImplemented
    font_style = NotImplemented
    font_variant = NotImplemented
    font_weight = NotImplemented
    grid = NotImplemented
    grid_area = NotImplemented
    grid_auto_columns = NotImplemented
    grid_auto_flow = NotImplemented
    grid_auto_rows = NotImplemented
    grid_column = NotImplemented
    grid_column_end = NotImplemented
    grid_column_gap = NotImplemented
    grid_column_start = NotImplemented
    grid_gap = NotImplemented
    grid_row = NotImplemented
    grid_row_end = NotImplemented
    grid_row_gap = NotImplemented
    grid_row_start = NotImplemented
    grid_template = NotImplemented
    grid_template_areas = NotImplemented
    grid_template_columns = NotImplemented
    grid_template_rows = NotImplemented
    hanging_punctuation = NotImplemented
    height: SizeType = field(default="auto", metadata=gen_metadata(inherited=False))
    hyphens = NotImplemented
    isolation = NotImplemented
    justify_content: JustifyType | GlobalType = field(default="flex-start", metadata=gen_metadata(inherited=False))
    left: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    letter_spacing = NotImplemented
    line_height = NotImplemented
    list_style = NotImplemented
    list_style_image = NotImplemented
    list_style_position = NotImplemented
    list_style_type = NotImplemented
    margin_bottom: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    margin_left: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    margin_right: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    margin_top: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    max_height: MaxSizeType = field(default="none", metadata=gen_metadata(inherited=False))
    max_width: MaxSizeType = field(default="none", metadata=gen_metadata(inherited=False))
    min_height: MinSizeType = field(default="auto", metadata=gen_metadata(inherited=False))
    min_width: MinSizeType = field(default="auto", metadata=gen_metadata(inherited=False))
    mix_blend_mode = NotImplemented
    mask_image = NotImplemented
    object_fit = NotImplemented
    object_position = NotImplemented
    order = NotImplemented
    outline_color = NotImplemented
    outline_offset = NotImplemented
    outline_style = NotImplemented
    outline_width = NotImplemented
    overflow_x = NotImplemented
    overflow_y = NotImplemented
    padding_bottom: PaddingType = field(default=0, metadata=gen_metadata(inherited=False))
    padding_left: PaddingType = field(default=0, metadata=gen_metadata(inherited=False))
    padding_right: PaddingType = field(default=0, metadata=gen_metadata(inherited=False))
    padding_top: PaddingType = field(default=0, metadata=gen_metadata(inherited=False))
    page_break_after = NotImplemented
    page_break_before = NotImplemented
    page_break_inside = NotImplemented
    perspective = NotImplemented
    perspective_origin = NotImplemented
    pointer_events = NotImplemented
    position: Literal["static", "relative", "absolute"] = field(default="static", metadata=gen_metadata(inherited=False))
    quotes = NotImplemented
    resize = NotImplemented
    right: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    scroll_behavior = NotImplemented
    cssText = NotImplemented
    length = NotImplemented
    parentRule = NotImplemented
    table_layout = NotImplemented
    tab_size = NotImplemented
    text_align = NotImplemented
    text_align_last = NotImplemented
    text_decoration = NotImplemented
    text_decoration_color = NotImplemented
    text_decoration_line = NotImplemented
    text_decoration_style = NotImplemented
    text_indent = NotImplemented
    text_justify = NotImplemented
    text_overflow = NotImplemented
    text_transform = NotImplemented
    text_shadow = NotImplemented
    top: PositionMarginType = field(default="auto", metadata=gen_metadata(inherited=False))
    # Transform properties are not included and there is no current plan to include them
    unicode_bidi = NotImplemented
    user_select = NotImplemented
    vertical_align = NotImplemented
    visibility = NotImplemented
    white_space = NotImplemented
    width: SizeType = field(default="auto", metadata=gen_metadata(inherited=False))
    word_break = NotImplemented
    word_spacing = NotImplemented
    word_wrap = NotImplemented
    will_change = NotImplemented
    writing_mode = NotImplemented
    z_index = NotImplemented
    
    def __init__(self, **kwargs):
        
        object.__setattr__(self,"_order", list(kwargs.keys()))

        # Initialize fields but don't handle defaults yet to save memory
        for k in kwargs:
            if k in self.__dataclass_fields__:
                object.__setattr__(self, k, kwargs[k])
            else:
                raise TypeError(f"'{k}' is not a valid parameter for Style")
            
        
    def __getattr__(self, name: str) -> Any:
        if name in self._order:
            return getattr(self, name)
        elif name in self.__fields__:
            return self.__fields__[name].default
        else:
            raise AttributeError(f"'Style' object does not support property: '{name}'")
    
    # def __setattr__(self, name: str, value: Any) -> None:
    #     print(f"Setting {name} to {value}")
    #     if name in self.__dataclass_fields__:
    #         super().__setattr__(name, value)
    #     else:
    #         raise AttributeError(f"'Style' object does not support property: '{name}'")
    
    def get_defined_fields(self) -> set[str]:
        """
        Returns a set of all fields that have been defined on the Style object. Either through initialization or through setting an attribute.
        """
        return {k for k, v in vars(self).items() if k[0] != "_"}
    
    def get_ordered_attributes(self, include: Optional[Iterable[str]] = None) -> list[str]:
        if include is not None:
            include = set(include)
            return [(k, getattr(self, k)) for k in self._order if k[0] != "_" and k in include]
        else:
            return [(k, getattr(self, k)) for k in self._order if k[0] != "_"]
    
    @staticmethod
    def parse_value(value: str | int) -> Tuple[Literal["literal", "%", "px", "tuple", "value"], str | int]:
        value_type: Literal["literal", "%", "px", "tuple", "value"]
        value: str | int
        if isinstance(value, tuple):
            value_type = "tuple"
            parsed_values = [Style.parse_value(v) for v in value]
            value = tuple(zip(*parsed_values))
        elif isinstance(value, str):
            if value.endswith("px"):
                value_type = "px"
                value = float(value[:-2])
            elif value.endswith("%"):
                value_type = "percent"
                value = float(value[:-1])
            elif value.endswith("em"):
                raise NotImplementedError(f"PTML does not support em units yet")
            elif value.endswith("rem"):
                raise NotImplementedError(f"PTML does not support rem units yet")
            else:
                value_type = "literal"
        elif isinstance(value, int) or isinstance(value, float):
            value_type = "value"
            value = value
        else:
            raise ValueError(f"Invalid value: {value}")
        return value_type, value

    def __or__(self, other: "Style") -> "Style":
        raise NotImplementedError(f"Merging not implemented yet")