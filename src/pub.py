class Pub:
    def __init__(self, name, till, drinks_list):
        self.name = name
        self.till = float(till)
        self.drinks_list = drinks_list

    def get_drinks_list(self):
        return [drink for drink in self.drinks_list]

    def get_stock_count(self):
        return len(self.drinks_list)

    def get_drink_price(self, drink_name):
        for drink in self.drinks_list:
            if drink_name == drink.name:
                return drink.price
            else:
                return "Drink not in stock"

    def add_drink_to_customer(self, customer, drink):
        # Always call this function BEFORE remove_drink()
        customer.stomach.append(drink)

    def remove_drink(self, drink_name):
        for drink in self.drinks_list:
            if drink_name == drink.name:
                self.drinks_list.remove(drink)
