"""
File: weather_master.py
Name: 黃勝弘 Kevin (few hours :<)
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	print("stancode \"Weather Master 4.0\"!")
	data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	if data == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = data
		minimum = data
		next_data = data
		data_number = 1
		cold_day = 0
		data_sum = data
		data_average = data_sum / data_number
		if data < 16:
			cold_day += 1
		while True:
			data_number += 1
			data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if data == EXIT:
				print('Highest temperature = ' + str(maximum))
				print('Lowest temperature = ' + str(minimum))
				print('Average = ' + str(data_average))
				print(str(cold_day) + ' cold day(s)')
				break
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
			if True:
				data_sum = next_data + data
				next_data = data_sum
				data_average = data_sum / data_number
			if data < 16:
				cold_day += 1





















"""

			num += 1
			if data == EXIT:
				print('Highest temperature = ' + str(max))
				print('Lowest temperature = ' + str(min))
				print('Average = ' + str(average))

				print(str(sum_data) + '，' + str(num) + '，' )
				break
			if data > max:
				max = data
			if data < min:
				min = data_m
			if True:
				next_data = data
				sum_data = data + next_data
				average = sum_data / num

"""

















###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
