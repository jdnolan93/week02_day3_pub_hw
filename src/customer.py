class Customer:
    def __init__(self, name, age, stomach, wallet):
        self.name = name
        self.age = age
        self.stomach = stomach
        self.wallet = float(wallet)
        self.drunkenness = 0

    def get_stomach_count(self):
        return len(self.stomach)

    def can_afford(self, drink):
        if self.wallet < drink.price:
            return False
        return True

    def buy_drink(self, pub, drink_name):
        if pub.in_stock(drink_name) == False:
            return "Drink not in stock"

        if pub.check_age(self, drink_name) == False:
            return "Need to be over 18"

        if self.can_afford(pub.get_drink(drink_name)) == False:
            return "Not enough money"

        if pub.check_drunkenness(self) == False:
            return "Too drunk"

        cost = pub.get_drink_price(drink_name)
        self.wallet -= cost
        pub.till += cost

        self.drunkenness += pub.get_drink(drink_name).alcohol_level

        pub.add_drink_to_customer(self, drink_name)
        pub.remove_drink(drink_name)
        # Check if self.wallet >= pub.get_drink_price("Name")


    def buy_food(self, pub, food_name):
        if pub.in_stock(food_name) == False:
            return "Food not in stock"

        if self.can_afford(pub.get_food(food_name)) == False:
            return "Not enough money"

        cost = pub.get_food_price(food_name)
        self.wallet -= cost
        pub.till += cost

        self.drunkenness -= pub.get_food(food_name).alcohol_level
