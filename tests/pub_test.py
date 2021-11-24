import unittest
from src.pub import Pub
from src.drink import Drink


class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Mahou", 4.5, True)
        self.drink_2 = Drink("Coca-Cola", 2.0, False)
        self.pub = Pub("El Tigre", 1000.0, [self.drink_1, self.drink_2])

    def test_pub_name(self):
        self.assertEqual("El Tigre", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(1000.0, self.pub.till)

    def test_pub_drinks_list(self):
        self.assertEqual([], self.pub.drinks_list)

    def test_get_total_till(self):
        pass

    def test_get_drinks_list(self):
        self.assertEqual([self.drink_1, self.drink_2], self.pub.drinks_list)
