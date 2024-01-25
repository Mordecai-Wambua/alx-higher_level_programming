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

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
