"""
File: prime_checker.py
Name: 黃勝弘 Kevin (1 hr)
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	print('Welcome to prime checker!')

	while True:
		num = int(input('n: '))
		n = num
		if num == EXIT:
			print('Have a good one!')
			break
		while num % (n-1) != 0:
			n = n-1
		if n != 2:
			print(str(num) + ' is not a prime number.')
		else:
			print(str(num) + ' is a prime number.')


















###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
