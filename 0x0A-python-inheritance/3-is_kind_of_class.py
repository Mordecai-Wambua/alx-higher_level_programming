#!/usr/bin/python3
"""Function to evaluate if object is an instance of class or one that inherited."""

def is_kind_of_class(obj, a_class):
    """Return True if is an instance of or of an inheriting class else False
    Args:
        obj: actual object
        a_class: evaluating class
    """
    return (isinstance(obj, a_class))
