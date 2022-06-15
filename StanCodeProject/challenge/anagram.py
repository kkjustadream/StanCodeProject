"""
File: anagram.py
Name: 黃勝弘
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
# global variable
DICTIONARY = []
ans_anagram = []
current = ''      # current word


def main():
    """
    TODO:
    """
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator"(or -1 to quit)')
    while True:
        anagram = input('Find anagrams for: ')
        start = time.time()
        if anagram == EXIT:
            break
        else:
            find_anagrams(anagram)
            print(f"{len(ans_anagram)} anagrams: {ans_anagram}")
            ans_anagram.clear()
            end = time.time()

        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    #  get dictionary list
    global DICTIONARY
    with open(FILE, 'r')as f:
        for word in f:
            DICTIONARY += word.strip().split()      # strip to cancel /n


def find_anagrams(s):
    """
    :param s: str, the word we input
    :return: input's anagrams
    """
    global ans_anagram, current
    # base case
    if len(s) == 0:
        # have this word in dict and haven't been search yet
        if current in DICTIONARY and current not in ans_anagram:
            print('Searching...')
            print(f"Found: {current}")
            ans_anagram.append(current)
    # recursion
    else:
        for i in range(len(s)):
            if has_prefix(current) is True:
                # choose
                current += s[i]
                # explore
                s_deleted = s[:i] + s[i+1:]    # create a string that delete a letter ex: kevin pick k remain evin，上限不包含
                find_anagrams(s_deleted)
                # un-choose
                current = current[:-1]  # current = current[:len(current)-1]；[:-1] ==  from 0 to last one(not include last one)


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for word in DICTIONARY:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
    # find_anagrams('arm')
