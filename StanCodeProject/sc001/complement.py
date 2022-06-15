"""
File: complement.py
Name: 黃勝弘
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    data = input("Please give me a DNA strand and I'll find the complement: ")
    upper_data = data.upper()
    print('The complement of ' + str(data) + ' is ' + build_complement(upper_data))


def build_complement(upper_data):
    """
    param upper_data: str, what we entered, but in upper condition
    return: str, the ans after changing
    """
    ans = ''
    for i in range(len(upper_data)):
        complement = upper_data[i]
        # pick out each character in upper_data
        if complement == 'A':
            ans += 'T'
        elif complement == 'T':
            ans += 'A'
        elif complement == 'C':
            ans += 'G'
        elif complement == 'G':
            ans += 'C'
    return ans




###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
