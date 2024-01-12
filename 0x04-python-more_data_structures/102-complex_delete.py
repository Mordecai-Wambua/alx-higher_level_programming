#!/usr/bin/python
def complex_delete(a_dictionary, value):
    a = [key for key, val in a_dictionary.items() if val == value]

    for key in a:
        del a_dictionary[key]

    return a_dictionary
