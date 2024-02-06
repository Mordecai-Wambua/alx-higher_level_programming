#!/usr/bin/python3
"""Script adding all arguments to a python list."""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = \
        __import__("6-load_from_json_file").load_from_json_file

    try:
        inputs = load_from_json_file("add_item.json")
    except FileNotFoundError:
        inputs = []
    inputs.extend(sys.argv[1:])
    save_to_json_file(inputs, "add_item.json")
