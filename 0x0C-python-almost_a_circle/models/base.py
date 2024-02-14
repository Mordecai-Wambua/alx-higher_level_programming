#!/usr/bin/python3
"""The first class Base."""
import json
import csv
import turtle


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

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.
        Args:
            dictionary: double pointer to a dictionary"""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return (instance)

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        json_file = str(cls.__name__) + ".json"
        try:
            with open(json_file, "r") as f:
                dicts = cls.from_json_string(f.read())
                return ([cls.create(**i) for i in dicts])
        except FileNotFoundError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize the csv.
        Args:
            list_objs (list):  list of instances who inherits of Base
        """
        with open("{}.csv".format(cls.__name__), "w", newline='') as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes the csv."""
        csv_file = str(cls.__name__) + ".csv"
        try:
            with open(csv_file, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                output = csv.DictReader(f, fieldnames=fields)
                output = [dict([k, int(v)] for k, v in i.items())
                          for i in output]
                return [cls.create(**i) for i in output]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draws all the Rectangles and Squares:"""
        import turtle
        import time
        from random import randrange
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
