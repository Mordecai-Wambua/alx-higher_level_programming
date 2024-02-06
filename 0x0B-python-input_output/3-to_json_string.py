#!/usr/bin/python3
"""Function to return JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of the specified object.

    Args:
        my_obj: specific object
    """
    return json.dumps(my_obj)
