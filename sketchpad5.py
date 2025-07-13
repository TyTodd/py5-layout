import ast

code = """
with MyContext():
    "standalone"
    42
    x = "assigned"
    y: str = "also assigned"
    z += "augmented"
    f(x="kw in function")
    f("arg in function")
    def f():
        return "nested"
"""

tree = ast.parse(code)

# Helper: walk only top-level, non-nested statements
def find_standalone_constants(nodes):
    constants = []

    for node in nodes:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue

        for subnode in ast.walk(node):
            if isinstance(subnode, ast.Constant):
                current = subnode
                is_disqualified = False

                while current is not node:
                    parent = getattr(current, "_parent", None)
                    if parent is None:
                        break

                    # Disqualifying contexts
                    if isinstance(parent, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
                        is_disqualified = True
                        break
                    if isinstance(parent, ast.Call):
                        is_disqualified = True
                        break
                    if isinstance(parent, ast.keyword):  # keyword arg like x="..."
                        is_disqualified = True
                        break

                    current = parent

                if not is_disqualified:
                    constants.append(subnode.value)

    return constants

# Patch AST to track parent pointers
def attach_parents(node):
    for parent in ast.walk(node):
        for child in ast.iter_child_nodes(parent):
            child._parent = parent

attach_parents(tree)

constants_in_with = []
for node in ast.walk(tree):
    if isinstance(node, ast.With):
        constants_in_with.extend(find_standalone_constants(node.body))

print(constants_in_with)
