import difflib


def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()


class Coffee:
    """Coffee contains name, ingredients and cost"""
    def __init__(self, coffee_name, coffee_ingredients: dict, coffee_cost):
        self.name = coffee_name
        self.ingredients = coffee_ingredients
        self.cost = coffee_cost


class Menu:
    def __init__(self):
        self.menu = []

    def append(self, coffee_name: str, coffee_ingredients: dict, coffee_dollars_cost: int):
        self.menu.append(Coffee(coffee_name, coffee_ingredients, coffee_dollars_cost))

    def find_coffee(self, coffee_name: str):
        if len(self.menu) >= 1:
            for coffee in self.menu:
                if similar(coffee_name, coffee.name) >= 0.7:
                    return coffee

        return False
