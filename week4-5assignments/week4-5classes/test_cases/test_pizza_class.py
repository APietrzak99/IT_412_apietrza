import unittest
from classes.pizza import Pizza

class TestPizzaClass(unittest.TestCase):
    """Test the pizza class"""

    def setUp(self):
        """creates an instance of the pizza class for testing all class functions"""
        self.my_pizza = Pizza("Anthony's Pizza")

    def test_add_topping_success(self):
        """Tests adding a valid topping to the pizza"""
        self.my_pizza.addTopping("bacon")
        self.assertIn("bacon", self.my_pizza.toppings)

    def test_add_topping_failure(self):
        """Tests adding an invalid topping to the pizza"""
        self.my_pizza.addTopping("onions")
        self.assertNotIn("onions", self.my_pizza.toppings)

    def test_remove_topping_success(self):
        """Tests removing a valid topping from the pizza"""
        self.my_pizza.addTopping("bacon")
        self.assertIn("bacon", self.my_pizza.toppings)
        self.my_pizza.removeTopping("bacon")
        self.assertNotIn("bacon", self.my_pizza.toppings)