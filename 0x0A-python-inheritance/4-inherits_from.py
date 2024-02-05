#!/usr/bin/python3
"""Function checking of object is an instance of a class that inherited."""


def inherits_from(obj, a_class):
    """Return True if  is an instance else False.

    Args:
        obj: object
        a_class: specified class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
