#!/usr/bin/python3
"""Creation of an empty class."""


class BaseGeometry:
    """Based on 5-base_geometry."""

    def area(self):
        """Unimplemented method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate user value.

        Args:
            name (str): input string
            value (int): value to be validated
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
