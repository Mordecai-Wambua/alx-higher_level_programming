#!/usr/bin/python3
"""The first class Base."""


class Base:
    """Manage id attribute in all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class.

        Args:
            id (int): identifier
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
