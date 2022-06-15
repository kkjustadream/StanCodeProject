"""
File: caesar.py
Name: 黃勝弘
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    secret = int(input('Secret number: '))
    alphabet = input("What's the ciphered string? ")
    upper_alphabet = alphabet.upper()
    real_code = decipher(upper_alphabet, new(secret))
    print('The deciphered string is: ' + str(real_code))


def new(secret):
    """
    param secret: int, how much we need to shift
    return: str, a new alphabet sequence
    """
    new_sequence = ''
    new_sequence = new_sequence + ALPHABET[26 - secret: 26] + ALPHABET[0: 26 - secret]
    # create a new sequence by taking last ? character to the front, and add A~? after.
    return new_sequence


def decipher(alphabet, new_sequence):
    """
    param alphabet: str, the code we entered
    param new_sequence: str, new sequence create by secret num
    return: str, get the code
    """
    new_alphabet = ''
    for i in range(len(alphabet)):
        x = alphabet[i]
        if x.isalpha():
            y = new_sequence.find(x)
            # y = code is no.? in new sequence
            new_alphabet = new_alphabet + ALPHABET[y]
        else:
            new_alphabet += x
    return new_alphabet





#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
