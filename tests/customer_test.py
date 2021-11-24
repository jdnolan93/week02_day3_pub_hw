import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Pedro Sanchez", [], 50.0)
        self.drink_1 = Drink("Mahou", 4.5, True)
        self.drink_2 = Drink("Coca-Cola", 2.0, False)
        self.pub = Pub("El Tigre", 1000.0, [self.drink_1, self.drink_2])

    def test_customer_name(self):
        self.assertEqual("Pedro Sanchez", self.customer.name)

    def test_customer_stomach(self):
        self.assertEqual([], self.customer.stomach)

    def test_customer_wallet(self):
        self.assertEqual(50.0, self.customer.wallet)

    @unittest.skip('Skip')
    def test_buy_drink(self):
        self.buy_drink(self.pub, "Mahou")
        # Check if self.wallet >= pub.get_drink_price("Name")
        self.assertEqual()
        # Check money leaves wallet
        # Check money is added to pub.till
        # Check drink is in stomach
        # Check drink leaves stock
        self.assertEqual(1, self.pub.get_stock_count())
        pass
