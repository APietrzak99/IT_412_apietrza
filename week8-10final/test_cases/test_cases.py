import unittest
from functions.validation import *

class CustomerTestCase(unittest.TestCase):
    """Tests the functions in the validation.py file"""

    def test_address_success(self):
        """Here is a bunch of addresses I think should work"""
        valid_addresses_to_test = ["7243 Miller Dr", " 8364   Cassidy-Jones     Dr", "   1029   Shelly    Lane      ", "10263 ShAkESpeArE Dr    "]

        for address in valid_addresses_to_test:
            self.assertTrue(address_number(address))

    def test_address_failure(self):
        """Here is a bunch of addresses I think should not work"""
        invalid_addresses_to_test = ["", " 8364   Cassidy-Jones     Dr!@", "   1029 &  Shelly    Lane @     ", "10263 ShAkESpeArE {} Dr    "]

        for address in invalid_addresses_to_test:
            self.assertFalse(address_number(address))

    def test_city_success(self):
        """Here is a bunch of values I think should work"""
        valid_cities_to_test = ["Macomb", "Troy", "De'Von", "Warren"]

        for city in valid_cities_to_test:
            self.assertTrue(city_validate(city))

    def test_city_failure(self):
        """Here is a bunch of values I think should not work"""
        invalid_cities_to_test = ["", "Smith!", " Smith ", "0947", "", "\\To4875    ","Boston1234!   "]

        for city in invalid_cities_to_test:
            self.assertFalse(city_validate(city))
        
    def test_company_success(self):
        """Here is a bunch of companies I think should work. No values should fail for the company field"""
        valid_companies_to_test = ["Apple ", " ", "Google ", " 9 Lives Tech"]

        for company in valid_companies_to_test:
            self.assertTrue(company_title(company))
    
    def test_email_success(self):
        """Here is a bunch of emails I think should work"""
        valid_emails_to_test = ["", "anthonypietrzak@gmail.com", "    tom.petz@walshcollege.edu", "john_smith98@yahoo.com     ","  tony_gandolfini234@aol.com   "]

        for value in valid_emails_to_test:
            self.assertTrue(email_validate(value))

    def test_email_failure(self):
        """Here is a bunch of emails I think should not work"""
        invalid_emails_to_test = ["anthony'99@gmail.com    ", "   tom(petz)@yahoo.com   ", "ciri&sate@jacob.com    ", "Anthony!", "\\To4875@sbcglobal.net    ","1234!@gmail.com   "]

        for value in invalid_emails_to_test:
            self.assertFalse(email_validate(value))

    def test_name_edit_success(self):
        """Here is a bunch of names I think should work"""
        valid_names_to_test = ["Anthony Pietrzak", "   Tom  Petz", "De'Andre Thomas", "Smith Casey     "]

        for name in valid_names_to_test:
            self.assertTrue(name_edit_validate(name))
    
    def test_name_edit_failure(self):
        """Here is a bunch of names I think should not work"""
        invalid_names_to_test = ["", "Andre-The-Giant", "Athony94840  "," Jonathan Banks!@    "]

        for name in invalid_names_to_test:
            self.assertFalse(name_edit_validate(name))
    
    def test_name_success(self):
        """Here is a bunch of names I think should work"""
        valid_names_to_test = ["Anthony", "Tom", "De'Andre", "Smith","Ja'name"]

        for name in valid_names_to_test:
            self.assertTrue(name_validate(name))
    
    def test_name_failure(self):
        """Here is a bunch of names I think should not work"""
        invalid_names_to_test = [" ", "Andre-The-Giant", "Athony94840  "," Jonathan Banks!@    ", "John Ryley", "Tripell  "]

        for name in invalid_names_to_test:
            self.assertFalse(name_validate(name))

    def test_phone_success(self):
        """Here is a bunch of phone numbers I think should work"""
        valid_phones_to_test = ["586-735-8820", "534-202-9876", "5634635236", "283-109-9987","125-098-7685"]

        for phone in valid_phones_to_test:
            self.assertTrue(phone_number(phone))
    
    def test_phone_failure(self):
        """Here is a bunch of phone numbers I think should not work"""
        invalid_phones_to_test = ["", "586 209 0987", "586A758A3546  "," Hello   ", "283-100-7865y", "2360088900     "]

        for phone in invalid_phones_to_test:
            self.assertFalse(phone_number(phone))

    def test_second_phone_success(self):
        """Here is a bunch of phone numbers I think should work"""
        valid_phones_to_test = ["586-735-8820", "534-202-9876", "5634635236", "283-109-9987","125-098-7685",""]

        for phone in valid_phones_to_test:
            self.assertTrue(second_phone_number(phone))
    
    def test_second_phone_failure(self):
        """Here is a bunch of phone numbers I think should not work"""
        invalid_phones_to_test = ["586 209 0987", "586A758A3546  "," Hello   ", "283-100-7865y", "2360088900     "]

        for phone in invalid_phones_to_test:
            self.assertFalse(second_phone_number(phone))

    def test_state_success(self):
        """Here is a bunch of states I think should work"""
        valid_states_to_test = ["MI", "AZ", "CO", "OR","PA"]

        for state in valid_states_to_test:
            self.assertTrue(state_validate(state))
    
    def test_state_failure(self):
        """Here is a bunch of states I think should not work"""
        invalid_states_to_test = ["", "MICHIGAN", "Mi","aZ", "arizona", "OR   "]

        for state in invalid_states_to_test:
            self.assertFalse(state_validate(state))

    def test_zip_success(self):
        """Here is a bunch of zips I think should work"""
        valid_zips_to_test = ["48041", "3689", "49317", "2637","1946"]

        for zip in valid_zips_to_test:
            self.assertTrue(zip_validate(zip))
    
    def test_zip_failure(self):
        """Here is a bunch of zips I think should not work"""
        invalid_zips_to_test = ["", "48094-1610", "435","2534  ", "zip code", "079   "]

        for zip in invalid_zips_to_test:
            self.assertFalse(zip_validate(zip))

    