#!/usr/bin/python3
"""an empty class Rectangle that defines a rectangle."""


class Rectangle:
    """Empty class for a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize of arguments.

        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for rectangle width."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for width.

        Args:
            value (int): user input for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for rectangle height."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter for height.

        Args:
            value (int): user input for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
