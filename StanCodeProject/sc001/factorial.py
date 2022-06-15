"""
File: factioral.py
Name: 黃勝弘 Kevin
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	print('Welcome to stanCode factorial master!')
	ans = 1
	a = 1
	while True:
		n = int(input('Give me a number, and I will list the answer of factorial: '))
		if n == EXIT:
			print('------ See ya! ------')
			break
		while a != n:
			a += 1
			ans = ans * a
		print('Answer: ' + str(ans))




















if __name__ == '__main__':
	main()