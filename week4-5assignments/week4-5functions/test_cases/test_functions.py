import unittest
from functions.function_library import *

class NamePartTestCase(unittest.TestCase):
    """Tests for functions in the function_library.py file"""

    def test_name_part(self):
        """Here is a bunch of titles I think should work"""
        valid_titles_to_test = ["Catcher     In The Rye", "   Stranger Things", "The things ThEy Carried", "As I Lay Dying    "]

        for title in valid_titles_to_test:
            self.assertTrue(book_title(title))

    def test_invalid_name_part(self):
        """Here is a bunch of values I think should not work"""
        invalid_names_to_test = ["Anthony'", "123", "   123Anthony", "Anthony $    ", "   ", "anthony#$@#   "]

        for name in invalid_names_to_test:
            self.assertFalse(validate_name_part(name))