#!/usr/bin/python3
"""class inheriting from class int."""


class MyInt(int):
    """subclass of class Int."""

    def __eq__(self, other):
        """Override equality operator."""
        return int(str(self)) != other

    def __ne__(self, other):
        """Override inequality operator."""
        return int(str(self)) == other
