#!/usr/bin/python3
"""
modele that tests class base
"""
import pycodestyle
import unittest
import os
Base = __import__('models.base').Base
from models.rectangle import Rectangle
from models.square import Square

class test_base(unittest.TestCase):
    """Class that test all the methods in class Base"""

    def test_pep8_base(self):
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(["models/base.py"])
        self.assertEqual(
            check.total_errors, 0, "Found code style errors (WARNING!!)."
        )

if __name__ == "__main__":
    unittest.main()
