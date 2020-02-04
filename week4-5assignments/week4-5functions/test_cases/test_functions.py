import unittest
from functions.function_library import *

class NamePartTestCase(unittest.TestCase):
    """Tests for functions in the function_library.py file"""

    def test_name_part(self):
        """Here is a bunch of values I think should not work"""
        valid_names_to_test = ["Anthony", "anthony", "   Anthony", "Anthony    ", " anthony", "anthony   "]

        for name in valid_names_to_test:
            self.assertTrue(validate_name_part(name))

    def test_invalid_name_part(self):
        """Here is a bunch of values I think should not work"""
        invalid_names_to_test = ["Anthony'", "123", "   123Anthony", "Anthony $    ", "   ", "anthony#$@#   "]

        for name in invalid_names_to_test:
            self.assertFalse(validate_name_part(name))