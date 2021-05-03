def get_square(x_mouse,y_mouse,background_size_x,background_size_y):
    x_mouse=x_mouse*(1600/background_size_x)
    y_mouse=y_mouse*(900/background_size_y)
    if x_mouse>=400 and x_mouse<=1445 and y_mouse>=120 and y_mouse<=820:
        x_square=(400+int((x_mouse-400)/116)*116+58)*background_size_x/1600
        y_square=(120+int((y_mouse-120)/140)*140+70)*background_size_y/900

        return x_square,y_square
    else:
        return -999,-999