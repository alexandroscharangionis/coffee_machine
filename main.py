MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    '''Returns True if order can be prepared with existing resources, False if not enough resources'''
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Not enough {item}")
            return False
    return True


def process_coins():
    '''Takes coins and returns total amount of money inserted'''
    print("Please insert coins")
    total = int(input("How many quarters?\n")) * 0.25  # value of 1 quarter
    total += int(input("How many dimes?\n")) * 0.1  # value of 1 dime
    total += int(input("How many nickels?\n")) * 0.05  # value of 1 nickel
    total += int(input("How many pennies?\n")) * 0.01  # value of 1 penny
    return total


def is_transaction_successful(payment_received, drink_cost):
    '''Return True if payment is accepted, or False if money is insufficient.'''
    if payment_received >= drink_cost:
        change = round(payment_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += payment_received
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


coffee_machine_is_on = True

while coffee_machine_is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) ")
    if choice == "off":
        coffee_machine_is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])
