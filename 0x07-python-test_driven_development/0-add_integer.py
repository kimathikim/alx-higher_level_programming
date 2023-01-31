#!/usr/bin/python3
"""Return the sum of the arguements
    """


def add_integer(a, b=98):
    """
    ARGS:
    a - first arg
    b - second arg

    RETURNS: (a + b)

    RAISES: typeError if a or b is not integer or a float"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
