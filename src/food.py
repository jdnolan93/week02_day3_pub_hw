class Food:
    def __init__(self, name, price, rejuvination_level):
        self.name = name
        self.price = price
        self.rejuvination_level = rejuvination_level

    def return_food(self, food_name):
        if self.name == food_name:
            return self

