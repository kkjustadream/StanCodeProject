"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
DICTIONARY = []
####################
TEST = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]
# f y c l
# i o m g
# o r i l
# h j h u
###################


def main():
	"""
	TODO:
	"""
	read_dictionary()
	# input 4 rows
	list = []
	for i in range(4):
		input_letter = input(str(i+1) + ' row of letters: ').lower()
		list.append([])		# create 4 blank list
		# check if it's legal format
		for j in range(4):
			list[i].append(input_letter[2 * j])  # add input in blank list
			check = input_letter.split()[j]
			if not check.isalpha() or len(check) != 1:
				print('Illegal input')
				break
	####################
	start = time.time()
	# get list = [['a', 'd', 'f', 'g'], ['a', 'd', 'f', 'd'], ['a', 'd', 'f', 'h'], ['a', 'd', 'f', 'e']]
	ans = find_word(list)
	print(ans)
	print('There are ' + str(len(ans)) + ' words in total.')

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(list_input):
	ans = []
	for i in range(4):
		for j in range(4):
			order = [(i, j)]
			find_word_helper(i, j, order, list_input, list_input[i][j], ans)
	# ans:
	# ['firm', 'form', 'foil', 'coif', 'coir', 'corm', 'coil', 'moor', 'moil', 'miri', 'giro',
	# 'glim', 'roil', 'roof', 'room', 'roomy', 'rimy', 'iglu', 'limy', 'limo', 'hoof']
	return ans


def find_word_helper(x, y, coordinate, list_input, word, ans):
	"""

	:param x: str, which row	第幾個row
	:param y: str, which alphabet of the row	row中第幾個字母
	:param coordinate: lst, (x, y)		第幾列第幾個
	:param list_input: lst, input list
			ex: [['a', 'd', 'f', 'g'], ['a', 'd', 'f', 'd'], ['a', 'd', 'f', 'h'], ['a', 'd', 'f', 'e']]
	:param word: str, the alphabet of (x, y)	要開始的字母
	:param ans: lst, ans we return
	:return: ans
	"""
	# base case
	if len(word) >= 4:
		if word in DICTIONARY and word not in ans:
			print(f"Found '{word}'")
			ans.append(word)
	for i in range(-1, 2):		# 左(-1)，中(0)，右(1)
		for j in range(-1, 2):		# 左，中，右
			start_x = x + i  		# 從第幾個row開始
			start_y = y + j			# 從第幾個字母開始
			# check limit 確認是再可行的row範圍和字母範圍 + 沒有從這個字母開始過
			if 0 <= start_x < 4 and 0 <= start_y < 4 and (start_x, start_y) not in coordinate:
				# Choose
				word += list_input[start_x][start_y]		# 將選定字母加入
				coordinate.append((start_x, start_y))		# 將選定子母的座標加入已選定過字母的座標
				# Explore
				if has_prefix(word):
					find_word_helper(start_x, start_y, coordinate, list_input, word, ans)
				# Un-choose
				word = word[:-1]
				coordinate.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	#  get dictionary list
	global DICTIONARY
	with open(FILE, 'r')as f:
		for word in f:
			DICTIONARY += word.strip().split()  # strip to cancel /n


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in DICTIONARY:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
	# find_word([['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']])