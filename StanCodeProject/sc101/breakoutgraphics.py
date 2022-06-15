"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # instance variable private
        self.__dx = 0
        self.__dy = 0

        self.switch = False     # a switch that control restarting game
        self.end = False        # a switch that turn on when live=0
        self.win = False        # a switch that turn on when brick=0

        self.x = 0  # count how many times player die
        self.score = 0  # score count
        self.brick_row = brick_rows
        self.brick_col = brick_cols

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        if not self.win:
            self.paddle = GRect(paddle_width, paddle_height, y=window_height-paddle_offset, x=(window_width-paddle_width)/2)
            self.paddle_offset = paddle_offset
            self.paddle.filled = True
            self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        if not self.win:
            self.ball = GOval(ball_radius*2, ball_radius*2)
            self.ball.filled = True
            self.window.add(self.ball, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
            self.ball_initial_position_x = window_width/2-ball_radius
            self.ball_initial_position_y = window_height/2-ball_radius
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmouseclicked(self.ball_move)
        onmousemoved(self.paddle_move)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick1 = GRect(brick_width, brick_height, x=(brick_width+brick_spacing)*j
                               , y=brick_offset+(brick_height+brick_spacing)*i)
                brick1.filled = True
                if i == 0:
                    brick1.fill_color = 'red'
                if i == 1:
                    brick1.fill_color = 'red'
                if i == 2:
                    brick1.fill_color = 'orange'
                if i == 3:
                    brick1.fill_color = 'orange'
                if i == 4:
                    brick1.fill_color = 'yellow'
                if i == 5:
                    brick1.fill_color = 'yellow'
                if i == 6:
                    brick1.fill_color = 'green'
                if i == 7:
                    brick1.fill_color = 'green'
                if i == 8:
                    brick1.fill_color = 'blue'
                if i == 9:
                    brick1.fill_color = 'blue'
                self.brick = brick1
                self.window.add(brick1)

    # control paddle by moving mouse
    def paddle_move(self, x):
        self.window.add(self.paddle, y=self.window.height-self.paddle_offset, x=x.x-self.paddle.width/2)
        # paddle limit, cannot go outside the window
        if self.paddle.x > self.window.width-self.paddle.width:
            self.paddle.x = self.window.width-self.paddle.width
        if self.paddle.x < 0:
            self.paddle.x = 0

    # ball velocity
    def ball_move(self, mouse):
        self.switch = True      # after mouse click turn on ball can move
        if not self.end and self.switch and self.ball.x == self.ball_initial_position_x \
                and self.ball.y == self.ball_initial_position_y:
            self.__dy = INITIAL_Y_SPEED  # y movement
            self.__dx = random.randint(1, MAX_X_SPEED)  # x movement
            # dx might 1~max or -(1~max) will not be 0
            if random.random() > 0.5:
                self.__dx *= -1
            return self.__dx and self.__dy

    # getter func to get __dx dy
    def get_ball_x_velocity(self):
        return self.__dx

    def get_ball_y_velocity(self):
        return self.__dy

    def check_for_collisions(self):
        # collide with paddle.
        if self.ball.y > self.window.height/2:
            if self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS) is not None:
                if self.__dy > 0:       # when dy>0 bounce reduce bouncing between paddle
                    self.__dy *= -1
            elif self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS) is not None:
                if self.__dy > 0:
                    self.__dy *= -1

        # collide with bricks
        if self.ball.y < self.window.height/2:
            if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
                self.__dy *= -1
                self.score += 1
            elif self.window.get_object_at(self.ball.x+2*BALL_RADIUS, self.ball.y) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x+2*BALL_RADIUS, self.ball.y))
                self.__dy *= -1
                self.score += 1
            elif self.window.get_object_at(self.ball.x, self.ball.y+2*BALL_RADIUS) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y+2*BALL_RADIUS))
                self.__dy *= -1
                self.score += 1
            elif self.window.get_object_at(self.ball.x+2*BALL_RADIUS, self.ball.y+2*BALL_RADIUS) is not None:
                self.window.remove(self.window.get_object_at(self.ball.x+2*BALL_RADIUS, self.ball.y+2*BALL_RADIUS))
                self.__dy *= -1
                self.score += 1

        # bounce by walls
        if self.ball.x <= 0 or self.ball.x >= self.window.width - BALL_RADIUS:
            self.__dx *= -1
        if self.ball.y <= 0:
            self.__dy *= -1

    def restart(self, num_lives):
        # drop out the window live-1
        if self.ball.y >= self.window.height:
            self.window.remove(self.ball)
            self.window.add(self.ball, x=self.window.width / 2 - BALL_RADIUS, y=self.window.height / 2 - BALL_RADIUS)
            self.x += 1     # die count + 1
            # reset ball condition
            self.__dx = 0
            self.__dy = 0
            self.switch = False

        # break all bricks
        if self.score == self.brick_row*self.brick_col:
            self.window.remove(self.ball)
            self.win = True     # Turn off paddle
            win = GLabel('You win!!!')
            win.font = '-40'
            self.window.add(win, x=(self.window.width-win.width)/2, y=(self.window.height-win.height)/2)
            self.end = True     # close everything

        # live = 0
        if self.x == num_lives:
            end = GLabel('You lose')
            end.font = '-40'
            self.window.add(end, x=(self.window.width-end.width)/2, y=(self.window.height-end.height)/2)
            self.end = True     # close everything





