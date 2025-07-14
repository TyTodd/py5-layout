from poga.libpoga_capi import *
import ctypes
# Create a leaf node    
node = YGNodeNew()
leaf = YGNodeNew()
YGNodeStyleSetWidth(leaf, 100)
YGNodeStyleSetHeight(leaf, 100)
YGNodeInsertChild(node, leaf, 0)

# Attempt to get a child at index 0
# print("child count of leaf", YGNodeGetChildCount(leaf))
# print("child count of node", YGNodeGetChildCount(node))
leaf_child = YGNodeGetChild(leaf, 0)
node_child = YGNodeGetChild(node, 0)

# print("Leaf node:", leaf)
# print("Child at index 0 of leaf node:", leaf_child)

# print("regular node", node)
# print("Child at index 0 of node", node_child)
# print("is same leaf is child of node", YGNodeIsSame(leaf, node_child))
# print("is same leaf is child of leaf", YGNodeIsSame(leaf, leaf_child))

def hash_node(node: YGNodeRef):
    return ctypes.cast(node, ctypes.c_void_p).value

print("hash of leaf", hash_node(leaf))