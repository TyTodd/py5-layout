from py5_markup.element import Element
from abc import ABC, abstractmethod
class Display(ABC):
    default_width: int | str = NotImplemented
    default_height: int | str = NotImplemented
    default_max_width: int | str = NotImplemented
    default_max_height: int | str = NotImplemented
    default_min_width: int | str = NotImplemented
    default_min_height: int | str = NotImplemented
    def __init__(self):
        pass

    def get_width(self, element: Element):
        pass

    def get_height(self, element: Element):
        pass
    
    def get_x(self, element: Element):
        pass
    
    def get_y(self, element: Element):
        pass


class Block(Display):
    default_width = "100%"
    default_height = "auto"
    default_min_width = "0"
    default_max_width = "none"
    default_min_height = "0"
    default_max_height = "none"
    
    def __init__(self):
        super().__init__()

    def get_max_width(self, element: "Element"):
        parent_width = element.parent.get_width()
        if element.style.max_width is None:
            return parent_width
        elif "px" in element.style.max_width:
            ele_max_width = int(element.style.max_width.replace("px", ""))
        elif "%" in element.style.max_width:
            percent = int(element.style.max_width.replace("%", ""))
            ele_max_width = min(parent_width * percent / 100, parent_width)
        else:
            raise NotImplementedError(f"Max width {element.style.max_width} is not supported")
        return min(ele_max_width, parent_width)
    def get_max_height(self, element: "Element"):
        parent_height = element.parent.get_height()
        ele_max_height = None
        if element.style.max_height is None:
            return None
        elif isinstance(element.style.max_height, int):
            ele_max_height = element.style.max_height
        elif "px" in element.style.max_height:
            ele_max_height = int(element.style.max_height.replace("px", ""))
        elif "%" in element.style.max_height:
            percent = int(element.style.max_height.replace("%", ""))
            ele_max_height = min(parent_height * percent / 100, parent_height)
        else:
            raise NotImplementedError(f"Max height {element.style.max_height} is not supported")
        return min(ele_max_height, parent_height)

    def get_min_width(self, element: "Element"):
        if isinstance(element.style.min_width, int):
            ele_min_width = element.style.min_width
        elif "px" in element.style.min_width:
            ele_min_width = int(element.style.min_width.replace("px", ""))
        elif "%" in element.style.min_width:
            percent = int(element.style.min_width.replace("%", ""))
            ele_min_width = element.parent.get_width() * percent / 100
        else:
            raise NotImplementedError(f"Min width {element.style.min_width} is not supported")
        return ele_min_width

    def get_min_height(self, element: "Element"):
        if isinstance(element.style.min_height, int):
            ele_min_height = element.style.min_height
        elif "px" in element.style.min_height:
            ele_min_height = int(element.style.min_height.replace("px", ""))
        elif "%" in element.style.min_height:
            percent = int(element.style.min_height.replace("%", ""))
            ele_min_height = element.parent.get_height() * percent / 100
        else:
            raise NotImplementedError(f"Min height {element.style.min_height} is not supported")
        return ele_min_height

    def get_default_width(self, element: "Element"):
        width = element.style.width
        if element.style.width is 'auto':
            width = "100%"
        if "px" in width:
            return int(width.replace("px", ""))
        elif "%" in width:
            percent = int(width.replace("%", ""))
            return int(element.parent.get_width() * percent / 100)
        else:
            raise NotImplementedError(f"Width {element.style.width} is not supported")
    
    def get_height(self, element: "Element"):
        if element.style.height is 'auto':
            return max([child.get_height() for child in element.get_children()])
        elif "px" in element.style.height:
            height = int(element.style.height.replace("px", ""))
        elif "%" in element.style.height:
            percent = int(element.style.height.replace("%", ""))
            return element.parent.get_height() * percent / 100
        else:
            raise NotImplementedError(f"Height {element.style.height} is not supported")
    
    def get_default_x(self, element: "Element"):
        if element.style.position == "absolute":
            return element.style.left
        elif element.style.position == "relative":
            return element.style.left
        else:
            return 0
    
    def get_default_y(self, element: "Element"):
        if element.style.position == "absolute":
            return element.style.top
        elif element.style.position == "relative":
            return element.style.top
        else:
            return 0
    