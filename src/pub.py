class Pub:
    def __init__(self, name, till, drinks_list):
        self.name = name
        self.till = float(till)
        self.drinks_list = drinks_list

    def get_drinks_list(self):
        return [drink for drink in self.drinks_list]
