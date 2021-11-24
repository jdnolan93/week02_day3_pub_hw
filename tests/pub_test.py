import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    def setUp(self):
        self.adult_customer = Customer("Pedro Sanchez", 50, [], 50.0)
        self.underage_customer = Customer("Abascal", 7, [], 50.0)
        self.drink_1 = Drink("Mahou", 4.5, True)
        self.drink_2 = Drink("Coca-Cola", 2.0, False)
        self.pub = Pub("El Tigre", 1000.0, [self.drink_1, self.drink_2])

    def test_pub_name(self):
        self.assertEqual("El Tigre", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(1000.0, self.pub.till)

    def test_pub_drinks_list(self):
        self.assertEqual([self.drink_1, self.drink_2], self.pub.drinks_list)

    def test_get_stock_count(self):
        self.assertEqual(2, self.pub.get_stock_count())

    def test_get_drinks_list_over_18(self):
        self.assertEqual([self.drink_1, self.drink_2],
                         self.pub.get_drinks_list(self.adult_customer))

    def test_get_drinks_list_under_18(self):
        self.assertEqual([self.drink_2], self.pub.get_drinks_list(
            self.underage_customer))

    def test_get_drink_price_by_name(self):
        self.assertEqual(4.5, self.pub.get_drink_price("Mahou"))
        self.assertEqual("Drink not in stock",
                         self.pub.get_drink_price("Dorada"))
