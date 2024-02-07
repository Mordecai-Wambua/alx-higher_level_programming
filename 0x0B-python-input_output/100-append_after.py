#!/usr/bin/python3
"""Function to insert text after line with specific string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after specific line.

    Args:
        filename: specific filename
        search_string (str): identified string
        new_string (str): string to be added
    """
    nfile = ""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            nfile += line
            if search_string in line:
                nfile += new_string
    with open(filename, "w", encoding="utf-8") as f:
        f.write(nfile)
