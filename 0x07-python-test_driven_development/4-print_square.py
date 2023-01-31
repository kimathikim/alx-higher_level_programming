#!/usr/bin/python3
"""Module with a  function that prints out Squire"""


def print_square(size):
    """function that prints Square
    Arg:
        size: the size of the square
    Return:
        No returns
    Exeptions:
        TypeError:
            if size is not an integer
            if size is a float and is less than 0
        ValueError:
            if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for row in range(size):
            for cul in range(size):
                print("#", end="")
            if row < cul:
                print()
        print()
