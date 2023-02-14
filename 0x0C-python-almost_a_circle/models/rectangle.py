#!/usr/bin/python3
import os
from models.base import Base
"""Define Rectangle class that inherits from Base
"""


class Rectangle(Base):
    """The constructor
    args:
        width:
            the width of the rectangle
        height:
            the height of the rectangle
        x:
            `value for x of the new rectangle
        y:
            value for y of the new rectangle
    raises:
        TypeError:
            if the value is not an integer
        ValueError:
            if the value is less of equal to 0
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get the the width of the rectangle"""

        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set/get the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def y(self):
        """set/get the y coordinates of the rectangle"""
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """set/get the y coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """Return the area of a rectangle"""

        return self.height * self.width

    def display(self):
        """Print the rectangle using '#' char."""
        if self.height == 0 or self.width == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for row in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            [print("#", end="") for col in range(self.width)]
            print("")

    def __str__(self):
        """The magic method"""
        return ("""
        "[Rectangle] ({}) {}/{} - {}/{}"
        """.format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Update the rectangle

        args:
            args:
                New attribute values
                 1st represent id
                 2nd represent width
                 3rd represent height
                 4th represent x
                 5th represent y
            **kwards (dict): new key/ value pairs of attribute
        """

        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    self.id = arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
                index += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Method that returns dictionary representation of the rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
