#!/usr/bin/python3
Base = __import__('base').Base
Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """
    Class squire that inherits from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor of a new square

        args:
            size: size of the nw square
            x: the xz coordinate of the new square
            y: the y coordinate of the new square
            id: the itentity of the new square
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set/get the value of size"""

        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """The magic method"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x, self.y, self.height))

    def update(self, *args, **kwargs):
        i = 0
        if args and len(args) != 0:
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    self.id = v
                elif k == "size":
                    self.size = v
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
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
