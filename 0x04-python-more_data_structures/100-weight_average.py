#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    a, b = 0, 0
    for i in my_list:
        a += i[0] * i[1]
        b += i[1]

        return (a / b)
