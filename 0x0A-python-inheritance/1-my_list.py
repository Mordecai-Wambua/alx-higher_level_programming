#!/usr/bin/python3
"""class to inherit from list"""


class MyList(list):
    """Inherit from list"""
    def print_sorted(self):
        x = sorted(self)
        print(x)
