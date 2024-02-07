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

    def to_json(self, attrs=None):
        """Retrieve dictionary representation.

        Args:
            attrs: list of strings of attributes
        """
        if (type(attrs) == list and
                all(type(x) == str for x in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of Student instance.

        Args:
            json (dict): replacing values
        """
        for i in json:
            self.__dict__[i] = json[i]
