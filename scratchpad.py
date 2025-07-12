# def get_layout_manger(display: str):
#     snake_case = display.replace(" ", "_")
#     layout_manager_cls_name = ""
#     for i in range(len(snake_case) - 1): # stride through string with window size 2 stride 1
#         window = snake_case[i:i+2]
#         print("window", window)
#         if window[0] == "-":
#             layout_manager_cls_name += window[1].upper()
#             i +=1
#         else:
#             layout_manager_cls_name += window[0] if i < len(snake_case) - 1 else window[1]
#     print(layout_manager_cls_name)

def get_layout_manger(display: str):
    # layout_manager_cls_name = display.replace(" ", "_")
    layout_manager_cls_name = display
    for c in layout_manager_cls_name: # stride through string with window size 2 stride 1
        if f"-{c}" in layout_manager_cls_name:
            layout_manager_cls_name = layout_manager_cls_name.replace(f"-{c}", c.upper())
        if f" {c}" in layout_manager_cls_name:
            layout_manager_cls_name = layout_manager_cls_name.replace(f" {c}",f"_{c.upper()}")
    layout_manager_cls_name = layout_manager_cls_name[0].upper() + layout_manager_cls_name[1:]
    print(layout_manager_cls_name)

def get_display_name(layout_manager_cls_name: str):
    display = layout_manager_cls_name
    for i, c in enumerate(display):
        if f"_{c}" in display:
            display = display.replace(f"_{c}", f" {c.lower()}")
        if i > 0 and display[i-1].islower() and c.isupper():
            prev = display[i-1]
            display = display.replace(f"{prev}{c}", f"{prev}-{c.lower()}")
    display = display[0].lower() + display[1:]
    return display
        
    

# get_layout_manger("flex container")
# get_layout_manger("flex")
# get_layout_manger("inline-flex")
# get_layout_manger("block flow-root")

get_display_name("Flex_Container")
get_display_name("Flex")
get_display_name("InlineFlex")
get_display_name("Block_FlowRoot")
