#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as ex:
        print("Exeption: {}".format(ex), file = sys.stderr)
        return None
