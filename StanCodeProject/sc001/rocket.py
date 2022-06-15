"""
File: rocket.py
Name: 黃勝弘
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	# print out head
	for i in range(SIZE):
		for j in range(SIZE - i):
			print(' ', end='')
		for j in range(i + 1):
			print('/', end='')
		for j in range(i + 1):
			print('\\', end='')
		print('')


def belt():
	# print out belt
	print('+', end='')
	for i in range(2 * SIZE):
		print('=', end='')
	print('+')


def upper():
	# print out upper rocket
	for i in range(SIZE):
		for j in range(1):
			print('|', end='')
		for j in range(SIZE - 1 - i):
			print('.', end='')
		for j in range(i + 1):
			print('/' + '\\', end='')
		for j in range(SIZE - 1 - i):
			print('.', end='')
		for j in range(1):
			print('|')


def lower():
	# print out lower rocket
	for i in range(SIZE):
		for j in range(1):
			print('|', end='')
		for j in range(i):
			print('.', end='')
		for j in range(SIZE - i):
			print('\\' + '/', end='')
		for j in range(i):
			print('.', end='')
		for j in range(1):
			print('|')






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()