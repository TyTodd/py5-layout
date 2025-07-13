from typing import List, Dict, TYPE_CHECKING
from dataclasses import dataclass
from py5_layout.style import Style

if TYPE_CHECKING:
    from py5_layout.element import Element

    
class ParentManager:
    def __init__(self):
        self.parent_map: Dict["Element", ("Element", int)] = {}
        self.context_stack: List["Element"] = []
        self.children_map: Dict["Element", List["Element"]] = {}
        
    
    def register(self, element: "Element"):
        if len(self.context_stack) > 0:
            parent = self.context_stack[-1]
            if parent not in self.children_map:
                self.children_map[parent] = []
            self.children_map[parent].append(element)
            
            self.parent_map[element] = (parent, len(self.children_map[parent])-1)
        
    
    def get_parent(self, element: "Element"):
        return self.parent_map.get(element, None)
    
    def get_children(self, element: "Element"):
        return self.children_map.get(element, [])
    
    def enter_context(self, element: "Element"):
        self.context_stack.append(element)
    
    def exit_context(self):
        self.context_stack.pop()
    