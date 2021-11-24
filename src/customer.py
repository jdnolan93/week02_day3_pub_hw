class Customer:
    def __init__(self, name, age, stomach, wallet):
        self.name = name
        self.age = age
        self.stomach = stomach
        self.wallet = float(wallet)
        self.drunkenness = 0

    def get_stomach_count(self):
        return len(self.stomach)

    def buy_drink(self, pub, drink_name):
        cost = pub.get_drink_price(drink_name)
        self.wallet -= cost
        pub.till += cost

        for drink in pub.drinks_list:
            if drink_name == drink.name:
                self.drunkenness += drink.alcohol_level

        pub.add_drink_to_customer(self, drink_name)
        pub.remove_drink(drink_name)
        # Check if self.wallet >= pub.get_drink_price("Name")

    def can_afford(self):
        pass
