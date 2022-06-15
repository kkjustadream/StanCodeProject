"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    num_live = NUM_LIVES
    while True:
        # check for collisions
        graphics.check_for_collisions()
        vx = graphics.get_ball_x_velocity()
        vy = graphics.get_ball_y_velocity()
        pause(FRAME_RATE)
        graphics.ball.move(vx, vy)
        graphics.restart(num_live)



if __name__ == '__main__':
    main()
