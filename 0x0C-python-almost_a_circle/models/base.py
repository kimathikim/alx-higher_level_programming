#!/usr/bin/python3
import json
import turtle
import csv
"""Define the base class
"""


class Base:
    """Rerpresent the "Base" for alll other classes
    attribute:
        The number of instatiated bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initiate a new base
        Args:
        id: The identity of a new base
        """
        if (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON serialization of objects to a file

        Args:
            list_dictionary(list): a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON serialization of a list of objects to a file

        Args:
            list_objs: list of inherited base instances
        """
        filename = cls.__name__ + "json"
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [objs.to_dictionary() for objs in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the JSON deserialization of objects to a file

        Args:
            json_string(list): a list of dictionaries"""
        if json_string is None or json_string == []:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instatiated from a dictionary of atribures

        Args:
            **dictionary (dict): key/value pairs of attributes to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of of class instances instatiated from a json file
         Reads from '<cls.__name__>.json'

         Returns:
            []: if the file does not exists
            [instances]: otherwise
        """
        filename = str(cls.__name__) + "json"
        try:
            with open(filename, 'r', encoding="utf-8") as jfile:
                list_dict = Base.from_json_string(jfile.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
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
