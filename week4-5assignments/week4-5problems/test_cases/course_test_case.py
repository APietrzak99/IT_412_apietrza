import unittest
from functions.function_library import *

class SectionPartTestCase(unittest.TestCase):
    """Tests the functions in the function_library.py file"""

    def test_section_part(self):
        """Here is what I think should work"""
        valid_course_names_test = ["IT412", "It410", "   IT413","IT408    ","   IT405", "IT438    "]
        for courses in valid_course_names_test:
            self.assertTrue(validate_course_part(courses))
        valid_semester_test = ["Fall2010","winter2090", "   Summer2050", "Spring2020   ", "    spring2040", "fall2030   "]
        for semesters in valid_semester_test:
            self.assertTrue(validate_course_part(semesters))
