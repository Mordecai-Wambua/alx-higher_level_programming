#!/usr/bin/python3
"""class inheriting the class Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherit the class Rectangle."""

    def __init__(self, size):
        """Instantiate the class.

        Args:
            size (int): square dimension
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """Return Square Area."""
        area = self.__size ** 2
        return (area)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
