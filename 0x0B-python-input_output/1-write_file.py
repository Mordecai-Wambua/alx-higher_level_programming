#!/usr/bin/python3
"""File writing function."""


def write_file(filename="", text=""):
    """Write specified text to the given file.

    Args:
        filename: specific file
        text: string to be passed
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
