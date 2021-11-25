import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food


class TestPub(unittest.TestCase):
    def setUp(self):
        self.adult_customer = Customer("Pedro Sanchez", 50, [], 50.0)
        self.underage_customer = Customer("Abascal", 7, [], 50.0)
        self.drink_1 = Drink("Mahou", 4.5, 5)
        self.drink_2 = Drink("Coca-Cola", 2.0, 0)
        self.drink_3 = Drink("Cruzcampo", 5.0, 5)
        self.food_1 = Food("Montadito", 1.0, 2)
        self.food_2 = Food("Tortilla", 2.5, 5)
        self.pub = Pub("El Tigre", 1000.0, [
                       self.drink_1, self.drink_2, self.drink_3], [self.food_1, self.food_2])

    def test_pub_name(self):
        self.assertEqual("El Tigre", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(1000.0, self.pub.till)

    def test_pub_drinks_list(self):
        self.assertEqual([self.drink_1, self.drink_2,
                         self.drink_3], self.pub.drinks_list)

    def test_get_stock_count(self):
        self.assertEqual(3, self.pub.get_stock_count())

    def test_get_drinks_list_over_18(self):
        self.assertEqual([self.drink_1, self.drink_2, self.drink_3],
                         self.pub.get_drinks_list(self.adult_customer))

    def test_get_drinks_list_under_18(self):
        self.assertEqual([self.drink_2], self.pub.get_drinks_list(
            self.underage_customer))

    def test_get_drink_price_by_name(self):
        self.assertEqual(4.5, self.pub.get_drink_price("Mahou"))
        self.assertEqual("Drink not in stock",
                         self.pub.get_drink_price("Dorada"))

    def test_check_drunkenness(self):
        self.assertEqual(0, self.adult_customer.drunkenness)
        self.adult_customer.buy_drink(self.pub, "Mahou")
        self.assertEqual(5, self.adult_customer.drunkenness)

    def test_get_drink(self):
        self.assertEqual(self.drink_2, self.pub.get_drink("Coca-Cola"))

    def test_refuse_customer(self):
        self.assertEqual(
            True, self.pub.check_drunkenness(self.adult_customer))
        self.adult_customer.buy_drink(self.pub, "Mahou")
        self.assertEqual(
            False, self.pub.check_drunkenness(self.adult_customer))
        self.assertEqual(
            "Too drunk", self.adult_customer.buy_drink(self.pub, "Cruzcampo"))
        self.assertEqual(2, self.pub.get_stock_count())
        self.assertEqual(45.5, self.adult_customer.wallet)

    def test_buy_non_stock_drink(self):
        self.assertEqual("Drink not in stock",
                         self.adult_customer.buy_drink(self.pub, "Dorada"))

    def test_underage_buy_alcohol(self):
        self.assertEqual("Need to be over 18",
                         self.underage_customer.buy_drink(self.pub, "Cruzcampo"))

    def test_get_food_list(self):
        self.assertEqual([self.food_1, self.food_2], self.pub.food_list)
