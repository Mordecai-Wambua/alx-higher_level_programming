#!/usr/bin/python3
"""The first class Base."""
import json


class Base:
    """Manage id attribute in all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class.

        Args:
            id (int): identifier
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON representation to list_dictionaries.
        Args:
            list_dictionaries (list): list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == []:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON representation of list_objs to a file.
        Args:
            list_objs (list): list of instances inheriting from cls"""
        if list_objs is None:
            list_objs = []
        list_objs = [obj.to_dictionary() for obj in list_objs]

        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Return list of JSON representation json_string.
        Args:
            json_string (str): string rep of a list of dictionaries"""
        if (json_string is None or json_string == []):
            return ([])
        return (json.loads(json_string))
