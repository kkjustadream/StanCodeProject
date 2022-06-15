"""
File: similarity.py (extension)
Name: 黃勝弘
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    long_seq = input(str('Please give me a DNA sequence to search: ')).upper()
    short_seq = input(str('What DNA sequence would you like to match? ')).upper()
    a = len(long_seq)
    b = len(short_seq)
    c = a - b + 1
    # c = we need to check long sequence to character no.c
    max_no = 0
    # max similarity
    from_which = 0
    # max similarity is from no.?? ; initial: no.0
    similarity = 0
    for i in range(0, c, 1):
        # we need to check from no.0 to no.c
        same_num = 0
        # save how many same character
        not_same = 0
        # save how many not_same character
        for j in range(b):
            # check long sequence for len(short seq) times
            lo = long_seq[j + i]
            s = short_seq[j]
            if s == lo:
                same_num += 1
            else:
                not_same += 1
        similarity = (same_num / len(short_seq)) * 100
        if similarity > max_no:
            max_no = similarity
            from_which = i
            # print(best_match(from_which, long_seq, short_seq))
            # print(str(max_no))
            # print(str(similarity))
    print('The best match is ' + str(best_match(from_which, long_seq, short_seq)))
    print('Similarity is ' + str(max_no) + '%')


def best_match(j, long, short):
    x = ''
    for i in range(len(short)):
        a = long[j + i]
        x += a
    return x


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
