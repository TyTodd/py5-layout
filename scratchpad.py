from poga.libpoga_capi import (
    YGNodeNew,
    YGNodeStyleSetWidth,
    YGNodeStyleSetHeight,
    YGNodeStyleSetFlexGrow,
    YGNodeInsertChild,
    YGNodeCalculateLayout,
    YGNodeFreeRecursive,
    YGUndefined,
    YGDirection,
    YGFlexDirection,
    YGAlign,
    YGNodeStyleSetFlexDirection,
    YGNodeGetChildCount
)

# Create root and two children
root = YGNodeNew()
YGNodeStyleSetWidth(root, 400)
YGNodeStyleSetHeight(root, 200)
YGNodeStyleSetFlexDirection(root, YGFlexDirection.Row)

child1 = YGNodeNew()
child2 = YGNodeNew()
YGNodeStyleSetFlexGrow(child1, 1.0)
YGNodeStyleSetFlexGrow(child2, 2.0)

# Insert children under root
YGNodeInsertChild(root, child1, 0)
YGNodeInsertChild(root, child2, 1)

print("old YGNodeGetChildCount", YGNodeGetChildCount(root))
# Compute layout (undefined auto size parent)
YGNodeCalculateLayout(root, 500, 500, YGDirection.LTR)

print("new YGNodeGetChildCount", YGNodeGetChildCount(root))
# Read results
from poga.libpoga_capi import YGNodeLayoutGetLeft, YGNodeLayoutGetWidth
print("Child1 x =", YGNodeLayoutGetLeft(child1), "width =", YGNodeLayoutGetWidth(child1))
print("Child2 x =", YGNodeLayoutGetLeft(child2), "width =", YGNodeLayoutGetWidth(child2))

# Cleanup
YGNodeFreeRecursive(root)


def test_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


