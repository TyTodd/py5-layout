from poga.libpoga_capi import *

# Create root and two children
root = YGNodeNew()
# YGNodeStyleSetWidth(root, 500)
# YGNodeStyleSetHeight(root, 500)

child1 = YGNodeNew()
child2 = YGNodeNew()
child3 = YGNodeNew()
# YGNodeStyleSetHeight(child1, 100)
# YGNodeStyleSetHeight(child2, 100)

# Insert children under root
print("root", root)
print("child1", child1)
print("child2", child2)
YGNodeInsertChild(root, child1, 0)
YGNodeInsertChild(child1, child2, 0)
YGNodeInsertChild(child1, child3, 1)
# YGNodeInsertChild(child1, child2, 0)

print("child1 owner", YGNodeGetOwner(child1))
print("child1 parent", YGNodeGetParent(child1))
print("child2 owner", YGNodeGetOwner(child2))
print("child2 parent", YGNodeGetParent(child2))
print("child3 owner", YGNodeGetOwner(child3))
print("child3 parent", YGNodeGetParent(child3))

print("child2 owner is child1", YGNodeIsSame(YGNodeGetOwner(child2), child1))
print("child2 parent is child1", YGNodeIsSame(YGNodeGetParent(child2), child1))


print("root children", YGNodeGetChildCount(root))
print("child1 children", YGNodeGetChildCount(child1))
print("child2 children", YGNodeGetChildCount(child2))

print("old YGNodeGetChildCount", YGNodeGetChildCount(root))
# Compute layout (undefined auto size parent)
YGNodeCalculateLayout(root, 500, 500, YGDirection.LTR)

print("new YGNodeGetChildCount", YGNodeGetChildCount(root))
# Read results
from poga.libpoga_capi import YGNodeLayoutGetLeft, YGNodeLayoutGetWidth

print("root x =", YGNodeLayoutGetLeft(root), "width =", YGNodeLayoutGetWidth(root))
print("root y =", YGNodeLayoutGetTop(root), "height =", YGNodeLayoutGetHeight(root))

print("Child1 x =", YGNodeLayoutGetLeft(child1), "width =", YGNodeLayoutGetWidth(child1))
print("Child1 y =", YGNodeLayoutGetTop(child1), "height =", YGNodeLayoutGetHeight(child1))
print("Child2 x =", YGNodeLayoutGetLeft(child2), "width =", YGNodeLayoutGetWidth(child2))
print("Child2 y =", YGNodeLayoutGetTop(child2), "height =", YGNodeLayoutGetHeight(child2))



