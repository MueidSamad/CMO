
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on=True
my_money_machine =MoneyMachine()
my_menu= Menu()
my_coffee_maker= CoffeeMaker()


while is_on:
    options=my_menu.get_items()
    choice="h"
    while choice not in ["latte", "cappuccino", "espresso","off","report"]:
        choice = input(f"What Coffee do you want to drink? ({options})").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        my_money_machine.report()
        my_coffee_maker.report()
    else:
        order=my_menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(order):
            my_money_machine.make_payment(order.cost)
            my_coffee_maker.make_coffee(order)