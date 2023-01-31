#!/usr/bin/python3
"""
This module contains a fuction that prints meassage
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints 'My name is <first name> <last name>'
    Args:
        first_name: first name
        last_name: last name
    Returns:
        no return
    Raises:
        TypeError:
            if first_name or last name is not string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f'My name is {first_name} {last_name}')
