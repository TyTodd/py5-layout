from typing import Tuple
from dataclasses import dataclass, field, InitVar
import py5
@dataclass
class Style:
    background_color: InitVar[Tuple | int | float | str] = 255
    color: InitVar[Tuple | int | str] = 0
    _background_color: Tuple | int | str = field(init=False)
    _color: Tuple | int | str = field(init=False)

    def __post_init__(self, background_color, color):
        self._background_color = background_color
        self._color = color
    
    @property
    def background_color(self) -> int:
        return args_to_color(self._background_color)
    
    @property
    def color(self) -> int:
        return args_to_color(self._color)
    
def args_to_color(args: Tuple | int | float | str) -> int:
    if isinstance(args, tuple):
        c = py5.color(*args)
    else:
        c = py5.color(args)
    return c
        

