from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: kevin huang 黃勝弘
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    get_the_paper()
    go_back_home()

def get_the_paper():
    """
    pre-condition: Karel at 3-4 facing east
    post-condition: Karel at 6-3 facing west
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_around()


def go_back_home():
    """
    pre-condition: Karel at 6-3 facing west
    post-condition: Karel at 3-4 facing east
    """
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
