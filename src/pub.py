class Pub:
    def __init__(self, name, till, drinks_list):
        self.name = name
        self.till = float(till)
        self.drinks_list = drinks_list

    def get_drinks_list(self, customer):
        if customer.age >= 18:
            return [drink for drink in self.drinks_list]
        else:
            return [drink for drink in self.drinks_list if drink.alcohol_level == 0]

    def get_stock_count(self):
        return len(self.drinks_list)

    def get_drink(self, drink_name):
        for drink in self.drinks_list:
            if drink.return_drink(drink_name):
                return drink

    def get_drink_price(self, drink_name):
        drink = self.get_drink(drink_name)
        if drink == None:
            return "Drink not in stock"
        else:
            return drink.price

    def check_age(self, customer, drink_name):
        age = customer.age
        drink = self.get_drink(drink_name).alcohol_level
        if age < 18 and drink > 0:
            return False
        return True

    def add_drink_to_customer(self, customer, drink_name):
        # Always call this function BEFORE remove_drink()
        customer.stomach.append(self.get_drink(drink_name))

    def remove_drink(self, drink_name):
        self.drinks_list.remove(self.get_drink(drink_name))

    def check_drunkenness(self, customer):
        if customer.drunkenness > 3:
            return False
        return True

    def in_stock(self, drink_name):
        if self.get_drink(drink_name) == None:
            return False
        return True
