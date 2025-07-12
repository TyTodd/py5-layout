from layout_manager import LayoutManager

class FlexBox(LayoutManager):
    def __init__(self):
        super().__init__()

    def get_width(self, element: "Element"):
        if "px" in element.style.width:
            return int(element.style.width.replace("px", ""))
        elif "%" in element.style.width:
            percent = int(element.style.width.replace("%", ""))
            return element.parent.get_width() * percent / 100
    def get_height(self, element: "Element"):
        pass