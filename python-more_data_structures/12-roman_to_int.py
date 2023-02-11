#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
    total = 0
    if (type(roman_string) is not str or roman_string is None):
        return 0
    for i, char in enumerate(roman_string):
        tmp_num = roman_num[char]
        try:
            if tmp_num < roman_num[roman_string[i + 1]]:
                tmp_num = tmp_num * -1
        except IndexError:
            pass
        total = total + tmp_num
    return (total)
