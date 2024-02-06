#!/usr/bin/python3
"""Function that returns the dictionary description for JSON object."""


def class_to_json(obj):
    """Return dictionary description.

    Args:
        obj: actual JSON object
    """
    return (obj.__dict__)
