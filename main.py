from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

shutdown = False
while not shutdown:
    order = input(f"What would you like? {menu.get_items()} :")
    if order == 'report':
        coffee_machine.report()
        money_machine.report()
    elif order == 'exit':
        shutdown = 'True'
    else:
        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)


