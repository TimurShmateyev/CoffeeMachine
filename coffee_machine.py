import menu
import currency_list
import os
import time
import difflib


def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()


class CoffeeMachine:
    """Can cook coffee and sell it"""
    def __init__(self):
        self.commands_list = ["off", "report", "new coffee", "add resources", "order"]
        self.resources = {"water": 300, "milk": 200, "coffee": 100}
        self.dollars = 0
        self.menu = menu.Menu()
        self.working = True
        input_correctly = False
        self.currency = None
        while not input_correctly:
            input_currency = input("Enter a currency: ").lower()
            expected_currency = currency_list.check_currency(input_currency)
            if expected_currency != [None, None]:
                input_correctly = True
                self.currency = expected_currency

    def check_resources(self, coffee_ingredients: menu.Coffee):

        have_ingredients_in_func = True
        for resource in self.resources.keys():
            if coffee_ingredients.ingredients[resource] > self.resources[resource]:
                have_ingredients_in_func = False
        return have_ingredients_in_func

    def off(self):
        self.working = False
        os.system("CLS")
        print("\nSTART DISABLING COFFEE MACHINE!\n")
        time.sleep(3)
        num = 0
        while num < 100:
            num += 1
            print(f"{num}%")
            time.sleep(0.05)
        print("SUCCESSFULLY STOPPED")

    def report(self):
        print(f"""
water: {self.resources["water"]} ml
milk: {self.resources["milk"]} ml
coffee: {self.resources["coffee"]} gr""")
        print(f"money: {self.dollars / self.currency[1][0]} {self.currency[0]}")

    def new_coffee(self):
        coffee_name = input("Enter coffee name: ").lower()
        coffee_ingredient_water = int(input("Enter count of ml water: "))
        coffee_ingredient_milk = int(input("Enter count of ml milk: "))
        coffee_ingredient_coffee = int(input("Enter count of gr coffee: "))
        coffee_cost = float(input(f"Enter {self.currency[0]} price of the coffee: ")) * self.currency[1][0]
        self.menu.append(coffee_name, {"water": coffee_ingredient_water, "milk": coffee_ingredient_milk, "coffee": coffee_ingredient_coffee}, coffee_cost)

    def add_resources(self):

        water = int(input("how much water? "))
        milk = int(input("how much milk? "))
        coffee = int(input("how much coffee? "))
        self.resources["water"] = self.resources["water"] + water
        self.resources["milk"] = self.resources["milk"] + milk
        self.resources["coffee"] = self.resources["coffee"] + coffee

    def order(self):

        drink_input = input("Enter coffee name: ").lower()
        while not self.menu.find_coffee(drink_input):
            drink_input = input("Sorry! I dont understand you, try again: ")

        coffee = self.menu.find_coffee(drink_input)
        have_ingredients = self.check_resources(coffee)
        user_money = float(input(f"How much you spend {self.currency[0]}: ")) * self.currency[1][0]
        have_money = True if coffee.cost <= user_money else False
        if have_money and have_ingredients:
            change = (user_money - coffee.cost) / self.currency[1][0]
            self.dollars += coffee.cost
            print(f"Here is you change: {round(change, 2)}. Enjoy the coffee")
        elif not have_money:
            print(f"Sorry, you dont have money to buy this coffee!")
        elif not have_ingredients:
            print(f"Sorry, coffee machine don't have ingredients, tell the administration about this event")
        else:
            print(f"You dont have money to buy coffee, and coffee machine dont have ingredients!")

    def navigator(self, user_command):
        match user_command:
            case "off":
                self.off()
            case "report":
                self.report()
            case "new coffee":
                self.new_coffee()
            case "add resources":
                self.add_resources()
            case "order":
                self.order()

    def main_loop(self):
        while self.working:
            print("\n")
            for i in self.commands_list:
                print(i)
            user_input = input("\nType a command: ").lower()
            similar_word = ""
            similar_percent = 0
            for i in self.commands_list:
                if similar(user_input, i) >= similar_percent and similar(user_input, i) >= 0.7:
                    similar_word = i
                    similar_percent = similar(user_input, i)

            if similar_word == "":
                print("Sorry, i dont understand you!")
            else:
                self.navigator(similar_word)
