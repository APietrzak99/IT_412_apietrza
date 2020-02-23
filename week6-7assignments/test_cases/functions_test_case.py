import unittest
from functions.functions import *

class BooksTestCase(unittest.TestCase):
    """Tests the functions in the functions.py file"""

    def test_author_success(self):
        """Here is a bunch of authors I think should work"""
        valid_authors_to_test = ["JD Salinger", "Tolkien", "    Mark    Twain", "William     SHaKeSpEArE    "]

        for author in valid_authors_to_test:
            self.assertTrue(book_author(author))

    def test_author_failure(self):
        """Here is a bunch of authors I think should not work"""
        invalid_authors_to_test = ["", "JD!@#", "   Saul069", "0495609456", "Salinger#$%", "\\Tolkien4875    "]

        for author in invalid_authors_to_test:
            self.assertFalse(book_author(author))
        

    def test_copies_purchased_success(self):
        """Here is a bunch of values I think should work"""
        valid_values_to_test = ["12", "567", "890", "1234"]

        for value in valid_values_to_test:
            self.assertTrue(book_copies(value))

    def test_copies_purchased_failure(self):
        """Here is a bunch of values I think should not work"""
        invalid_values_to_test = ["", "JD  !@#", "   Sau  l069", "049560  945!@#6", "", "\\To4875    ","1234!   "]

        for value in invalid_values_to_test:
            self.assertFalse(book_copies(value))
        
    def test_isbn_success(self):
        """Here is a bunch of isbns I think should work"""
        valid_isbns_to_test = ["97801940-3039", "9585760498", "930486-393485", "120396-29948"]

        for isbn in valid_isbns_to_test:
            self.assertTrue(book_isbn(isbn))

    def test_isbn_failure(self):
        """Here is a bunch of isbns I think should not work"""
        invalid_isbns_to_test = ["", "123456$%", "11233asd", "Anthonyt12334---", "93458HJOYT", "908   1283     098-GHJOI    "]

        for isbn in invalid_isbns_to_test:
            self.assertFalse(book_isbn(isbn))
    
    def test_retail_success(self):
        """Here is a bunch of values I think should work"""
        valid_values_to_test = ["12.00", "567.56", "890.89", "1234.10","576.46"]

        for value in valid_values_to_test:
            self.assertTrue(book_retail(value))

    def test_retail_failure(self):
        """Here is a bunch of values I think should not work"""
        invalid_values_to_test = ["12!@    ", "   12 . 006!", "130,0001DF", "Anthony", "\\To4875    ","1234!   "]

        for value in invalid_values_to_test:
            self.assertFalse(book_retail(value))

    def test_title_success(self):
        """Here is a bunch of titles I think should work"""
        valid_titles_to_test = ["Catcher     In The Rye", "   Stranger Things", "The things ThEy Carried", "As I Lay Dying    "]

        for title in valid_titles_to_test:
            self.assertTrue(book_title(title))
    
    def test_title_failure(self):
        """Here is a title I think should not work"""
        invalid_titles_to_test = [""]

        for title in invalid_titles_to_test:
            self.assertFalse(book_title(title))

    