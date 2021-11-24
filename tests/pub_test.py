import unittest
from src.pub import Pub


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("El Tigre", 1000.0, [])

    def test_pub_name(self):
        self.assertEqual("El Tigre", self.pub.name)

    def test_pub_price(self):
        self.assertEqual(1000.0, self.pub.price)

    def test_pub_drinks_list(self):
        self.assertEqual([], self.pub.drinks_list)
