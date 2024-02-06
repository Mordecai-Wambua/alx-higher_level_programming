#!/usr/bin/python3
"""Class defining a student."""


class Student:
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiate class.

        Args:
            first_name: student's first name
            last_name: student's last name
            age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve dictionary representation."""
        return self.__dict__
