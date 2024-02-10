#!/usr/bin/python3
"""Class to inherit from Base."""
from models.base import Base


class Rectangle(Base):
    """Manage id attribute in all future classes."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate the Rectangle class."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return values of the width."""
        return (self.__width)

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """Return values of the height."""
        return (self.__height)

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """Return value of x."""
        return (self.__x)

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Return value of y."""
        return (self.__y)

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Return the area value of the Rectangle instance."""
        return (self.__width * self.__height)

    def display(self):
        """Print in stdout the Rectangle instance."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Assign argument to each Rectangle attribute."""
        if args is not None and len(args) != 0:
            elements = ['id', 'width', 'height', 'x', 'y']
            for x in range(len(args)):
                setattr(self, elements[x], args[x])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """Print the instance."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))
