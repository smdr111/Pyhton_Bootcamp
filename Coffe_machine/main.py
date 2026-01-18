from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu =  Menu()
maker = CoffeeMaker()
money = MoneyMachine()

while True:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
       break
    elif choice == "report":
        maker.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if maker.is_resource_sufficient(drink):
            payment = money.make_payment(drink.cost)
            if payment:
                maker.make_coffee(drink)



