#!/usr/bin/python3
"""Function that creates an Object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create object from the JSON file.

    Args:
        my_obj: actual object
        filename: text file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))
