"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        numbers = soup.find_all('table', {'class', 't-stripe'})
        for number in numbers:
            # data = get ['1', 'Michael 462,383 Jessica 303,115', '2', 'Christopher 360,241 Ashley 301,815'.......]
            data = number.tbody.text.strip().split('\n')
            male = 0
            female = 0
            for i in range(200):
                """
                useful data = 
                ['Noah', '183,076', 'Emma', '194,836']
                ['Liam', '173,797', 'Olivia', '184,355']
                ...
                string !!
                and number has ',', need to remove ','
                """
                useful_data = data[i*2+1].split(' ')
                num = []
                num2 = []
                num += useful_data[1]   # list and has ',' ex: [15,943]
                num2 += useful_data[3]
                # remove ','
                num.remove(',')
                num2.remove(',')
                male += int(''.join(num))
                female += int(''.join(num2))
            print(f"Male number: {male}")
            print(f"Female number: {female}")


if __name__ == '__main__':
    main()
