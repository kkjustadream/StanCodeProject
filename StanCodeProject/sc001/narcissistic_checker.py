"""
File: narcissistic_checker.py
Name: 黃勝弘 Kevin (想很久)
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    print('Welcome to the narcissistic checker!')
    while True:
        a = 1
        b = 0
        # a = 10 ^ a
        # b = How many orders
        n = int(input('n: '))
        n2 = n
        if n == EXIT:
            print('Have a good one!')
            break
        else:
            while n // a > 9:
                a *= 10
                b += 1

            total = 0
            x = b + 1
            while b >= 0:
                total += (n // 10 ** b) ** x
                n = n % (10 ** b)
                # order - 1
                b -= 1
                # order change
                # NOW n = 0 !!! b = -1
            if total == n2:
                print(str(n2) + ' is a narcissistic number')
            else:
                print(str(n2) + ' is not a narcissistic number')




"""
------PRACTICE------
        else:
            while n // a > 9:
                a *= 10
                b += 1
            print('a= ' + str(a) + '，' + 'b= ' + str(b))
            total = 0
            x = 0
            b_2 = b
            total_2 = 0
            while b >= 0:
                total += (n // 10 ** b) ** x
                n = n % (10 ** b)
                # number change to -1 order
                b -= 1
                # order change
                # NOW n = 0 !!! b = -1
                if total < n2:
                    x += 1
            while b_2 >= 0:
                total_2 += (n2 // 10 ** b_2) ** x
                n2 = n2 % (10 ** b_2)
                # number change to -1 order
                b_2 -= 1

            print('a= ' + str(a) + '，' + 'b= ' + str(b))
            print('n2= ' + str(n2))
            print('total 2 = ' + str(total_2))
            print('x =' + str(x))
            if total_2 == n_check:
                print(str(n_check) + ' is a narcissistic number')
            else:
                print(str(n_check) + ' is not a narcissistic number')

"""




if __name__ == '__main__':
    main()
