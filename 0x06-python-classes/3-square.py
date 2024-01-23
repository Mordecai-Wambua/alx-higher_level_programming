#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square """
    def __init__(self, size=0):
        """Instantiation of the square
        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns area of the square"""
        return self.__size**2
