import unittest
from src.drink import Drink
from src.food import Food

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Tennents", 3.95, 5)

    def test_drink_name(self):
        self.assertEqual("Tennents", self.drink.name)

    def test_drink_price(self):
        self.assertEqual(3.95, self.drink.price)

    def test_drink_alcoholic_status(self):
        self.assertEqual(5, self.drink.alcohol_level)

    def test_return_drink(self):
        self.assertEqual(self.drink, self.drink.return_drink("Tennents"))
