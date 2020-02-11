import unittest
from classes.phonebook import PhoneBook

class TestPhoneClass(unittest.TestCase):
    """Test the phonebook class"""

    def setUp(self):
        """creates an instance of the phonebook class for testing all class functions"""
        self.my_phone = PhoneBook()

    def test_invalid_name_validator(self):
        """Tests validation of name_input with invalid possible values"""
        """I think these names will not work"""
        invalid_names = ["Anthony Pietrzak", "    5676AlissaTyreen", "TroyBaker#$%    "]
        for values in invalid_names:
            self.assertFalse(self.my_phone.name_validator(values))

    def test_name_validator(self):
        """Tests validation of name_input"""
        """I think these name will work"""
        valid_names = ["AnthonyPietrzak", "    AlissaTyreen", "TroyBaker    "]
        for values in valid_names:
            self.assertTrue(self.my_phone.name_validator(values))

    def test_phone_number_failure(self):
        """Tests adding an invalid phone number to the list"""
        """I think these will not work"""
        invalid_phones = ["5862462296#$", "   576@#475657", "5679830    "," "," 6985","049587%^&"]
        for values in invalid_phones:
            self.assertFalse(self.my_phone.phone_validator(values))

    def test_phone_number_success(self):
        """Tests adding a valid phone number to the list"""
        """I think these will work"""
        valid_phones = ["5862462286", "   5768475657", "5679830456    "]
        for values in valid_phones:
            self.assertTrue(self.my_phone.phone_validator(values))

    def test_type_validator_failure(self):
        """Tests adding an invalid phone type to the list"""
        """I think these will work"""
        invalid_type = ["hsadkjh", "   office$%", "cells   ","1235467","fash46"]
        for values in invalid_type:
            self.assertFalse(self.my_phone.type_validator(values))
  
    def test_type_validator_success(self):
        """Tests adding a valid phone type to the list"""
        """I think these will work"""
        valid_type = ["office", "   cell", "home   "]
        for values in valid_type:
            self.assertTrue(self.my_phone.type_validator(values))


    

    