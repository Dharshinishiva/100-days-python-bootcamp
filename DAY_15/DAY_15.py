# CREATING A COFFEE MACHINE

MENU = {
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18, "milk": 80},
        "cost": 1.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

profit = 0  # no money collected yet

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if (
            order_ingredients[item] > resources[item]
        ):  #  it compares the required ingredients with the resorces eg. 200(required) > 100(current resource)
            print(f"sorry!! there is no enough {item}")
            return False
    return True  # returns true if the resource is sufficient


def process_coin():
    print("insert the coin")
    total = int(input("enter the number of quarter:  ")) * 0.25
    total += int(input("enter the number of dimes:  ")) * 0.1
    total += int(input("enter the number of nickles:  ")) * 0.05
    total += int(input("enter the number of pennies:  ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in charge.")
        global profit
        profit += drink_cost
        return True
    else:
        print("There is no enough money. Money refunded ")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[
            item
        ]  # this line tells the resources left by subracting the items in resouces by items in current coffee
    print(f"here is your {drink_name}")
    print("\n" * 20)


game = True
while game:
    choice = input("what kind of coffee you want \n (espresso/latte/cappuccino):")
    if choice == "off":
        game = False
    elif choice == "report":  # it gives the report for resorces left
        print(f"Water: {resources['water']} ml")
        print(f"Milk:  {resources['milk']}ml")
        print(f"Coffee:  {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        ingredients = drink["ingredients"]
        if is_resources_sufficient(ingredients):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
