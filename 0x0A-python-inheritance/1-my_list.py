#!/usr/bin/python3
"""class to inherit from list."""


class MyList(list):
    """Inherit from list."""

    def print_sorted(self):
        """Sort the list in ascending order."""
        print(sorted(self))
