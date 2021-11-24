class Drink:
    def __init__(self, name, price, alcohol_level):
        self.name = name
        self.price = float(price)
        self.alcohol_level = alcohol_level

    def return_drink(self, drink_name):
        if self.name == drink_name:
            return self
