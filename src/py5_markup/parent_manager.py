from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from py5_markup.element import Element

class ParentManager:
    def __init__(self):
        self.parent_map: Dict["Element", "Element"] = {}
        self.context_stack: List["Element"] = []
        self.children_map: Dict["Element", List["Element"]] = {}
    
    def register(self, element: "Element"):
        if len(self.context_stack) > 0:
            self.parent_map[element] = self.context_stack[-1]
            if self.context_stack[-1] not in self.children_map:
                self.children_map[self.context_stack[-1]] = []
            self.children_map[self.context_stack[-1]].append(element)
    
    def get_parent(self, element: "Element"):
        return self.parent_map.get(element, None)
    
    def get_children(self, element: "Element"):
        return self.children_map.get(element, [])
    
    def enter_context(self, element: "Element"):
        self.context_stack.append(element)
    
    def exit_context(self):
        self.context_stack.pop()
    