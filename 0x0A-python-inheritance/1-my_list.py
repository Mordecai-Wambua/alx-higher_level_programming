#!/usr/bin/python3
"""class to inherit class list."""


class MyList(list):
    """Inherit properties of class list."""

    def print_sorted(self):
        """Sort the list in ascending order."""
        print(sorted(self))
