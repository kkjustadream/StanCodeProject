"""
File: triangular_checker.py
Name: 黃勝弘 Kevin
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    print('Welcome to the triangular number checker!')
    while True:
        a = 0
        n = int(input('n: '))
        if n == EXIT:
            print('Have a good one!')
            break
        if n ==1:
            print(str(n) + ' is a triangular number')
        while a < n:
            if n == (a*(a + 1))/2:
                print(str(n) + ' is a triangular number')
                break
            else:
                a += 1
        if a == n:
            if n != (a * (a + 1)) / 2:
                print(str(n) + ' is not a triangular number')





# print(str(n) + ' is a triangular number')





### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
