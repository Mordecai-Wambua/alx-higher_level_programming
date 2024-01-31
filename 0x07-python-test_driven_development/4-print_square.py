#!/usr/bin/python3
"""Function to print a square visually using th '#' character"""


def print_square(size):
    """Function to print a square
        Args:
            size (int): square dimensions
    """
    try:
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif (type(size) is float and size < 0):
            raise TypeError("size must be an integer")
        else:
            for i in range(size):
                print("#" * size)
    except Exception as i:
        raise i
