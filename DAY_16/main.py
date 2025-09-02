from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# initializing the class or creating an object
coffeemaker = CoffeeMaker()
menu = Menu()
moneymachine = MoneyMachine()

game = True
while game:
    print("items", menu.get_items())

    order_name = input("what kind of coffee you want \n (espresso/latte/cappuccino):")
    if order_name == "off":
        game = False
    elif order_name == "report":  # it gives the report for resorces left
        coffeemaker.report()
    else:
        drink = menu.find_drink(order_name)
        print("drink", drink.name, drink.cost, drink.ingredients)
        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
