#!/usr/bin/python3
"""Module containing a function that prints  a text"""


def text_indentation(text):
    """
    Fuction that prints a text and 2 new lines after '.' & '?'
    Args:
        text:
            text to be printed
        return:
            No return
        Raises:
            TypeError:
                if the text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        s = text[:]
        for j in ".?:":
            lis = s.split(j)
            s = ""
            for i in lis:
                i = i.strip(" ")
                s = (i + j) if s == "" else s + "\n\n" + i + j

        print(s[: -3])
