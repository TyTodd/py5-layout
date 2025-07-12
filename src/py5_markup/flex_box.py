from py5_markup.layout_manager import LayoutManager

class FlexBox(LayoutManager):
    def __init__(self):
        super().__init__()

    def get_max_width(self, element: "Element"):
        parent_width = element.parent.get_width()
        if element.style.max_width is None:
            return parent_width
        elif "px" in element.style.max_width:
            return min(int(element.style.max_width.replace("px", "")), parent_width)
        elif "%" in element.style.max_width:
            percent = int(element.style.max_width.replace("%", ""))
            return min(parent_width * percent / 100, parent_width)
        else:
            raise NotImplementedError(f"Max width {element.style.max_width} is not supported")

    def get_max_height(self, element: "Element"):
        pass

    def get_min_width(self, element: "Element"):
        pass

    def get_min_height(self, element: "Element"):
        pass

    def get_width(self, element: "Element"):
        width = element.style.width
        if element.style.width is 'auto':
            width = "100%"
        if "px" in width:
            return int(element.style.width.replace("px", ""))
        elif "%" in width:
            percent = int(element.style.width.replace("%", ""))
            return element.parent.get_width() * percent / 100
        else:
            
    def get_height(self, element: "Element"):
        pass