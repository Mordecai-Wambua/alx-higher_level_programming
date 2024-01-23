#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square """
    def __init__(self, size=0):
        """Instantiation of the square
        Args:
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for size
        Args:
            value (int): size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns area of the square"""
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character # """
        if self.__size != 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()
