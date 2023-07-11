from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

isTurnedOn = True
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_coin_machine = MoneyMachine()
my_coffee_maker.report()
my_coin_machine.report()

while isTurnedOn:
    order_name = input(f"What would you like? {my_menu.get_items()}: ")
    if order_name == "report":
        my_coffee_maker.report()
        my_coin_machine.report()
    elif order_name == "off":
        print("Turning off for Maintenance")
        isTurnedOn = False
    else:
        drink = my_menu.find_drink(order_name)
        if order_name in my_menu.get_items():
            if my_coffee_maker.is_resource_sufficient(drink):
                if my_coin_machine.make_payment(drink.cost):
                    my_coffee_maker.make_coffee(drink)
