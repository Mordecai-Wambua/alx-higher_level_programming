#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square """
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation of the square
        Args:
            size (int): size of square
            position (tuple): position of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns area of the square"""
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character # """
        if self.__size != 0:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.__size)
        else:
            print()

    def __str__(self):
        output = []
        if self.__size != 0:
            for i in range(self.__position[1]):
                output.append(" ")
            for i in range(self.__size):
                output.append(" " * self.__position[0] + "#" * self.__size)
        else:
            output.append("")
        return ('\n'.join(output))
