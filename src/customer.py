class Customer:
    def __init__(self, name, stomach, wallet):
        self.name = name
        self.stomach = stomach
        self.wallet = float(wallet)

    def get_stomach_count(self):
        return len(self.stomach)

    def buy_drink(self, pub, drink_name):
        cost = pub.get_drink_price(drink_name)
        self.wallet -= cost
        pub.till += cost
        pub.add_drink_to_customer()
        # Check if self.wallet >= pub.get_drink_price("Name")
        pass
