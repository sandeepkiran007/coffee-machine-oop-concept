from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menus = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while 1:
    order_name = input(f"What would you like? {menus.get_items()}:").lower()
    if order_name == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order_name == 'off':
        break
    elif order_name == 'espresso' or order_name == 'latte' or order_name == 'cappuccino':
        menu_item = menus.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)





