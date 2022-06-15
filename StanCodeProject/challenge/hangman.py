"""
File: hangman.py
Name: 黃勝弘
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    guess_left = N_TURNS
    code = random_word()
    already_guessed = ''
    # help to remember what we have already guessed
    print('The word looks like ' + str(dashed(code)))
    print('You have ' + str(guess_left) + ' wrong guesses left.')
    while guess_left > 0:
        input_ch = input('Your guess: ')
        input_ch_upper = input_ch.upper()
        if len(input_ch_upper) == 1 and input_ch_upper.isalpha():
            # check if input is single letter, if input is alpha
            if input_ch_upper in code:
                already_guessed += input_ch_upper
                # put input in already guessed
                check = 0
                # check if we get the full ans
                print('You are correct!')
                (ans1, check1) = dashed_2(code, check, already_guessed)
                # catch the return value
                if check1 == len(code):
                    # we get the full code
                    print('You win!!' + '\n' + 'The word was: ' + str(code))
                    break
                else:
                    # we didn't get the full ans
                    print('The word looks like ' + str(ans1), end='')
                    print('')
                    print('You have ' + str(guess_left) + ' wrong guesses left.')
            else:
                # we didn't guess right
                check = 0
                (ans1, check1) = dashed_2(code, check, already_guessed)
                # catch the return value
                print('There is no ' + str(input_ch_upper) + ' in the word')
                guess_left -= 1
                if guess_left == 0:
                    # no more chances
                    print('You are completely hung :(')
                    print('The word was: ' + str(code))
                    break
                print('The word looks like ' + str(ans1), end='')
                print('')
                print('You have ' + str(guess_left) + ' wrong guesses left.')
        else:
            print('illegal format')


def dashed_2(code, check, already_guessed):
    """
    param code: str, the code we choose
    param check: check if we get the full ans
    param already guessed: str, save the letter we already guessed
    return ans: str, reveal correct letter with other still remain -
    """
    ans = ''
    for i in range(len(code)):
        dashed_code = code[i]
        if dashed_code in already_guessed:
            # if already_guessed has code character, print out
            check += 1
            ans += dashed_code
        else:
            ans += '-'
    return ans, check


def dashed(code):
    """
    param input_ch_upper: str, the upper of input_ch
    param code: str, the random word
    return: str, create a code length -(ex: ABC  -->  ---)
    """
    a = ''
    for i in range(len(code)):
        a += '-'
    return a


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
