"""
File: draw_line
Name: 黃勝弘
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow()
num = 1
a = 0
b = 0
spot = 0

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(create_spot)


def create_spot(mouse):
    global num, a, b, spot
    # num is not const is variable
    if num % 2 == 1:
        spot = GOval(SIZE, SIZE)
        window.add(spot, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        # the place mouse click is at the center of circle
        a = mouse.x
        b = mouse.y
        num += 1
    elif num % 2 == 0:
        window.remove(spot)
        line = GLine(a, b, mouse.x, mouse.y)
        num += 1
        window.add(line)


if __name__ == "__main__":
    main()
