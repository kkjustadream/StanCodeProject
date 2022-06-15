"""
File: quadratic_solver.py
Name: 黃勝弘 Kevin (1hr 10min)
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


print('stanCode Quadratic Solver!')


def main():

	a = int(input('a= '))
	b = int(input('b= '))
	c = int(input('c= '))
	discriminant = b ** 2 - 4 * a * c
	while discriminant >= 0:
		if discriminant == 0:
			print('One root: ' + str((-b + math.sqrt(discriminant)) / (2 * a)))
			break
		else:
			print('Two roots: ' + str((-b + math.sqrt(discriminant)) / (2 * a)) + '，' + str((-b - math.sqrt(discriminant)) / (2 * a)))
			break
	while discriminant < 0:
		print('No real roots')
		break





###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
