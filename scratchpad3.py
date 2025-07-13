from poga.libpoga_capi import *
import ctypes
import sys


YGLoggerFunc = ctypes.CFUNCTYPE(          # ← correct signature
    ctypes.c_int,       # return int
    ctypes.c_void_p,    # YGConfigRef cfg
    ctypes.c_void_p,    # YGNodeRef  node
    ctypes.c_int,       # YGLogLevel level
    ctypes.c_char_p     # const char* msg
)

def py_logger(cfg, node, level, msg):
    # dump the C string
    sys.stdout.write(ctypes.string_at(msg).decode())
    return 0            # MUST return int (ignored by Yoga)

c_logger = YGLoggerFunc(py_logger) 

config = YGConfigNew()
YGConfigSetLogger(config, c_logger)
YGConfigSetPrintTreeFlag(config, enabled=True)
# Create root and two children
root = YGNodeNewWithConfig(config)
YGNodeStyleSetWidth(root, 400)
YGNodeStyleSetHeight(root, 200)
YGNodeStyleSetFlexDirection(root, YGFlexDirection.Row)

child1 = YGNodeNewWithConfig(config)
child2 = YGNodeNewWithConfig(config)
YGNodeStyleSetFlexGrow(child1, 1.0)
YGNodeStyleSetFlexGrow(child2, 2.0)


# Insert children under root
YGNodeInsertChild(root, child1, 0)
YGNodeInsertChild(root, child2, 1)
# YGNodeInsertChild(root, child2, 1)

# Compute layout (undefined auto size parent)
YGNodeCalculateLayout(root, 500, 500, YGDirection.LTR)

print("before",YGNodeGetChildCount(root))
YGNodeFree(child2)
print("after",YGNodeGetChildCount(root))
print("Child1 x =", YGNodeLayoutGetLeft(child1), "width =", YGNodeLayoutGetWidth(child1))
print("Child2 x =", YGNodeLayoutGetLeft(child2), "width =", YGNodeLayoutGetWidth(child2))

# YGNodeStyleSetWidth(root, 400)
# YGNodeSwapChild(root, child1, 0)
# YGNodeSwapChild(child1, child2, 0)

# print(YGNodeIsDirty(root))
# print(YGNodeIsDirty(child1))
# print(YGNodeIsDirty(child2))

# # Compute layout (undefined auto size parent)
# YGNodeCalculateLayout(root, 500, 500, YGDirection.LTR)

# print("Child1 x =", YGNodeLayoutGetLeft(child1), "width =", YGNodeLayoutGetWidth(child1))
# print("Child2 x =", YGNodeLayoutGetLeft(child2), "width =", YGNodeLayoutGetWidth(child2))


