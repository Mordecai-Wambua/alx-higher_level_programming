#!/usr/bin/python3
"""Function to return the object from its JSON representation."""
import json


def from_json_string(my_str):
    """Return the actual object from its JSON representation.

    Args:
        my_str: specific JSON string
    """
    return json.loads(my_str)
