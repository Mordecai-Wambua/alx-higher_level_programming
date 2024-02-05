#!/usr/bin/python3
"""Function to check if an object is an instance of specified class."""


def is_same_class(obj, a_class):
    """Return True if object is an instance otherwise False.

    Args:
        obj: object being evaluated
        a_class: class
    """
    return isinstance(obj, a_class) and type(obj) == a_class
