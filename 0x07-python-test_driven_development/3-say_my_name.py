#!/usr/bin/python3
""" Function to print the first and last name of a person"""


def say_my_name(first_name, last_name=""):
    """
        Function to print a person's first and last name
        Args:
            first_name (string): first
            last_name (string): last
    """
    try:
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        elif not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        else:
            print("My name is {} {}".format(first_name, last_name))
    except TypeError as i:
        print(i)
