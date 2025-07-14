import poga
from poga.libpoga_capi import *

# Create nodes
root = YGNodeNew()
node1 = YGNodeNew()
node2 = YGNodeNew()
node3 = YGNodeNew()

# Root: width/height = 100% (use undefined so it stretches to parent)
YGNodeStyleSetWidthPercent(root, 100)
YGNodeStyleSetHeightPercent(root, 100)

# node1: 100% width, 50% height
YGNodeStyleSetWidthPercent(node1, 100)
YGNodeStyleSetHeightPercent(node1, 50)

# node2: 100% width, 50% height
YGNodeStyleSetWidthPercent(node2, 100)
YGNodeStyleSetHeightPercent(node2, 50)

# node3 (child of node2): 50% width, 50% height
YGNodeStyleSetWidthPercent(node3, 50)
YGNodeStyleSetHeightPercent(node3, 50)

# Build hierarchy
YGNodeInsertChild(root, node1, 0)
YGNodeInsertChild(root, node2, 1)
YGNodeInsertChild(node2, node3, 0)

# Calculate layout with a fixed container size
YGNodeCalculateLayout(root, 500, 500, YGDirection.LTR)

# Print layout results
def print_layout(label, node):
    left = YGNodeLayoutGetLeft(node)
    top = YGNodeLayoutGetTop(node)
    width = YGNodeLayoutGetWidth(node)
    height = YGNodeLayoutGetHeight(node)
    print(f"{label}: left={left}, top={top}, width={width}, height={height}")

print_layout("root", root)
print_layout("node1", node1)
print_layout("node2", node2)
print_layout("node3", node3)

# Cleanup
YGNodeFreeRecursive(root)
