from typing import Tuple, TYPE_CHECKING, Any, Literal, Dict, Set
from dataclasses import dataclass
from poga.libpoga_capi import *
from py5_layout.style import Style

if TYPE_CHECKING:
    from py5_layout.element import Element


align_arg_to_poga: dict[str, YGAlign] = {
    "auto": YGAlign.Auto,
    "flex-start": YGAlign.FlexStart,
    "center": YGAlign.Center,
    "flex-end": YGAlign.FlexEnd,
    "stretch": YGAlign.Stretch,
}

direction_arg_to_poga: dict[str, YGDirection] = {
    "ltr": YGDirection.LTR,
    "rtl": YGDirection.RTL,
    "inherit": YGDirection.Inherit
}

display_arg_to_poga: dict[str, YGDisplay] = {
    "flex": YGDisplay.Flex,
    "none": YGDisplay.DisplayNone
}

edge_arg_to_poga: dict[str, YGEdge] = {
    "left": YGEdge.Left,
    "top": YGEdge.Top,
    "right": YGEdge.Right,
    "bottom": YGEdge.Bottom,
    "start": YGEdge.Start,
    "end": YGEdge.End,
    "horizontal": YGEdge.Horizontal,
    "vertical": YGEdge.Vertical,
    "all": YGEdge.All,
}

position_arg_to_poga: dict[str, YGPositionType] = {
    "static": YGPositionType.Static,
    "relative": YGPositionType.Relative,
    "absolute": YGPositionType.Absolute,
}
    
