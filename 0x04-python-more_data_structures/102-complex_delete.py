#!/usr/bin/python
def complex_delete(a_dictionary, value):
    a = list(a_dictionary.keys())

    for v in a:
        if value == a_dictionary.get(v):
            del a_dictionary[v]

    return a_dictionary
