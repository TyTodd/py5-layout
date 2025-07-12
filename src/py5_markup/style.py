from typing import Tuple, Optional, Literal
from dataclasses import dataclass, field, InitVar
import py5


def gen_metadata(inherited: bool = False, handler: Optional[str] = None, precedence: Optional[int] = None):
    return {"inherited": inherited, "handler": handler, "precedence": precedence}

@dataclass
class Style:
    display: Literal["block"] = field(default="block", metadata=gen_metadata(inherited=False))
    background_color: Tuple | int | float | str = field(default="transparent", metadata=gen_metadata(inherited=False))
    color: Tuple | int | str = field(default=0, metadata=gen_metadata(inherited=True))
    width: int | str = field(default="auto", metadata=gen_metadata(inherited=True, handler="layout_manager", precedence=3))
    height: int | str = field(default="auto", metadata=gen_metadata(inherited=True, handler="layout_manager", precedence=3))
    max_width: int | str = field(default="none", metadata=gen_metadata(inherited=True, handler="layout_manager", precedence=1))
    max_height: int | str = field(default="none", metadata=gen_metadata(inherited=True, handler="layout_manager", precedence=1))
    min_width: int | str = field(default="0", metadata=gen_metadata(inherited=True, handler="layout_manager", precedence=1))
    min_height: int | str = field(default="0", metadata=gen_metadata(inherited=True, handler="layout_manager", precedence=1))
    padding: int | str = field(default="0", metadata=gen_metadata(inherited=True, handler="layout_manager", precedence=1))
    margin: int | str = field(default="0", metadata=gen_metadata(inherited=True, handler="layout_manager", precedence=1))
    border: int | str = field(default="0", metadata=gen_metadata(inherited=True, handler="layout_manager", precedence=1))
    # border_radius: int | str = field(default="0", metadata=gen_metadata(inherited=True, handler="layout_manager", precedence=1))
    # border_color: Tuple | int | float | str = field(default="transparent", metadata={"inherited": True, "handler": "color", "precedence": 1})
    # border_width: int | str = field(default="0", metadata={"inherited": True, "handler": "layout_manager", "precedence": 1})
    # border_style: str = field(default="solid", metadata={"inherited": True, "handler": "layout_manager", "precedence": 1})
    # position: str = field(default="static", metadata={"inherited": True, "handler": "layout_manager", "precedence": 0})
    # left: int | str = field(default=0, metadata={"inherited": True, "handler": "layout_manager", "precedence": 0})
    # top: int | str = field(default=0, metadata={"inherited": True, "handler": "layout_manager", "precedence": 0})
    # right: int | str = field(default=0, metadata={"inherited": True, "handler": "layout_manager", "precedence": 0})
    # bottom: int | str = field(default=0, metadata={"inherited": True, "handler": "layout_manager", "precedence": 0})
    # z_index: int = field(default=0, metadata={"inherited": True, "handler": "layout_manager", "precedence": 0})
        

