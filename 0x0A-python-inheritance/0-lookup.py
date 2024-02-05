#!/usr/bin/python3
"""Function to return attributes and methods of an object."""


def lookup(obj):
    """Return the attributes and methods of the object."""
    if obj:
        return list(dir(obj))
