#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for x in my_list:
        result.append(x % 2 == 0)

    return (result)
