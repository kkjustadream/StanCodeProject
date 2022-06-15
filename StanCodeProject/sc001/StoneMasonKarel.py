from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: Kevin 黃勝弘
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    pre-condition: Karel at 1-1, facing East
    post-condition: Karel at ?-1, facing East
    """
    while front_is_clear():
        climb_up()
        climb_down()
        go_to_another()
    if not front_is_clear():
        climb_up()
        climb_down()


def climb_up():
    """
    pre-condition: Karel at 1-1, facing east
    post-condition: Karel climb up 5 steps, facing South
    """
    turn_left()
    # facing North
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    while not front_is_clear():
        if on_beeper():
            turn_around()
        else:
            put_beeper()
            turn_around()
    # facing South





def climb_down():
    """
    pre-condition: Karel at 1-5, facing South
    post-condition: Karel climb down 5 steps, facing East
    """
    for i in range(4):
        move()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def go_to_another():
    """
    pre-condition: facing East
    post-condition: facing East
    """
    for i in range(4):
        move()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
