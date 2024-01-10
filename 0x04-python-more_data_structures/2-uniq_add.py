#!/usr/bin/python3
def uniq_add(my_list=[]):
    from functools import reduce
    z = set(my_list)
    y = reduce(lambda x, y: x + y, z, 0)
    return y
