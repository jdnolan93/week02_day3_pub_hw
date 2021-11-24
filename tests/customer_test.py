import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Pedro Sanchez", 10, 50.0)

    def test_customer_name(self):
        self.assertEqual("Pedro Sanchez", self.customer.name)

    def test_customer_stomach(self):
        self.assertEqual(10, self.customer.stomach)

    def test_customer_wallet(self):
        self.assertEqual(50.0, self.customer.wallet)