class LayoutManager:
    def __init__(self, width: int, height: int):
        self.last_hash = None
        self.current_hash = None
        self.id_node_map: Dict[int, YGNodeRef] = {}
        self.registered_ids: Set[int] = set()
        self.layout_width = width
        self.layout_height = height
    
    def register(self, element: "Element", root: bool = False):
        # TODO: use children of element to insert/swap in the correct position. Using parent it wrong.
        if root:
            self.root = element
        self.registered_ids.add(element._id)
        if element._id not in self.id_node_map:
            self.id_node_map[element._id] = YGNodeNew()
        if element.get_parent() is None:
            return
        parent, index = element.get_parent()
        parent_node = self.id_node_map[parent._id]
        element_node = self.id_node_map[element._id]
        
        if not YGNodeIsSame(YGNodeGetOwner(parent_node), parent_node):
            if index < YGNodeGetChildCount(parent_node):
                YGNodeSwapChild(parent_node, element_node, index)
            else:
                YGNodeInsertChild(parent_node, element_node, index)
        self.resolve(element)
    
    def draw(self):
        self.clean()
        direction = direction_arg_to_poga[self.root.style.direction]
        root_node = self.id_node_map[self.root._id]
        YGNodeCalculateLayout(root_node, self.layout_width, self.layout_height, direction)
        
    
    def clean(self):
        for id in self.id_node_map:
            if id not in self.registered_ids:
                print("freeing", id)
                YGNodeFree(self.id_node_map[id])
        self.registered_ids.clear()
    
    def resolve(self, element: "Element"):
        include = ["align_content", "align_items", "align_self", 
                   "direction", "display", "height", "left", 
                   "margin_bottom", "margin_left", "margin_right", 
                   "margin_top", "max_height", "max_width", 
                   "min_height", "min_width", "padding_bottom", 
                   "padding_left", "padding_right", "padding_top", 
                   "position", "right", "top", "width"]
        style = element.style
        node = self.id_node_map[element._id]
        for k, v in style.get_ordered_attributes(include=include):
            func = getattr(LayoutManager, k)
            func(node, v)
    
    def get_x(self, element: "Element"):
        return YGNodeLayoutGetLeft(self.id_node_map[element._id])
    
    def get_y(self, element: "Element"):
        return YGNodeLayoutGetTop(self.id_node_map[element._id])
    
    def get_width(self, element: "Element"):
        return YGNodeLayoutGetWidth(self.id_node_map[element._id])
    
    def get_height(self, element: "Element"):
        return YGNodeLayoutGetHeight(self.id_node_map[element._id])
    def get_padding(self, element: "Element", edge: Literal["left", "right", "top", "bottom"]):
        return YGNodeLayoutGetPadding(self.id_node_map[element._id], edge_arg_to_poga[edge])
    
    def get_margin(self, element: "Element", edge: Literal["left", "right", "top", "bottom"]):
        return YGNodeLayoutGetMargin(self.id_node_map[element._id], edge_arg_to_poga[edge])
    
    
    @staticmethod
    def align_content(node: YGNodeRef, value: str):
        YGNodeStyleSetAlignContent(node, align_arg_to_poga[value])
    
    @staticmethod
    def align_items(node: YGNodeRef, value: str):
        YGNodeStyleSetAlignItems(node, align_arg_to_poga[value])
    
    @staticmethod
    def align_self(node: YGNodeRef, value: str):
        YGNodeStyleSetAlignSelf(node, align_arg_to_poga[value])
    
    @staticmethod
    def direction(node: YGNodeRef, value: str):
        YGNodeStyleSetDirection(node, direction_arg_to_poga[value])
    
    @staticmethod
    def display(node: YGNodeRef, value: str):
        YGNodeStyleSetDisplay(node, display_arg_to_poga[value])
    
    @staticmethod
    def height(node: YGNodeRef, value: str | int):
        value_type, parsed_value = Style.parse_value(value)
        if parsed_value == "auto":
            YGNodeStyleSetHeightAuto(node)
        elif value_type == "percent":
            YGNodeStyleSetHeightPercent(node, parsed_value)
        elif value_type == "px" or value_type == "value":
            YGNodeStyleSetHeight(node, parsed_value)
        else:
            raise ValueError(f"Invalid value for height: {value}")
    
    @staticmethod
    def left(node: YGNodeRef, value: str | int):
        LayoutManager.position_handler(node, value, "left")
    
    @staticmethod
    def margin_bottom(node: YGNodeRef, value: str | int):
        LayoutManager.margin_handler(node, value, "bottom")
    
    @staticmethod
    def margin_left(node: YGNodeRef, value: str | int):
        LayoutManager.margin_handler(node, value, "left")
    
    @staticmethod
    def margin_right(node: YGNodeRef, value: str | int):
        LayoutManager.margin_handler(node, value, "right")
    
    @staticmethod
    def margin_top(node: YGNodeRef, value: str | int):
        LayoutManager.margin_handler(node, value, "top")
    
    @staticmethod
    def max_height(node: YGNodeRef, value: str | int):
        value_type, parsed_value = Style.parse_value(value)
        if value_type == "px" or value_type == "value":
            YGNodeStyleSetMaxHeight(node, parsed_value)
        elif value_type == "percent":
            YGNodeStyleSetMaxHeightPercent(node, parsed_value)
        elif value == "none": # CAVEAT: Allows none to be used as a value
            pass
        else:
            raise ValueError(f"Invalid value for max-height: {value}")
    
    @staticmethod
    def max_width(node: YGNodeRef, value: str | int):
        value_type, parsed_value = Style.parse_value(value)
        if value_type == "px" or value_type == "value":
            YGNodeStyleSetMaxWidth(node, parsed_value)
        elif value_type == "percent":
            YGNodeStyleSetMaxWidthPercent(node, parsed_value)
        elif value == "none": # CAVEAT: Allows none to be used as a value
            pass
        else:
            raise ValueError(f"Invalid value for max-height: {value}")
    
    @staticmethod
    def min_height(node: YGNodeRef, value: str | int):
        value_type, parsed_value = Style.parse_value(value)
        if value_type == "px" or value_type == "value":
            YGNodeStyleSetMinHeight(node, parsed_value)
        elif value_type == "percent":
            YGNodeStyleSetMinHeightPercent(node, parsed_value)
        elif value == "auto": # CAVEAT: Allows auto to be used as a value
            pass
        else:
            raise ValueError(f"Invalid value for min-height: {value}")
    
    @staticmethod
    def min_width(node: YGNodeRef, value: str | int):
        value_type, parsed_value = Style.parse_value(value)
        if value_type == "px" or value_type == "value":
            YGNodeStyleSetMinWidth(node, parsed_value)
        elif value_type == "percent":   
            YGNodeStyleSetMinWidthPercent(node, parsed_value)
        elif value == "auto": # CAVEAT: Allows auto to be used as a value
            pass
        else:
            raise ValueError(f"Invalid value for min-width: {value}")
    
    @staticmethod
    def padding_bottom(node: YGNodeRef, value: str | int):
        LayoutManager.padding_handler(node, value, "bottom")
    
    @staticmethod
    def padding_left(node: YGNodeRef, value: str | int):
        LayoutManager.padding_handler(node, value, "left")
    
    @staticmethod
    def padding_right(node: YGNodeRef, value: str | int):
        LayoutManager.padding_handler(node, value, "right")
    
    @staticmethod
    def padding_top(node: YGNodeRef, value: str | int):
        LayoutManager.padding_handler(node, value, "top")
    
    @staticmethod
    def position(node: YGNodeRef, value: str):
        YGNodeStyleSetPositionType(node, position_arg_to_poga[value])
    
    @staticmethod
    def right(node: YGNodeRef, value: str | int):
        LayoutManager.position_handler(node, value, "right")
    
    @staticmethod
    def top(node: YGNodeRef, value: str | int):
        LayoutManager.position_handler(node, value, "top")
    
    @staticmethod
    def width(node: YGNodeRef, value: str | int):
        value_type, parsed_value = Style.parse_value(value)
        if value_type == "px" or value_type == "value":
            YGNodeStyleSetWidth(node, parsed_value)
        elif value_type == "percent":
            YGNodeStyleSetWidthPercent(node, parsed_value)
        elif value == "auto":
            YGNodeStyleSetWidthAuto(node)
        else:
            raise ValueError(f"Invalid value for width: {value}")
        
    @staticmethod
    def position_handler(node: YGNodeRef, value: str | int, position: Literal["left", "right", "top", "bottom"]):
        value_type, parsed_value = Style.parse_value(value)
        if value_type == "px" or value_type == "value":
            YGNodeStyleSetPosition(node, edge_arg_to_poga[position], parsed_value)
        elif value_type == "percent":
            YGNodeStyleSetPositionPercent(node, edge_arg_to_poga[position], parsed_value)
        else:
            raise ValueError(f"Invalid value for {position}: {value}")
    
    @staticmethod
    def margin_handler(node: YGNodeRef, value: str | int, position: Literal["left", "right", "top", "bottom"]):
        value_type, parsed_value = Style.parse_value(value)
        if value_type == "px" or value_type == "value":
            YGNodeStyleSetMargin(node, edge_arg_to_poga[position], parsed_value)
        elif value_type == "percent":
            YGNodeStyleSetMarginPercent(node, edge_arg_to_poga[position], parsed_value)
        elif value == "auto":
            YGNodeStyleSetMarginAuto(node, edge_arg_to_poga[position])
        else:
            raise ValueError(f"Invalid value for {position}: {value}")
    
    @staticmethod
    def padding_handler(node: YGNodeRef, value: str | int, position: Literal["left", "right", "top", "bottom"]):
        value_type, parsed_value = Style.parse_value(value)
        if value_type == "px" or value_type == "value":
            YGNodeStyleSetPadding(node, edge_arg_to_poga[position], parsed_value)
        elif value_type == "percent":
            YGNodeStyleSetPaddingPercent(node, edge_arg_to_poga[position], parsed_value)
        else:
            raise ValueError(f"Invalid value for {position}: {value}")
    