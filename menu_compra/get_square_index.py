from constants import SCREEN_WIDTH,SCREEN_HEIGHT

def get_square_index(x_mouse,y_mouse):
    x_mouse=x_mouse*(1600/SCREEN_WIDTH)
    y_mouse=y_mouse*(900/SCREEN_HEIGHT)
    if x_mouse>=400 and x_mouse<=1445 and y_mouse>=120 and y_mouse<=820:
        x_index=int((x_mouse-400)/116)
        y_index=int((y_mouse-120)/140)

        return x_index,y_index
    else:
        return -999,-999