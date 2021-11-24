import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Montadito", 1, 2)

    # @unittest.skip("deletethis")
    def test_food_name(self):
        self.assertEqual("Montadito", self.food.name)

    # @unittest.skip("deletethis")
    def test_food_price(self):
        self.assertEqual(1, self.food.price)

    # @unittest.skip("deletethis")
    def test_rejuvination_level(self):
        self.assertEqual(2, self.food.rejuvination_level)