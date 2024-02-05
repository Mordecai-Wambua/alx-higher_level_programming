#!/usr/bin/python3
"""Creation of a child class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Inherit from BaseGeometry."""

    def __init__(self, width, height):
        """Instantiate the class.

        Args:
            width (int): rectangle dimension
            height (int): rectangle dimension
        """        
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
