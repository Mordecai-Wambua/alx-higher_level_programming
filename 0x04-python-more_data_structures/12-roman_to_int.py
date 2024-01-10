#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    x = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    n = 0

    for i in range(len(roman_string)):
        a = x[roman_string[i]]
        if i < len(roman_string) - 1 and x[roman_string[i + 1]] > a:
            n -= a
        else:
            n += a
    return n
