import py5

def setup():
    py5.size(500, 500)
    font_list = py5.Py5Font.list()
    print(font_list)

def draw():
    py5.background(255)
    txt = "This is a long string of text that will automatically wrap within the rectangle."
    txt = "Just some text"
    # py5.text_align(py5.LEFT, py5.TOP)
    # Draw text box
    font_name = "Zapfino"
    font_obj = py5.create_font(font_name, 32)
    
    spacing = 10
    py5.text_leading(spacing)
    py5.text_font(font_obj)
    py5.text_size(16)
    py5.fill(0)
    py5.text_align(py5.CENTER, py5.CENTER)
    # py5.text(txt, 50, 50, 200, 100)
    py5.text(txt, 50, 50)
    
    height = (py5.text_ascent() + py5.text_descent())/2 + spacing
    py5.stroke(255,0,0)
    py5.line(50, 50, 80, 50)
    py5.line(50, 50+height, 80, 50+height)
    


def mouse_pressed():
    print("mouse pressed", py5.mouse_x, py5.mouse_y)

py5.run_sketch()