#!/usr/bin/python3
"""Class Square to inherit from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherit from Rectangle - is a special rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square attributes.
        Args:
            size (int): square dimensions
            x (int): position on x axis
            y (int):position on y axis
            id (str): unique identifier
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method."""
        return (self.width)

    @size.setter
    def size(self, size):
        """Setter method."""
        self.width = size
        self.height = size

    def __str__(self):
        """Print the instance."""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))
