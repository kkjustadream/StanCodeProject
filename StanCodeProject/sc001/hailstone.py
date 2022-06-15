"""
File: hailstone.py
Name: 黃勝弘 Kevin (22min)
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    n = int(input('Enter a number: '))
    step = 0
    while n != 1:
        while n % 2 == 1:
            m = n
            n = 3*n+1
            print(str(m) + ' is odd, so I make 3n+1: ' + str(n))
            step += 1
        while n % 2 == 0:
            m = n
            n = n//2
            print(str(m) + ' is even, so I take half: ' + str(n))
            step += 1
    print('It took ' + str(step) + ' steps to reach 1.')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
