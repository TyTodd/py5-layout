from typing import Tuple, Optional, Literal, Any, ClassVar, Iterable, List
from dataclasses import dataclass, field, InitVar, fields, MISSING, asdict
import py5
import time
import webcolors


def gen_metadata(inherited: bool = False, ignore: List[str] = []):
    return {"inherited": inherited, "ignore": ignore}

GlobalType = Literal["inherit", "initial"]
AlignType = Literal["auto", "flex-start", "center", "flex-end", "stretch", "baseline", "space-between", "space-around"]
JustifyType = Literal["flex-start", "center", "flex-end", "space-between", "space-around", "space-evenly"]
PositionMarginType = str | float | Literal["auto"] # TODO: Add GlobalType
SizeType = float | str | Literal["auto"] # TODO: Add GlobalType
MaxSizeType = float | str | Literal["none"] # TODO: Add GlobalType
MinSizeType = float | str | Literal["auto"] # TODO: Add GlobalType
PaddingType = float | str # TODO: Add GlobalType
ColorType = str | Tuple | int | float

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
    
    def __init__(self, **kwargs):
        
        object.__setattr__(self,"_order", list(kwargs.keys()))

        # Initialize fields but don't handle defaults yet to save memory
        for k in kwargs:
            if k in self.__dataclass_fields__ and self.__dataclass_fields__[k].default != NotImplemented:
                object.__setattr__(self, k, kwargs[k])
            elif k in self.__dataclass_fields__:
                raise NotImplementedError(f"Style property '{k}' is not implemented yet. But we're working on it! Wanna help? 👀 \n👉 https://github.com/TyTodd/py5-layout#")
            else:
                raise TypeError(f"'{k}' is not a valid parameter for Style. Should it be? Make a PR! \n👉 https://github.com/TyTodd/py5-layout#")
            
        
    def __getattr__(self, name: str) -> Any:
        if name in self._order:
            return getattr(self, name)
        elif name in self.__fields__ and self.__fields__[name].default != NotImplemented:
            return self.__fields__[name].default
        elif name in self.__fields__:
            raise NotImplementedError(f"Style property '{name}' is not implemented yet. But we're working on it! Wanna help? 👀 \n👉 https://github.com/TyTodd/py5-layout#")
        else:
            raise AttributeError(f"'Style' object does not support property: '{name}'")
    
    
    def get_defined_fields(self) -> set[str]:
        """
        Returns a set of all fields that have been defined on the Style object. Either through initialization or through setting an attribute.
        """
        return {k for k, v in vars(self).items() if k[0] != "_"}
    
    def get_ordered_attributes(self, include: Optional[Iterable[str]] = None) -> list[str]: # TODO add ignore defaults param instead of always ignoring defaults
        if include is not None:
            include = set(include)
            return [(k, getattr(self, k)) for k in self._order if k[0] != "_" and k in include]
        else:
            return [(k, getattr(self, k)) for k in self._order if k[0] != "_"]
    
    @staticmethod
    def parse_value(value: str | int | tuple | float, color = False) -> Tuple[Tuple | Literal["literal", "%", "px", "value", "color"], str | int]:
        value_type: Literal["literal", "%", "px", "value", "color"]
        value: str | int
        if isinstance(value, tuple):
            parsed_values = [Style.parse_value(v) for v in value]
            value_type, value = tuple(zip(*parsed_values))
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
            elif value.startswith("#"):
                value_type = "color"
                value = py5.color(value)
            elif color:
                value_type = ("value", "value", "value")
                value = tuple(webcolors.name_to_rgb(value))
            else:
                value_type = "literal"
        elif isinstance(value, int) or isinstance(value, float):
            value_type = "value"
            value = value
        else:
            raise ValueError(f"Invalid value: {value}")
        return value_type, value

    def __or__(self, other: "Style") -> "Style":
        return self.merge(other)
    
    def merge(self, other: "Style") -> "Style":
        new_dict = {**self.to_dict(), **other.to_dict()}
        return Style(**new_dict)

    def inherit_from(self, other: Optional["Style"]) -> "Style":
        """
        Inherits the values of the other style object. Resolves global key words 'inherit' and 'unset'. 
        For fields marked as 'inherited' = True, overrides the value of parent if undefined.
        Params:
            other: Optional[Style] 
                The style to inherit from. If set to None, all args marked inherit will be set to the default value.
        Returns:
            Style: A new style object with the values inherited.
        """
        self_defined = vars(self)
        new_dict = {}
        for field in fields(self):
            if field.default == NotImplemented:
                continue
            # if key word is unset, act as if the value is not set
            field_is_defined = field.name in self_defined and getattr(self, field.name) != "unset"
            # Don't inherit if the value is explicitly set
            if field_is_defined and getattr(self, field.name) != "inherit":
                new_dict[field.name] = getattr(self, field.name)
            # Inherit if inherit keyword is used 
            elif field_is_defined and getattr(self, field.name) == "inherit" and other is not None: # CAVEAT: if other is None, the value will be set to the default value. We can effectively do this by not setting the value at all and save memory.
                new_dict[field.name] = getattr(other, field.name)
            # Inheritance by default
            elif not field_is_defined and field.metadata["inherited"] and other is not None: 
                new_dict[field.name] = getattr(other, field.name) # will return the default value if not set:
        return Style(**new_dict)
    def resolve_globals(self, other: Optional["Style"] = None) -> "Style": # TODO: add custom globals too like --color-primary
        """
        Resolves the global values initial, inherit, and unset.
        Params:
            other: Optional[Style] = None
                The style to inherit from. If not provided, all inherit values will be set to the default value.
        Returns:
            Style: A new style object with the globals resolved.
        """
        # inherited = self.inherit_from(other)
        # for field, value in vars(inherited).items():
        #     if value == ""
        raise NotImplementedError("Not implemented yet")
        
    def to_dict(self) -> dict[str, Any]:
        return {k: getattr(self, k) for k in self._order if k[0] != "_"}

    def __repr__(self) -> str:
        return f"Style({', '.join([f'{k}={getattr(self, k)}' for k in self._order if k[0] != '_'])})"
    
    def __str__(self) -> str:
        return str(self.to_dict())