import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Tennents", 3.95, True)

    def test_drink_name(self):
        self.assertEqual("Tennents", self.drink.name)

    def test_drink_price(self):
        self.assertEqual(3.95, self.drink.price)

    def test_drink_alcoholic_status(self):
        self.assertEqual(True, self.drink.status)
