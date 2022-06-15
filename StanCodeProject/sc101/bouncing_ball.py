"""
File: bouncing_ball
Name: 黃勝弘
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

click_or_not = True # switch
n = 0
# count how many time does ball go out the window
window = GWindow(800, 500, title='bouncing_ball.py')

ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
ball.fill_color = 'black'


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball)
    onmouseclicked(go)


def go(self):
    global click_or_not, n
    if ball.x == START_X and click_or_not:
        # ball need to be at start point and True that mouse click will do things
        move()
    if ball.x >= window.width:
        n += 1
        window.clear()
        window.add(ball, x=START_X, y=START_Y)
    if n == 3:
        # if ball go out 3 times switch off
        click_or_not = False


def move():
    """
    Ball's movement
    """
    vy = 0
    # first vy = 0
    while True:
        ball.move(VX, vy)
        vy += GRAVITY
        pause(DELAY)
        if ball.y + SIZE > window.height:
            vy = -vy * REDUCE
            if ball.x >= window.width:
                break
                # when ball go out from window break::::ball don't move!!

            ######  TEST    ######
            #     click_or_not = False
            #     n += 1
            #     # count how many time does ball go out the window
            #     window.clear()
            #     print('2')
            #     break
                # vy = 0
                # window.add(ball, x=START_X, y=START_Y)
                # why + cannot work
                # if n == 3:
                #     break


if __name__ == "__main__":
    main()
