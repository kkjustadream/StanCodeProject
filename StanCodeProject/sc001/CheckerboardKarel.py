from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: Kevin 黃勝弘
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.

First fill odd straight line and even straight line in orders except last line. 
But need to check if it's ?x1.
Last, check last line is odd or even by check the second to last line is odd or even.
"""


def main():
    """
    pre-condition: Karel at 1-1, facing East
    post-condition: Karel at ?-1, facing East
    """
    fill_with_odd_even_straight_line()
    # facing East
    if not front_is_clear():
        turn_around()
        if not front_is_clear():
            turn_around()
            do_one_straight_line_odd()
            # check is ?x1
        else:
            check_and_fill_last_line()


def check_and_fill_last_line():
    move()
    if on_beeper():
        turn_around()
        move()
        do_one_straight_line_even()
    # left straight line is odd
    else:
        turn_around()
        move()
        do_one_straight_line_odd()
    # left straight line is even

def fill_with_odd_even_straight_line():
    while front_is_clear():
        do_one_straight_line_odd()
        move()
        if front_is_clear():
            do_one_straight_line_even()
            move()

def do_one_straight_line_odd():
    """
    pre-condition: Karel at 1-1, facing East
    post-condition: Karel at 1-1, facing East
    Karel go up
    """
    fill_one_line()
    move_to_bottom()
        # facing South at bottom
    turn_around()
        # facing North at bottom
    while front_is_clear():
        move()
        pick_beeper()
        if front_is_clear():
            move()
        else:
            turn_around()
            # facing South
            if front_is_clear():
                move_to_bottom()
    if not front_is_clear():
        if not facing_south():
            turn_around()
            move_to_bottom()
    turn_left()
    # facing East



def do_one_straight_line_even():
    fill_one_line()
    move_to_bottom()
        # facing South at bottom
    turn_around()
        # facing North at bottom
    while front_is_clear():
        pick_beeper()
        move()
        if front_is_clear():
            move()
        else:
            turn_around()
            # facing South
            if front_is_clear():
                move_to_bottom()
    if not front_is_clear():
        if on_beeper():
            pick_beeper()
    if facing_north():
        turn_around()
        move_to_bottom()
        turn_left()
    if facing_south():
        turn_left()


def move_to_bottom():
    """
    pre-condition: Karel facing South
    post-condition: Karel facing South
    Karel put beeper on all spot
    """
    while front_is_clear():
        move()
def fill_one_line():
    """
    pre-condition: Karel facing East
    post-condition: Karel facing South
    Karel put beeper on all spot
    """
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_around()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
