"""
File: largest_digit.py
Name: 黃勝弘
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int
	:return:
	"""
	largest_digit = 0
	final_ans = find_largest_digit_helper(n, largest_digit)
	return final_ans


def find_largest_digit_helper(n, largest_digit):
	# check +-
	if n < 0:
		n = -n
	# base case only have 1 digit left
	if n < 10:
		if n > largest_digit:
			return n
		else:
			return largest_digit
	# have more than 1 digit ex: 12, 364...
	else:
		y = n // 10		# become next number
		y2 = n % 10		# digit
		if y2 > largest_digit:
			return find_largest_digit_helper(y, y2)		# need to return
		else:
			return find_largest_digit_helper(y, largest_digit)		# need to return


if __name__ == '__main__':
	main()
# def code_tracing():
# 	sc = [1, 2, 3]
# 	if sc.pop() is 3.0:
# 		print('A1: ', sc)
# 	else:
# 		print('A2: ', sc)
# 	cs = ['hi']
# 	mystery(sc, cs)
# 	print('A3:',sc,cs)
#
# def mystery(cs,sc):
# 	if len(cs):
# 		print('A5:', sc)
# 	else:
# 		print('A6:',sc)
# 	cs = sc
#
# if __name__ == '__main__':
# 	code_tracing()
