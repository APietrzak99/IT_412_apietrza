import unittest
from classes.inventory import InventoryItem

class InventoryTestCase(unittest.TestCase):
    """Tests the functions in the inventory.py file"""

    def setUp(self):
        """creates an instance of the inventory class for testing all class functions"""
        self.inventory = InventoryItem("Anthony's Pizza")

    def test_default_inventory(self):
        """Here is what I think should work"""
        valid_pass = [""]
        for quantity in valid_pass:
            self.inventory.buy_item(quantity)
            self.assertIn(1, self.inventory.quantity_total_purchased)
        

    def test_override_inventory(self):
        """Here is what I think should work"""
        valid_override_test = [2,34,16,18,20, 13]
        for quantities in valid_override_test:
            self.inventory.buy_item(quantities)
            self.assertIn(quantities, self.inventory.quantity_total_purchased)
        
