#!/usr/bin/python3
"""File append function."""


def write_file(filename="", text=""):
    """Write specified text to the end of the given file.

    Args:
        filename: specific file
        text: string to be passed
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
