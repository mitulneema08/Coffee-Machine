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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def sufficient_resources(ingredient):
    """Checks if there are enough resources available to make coffee or not."""
    for item in ingredient:
        if ingredient[item] > resources[item]:
            print(f"Sorry...not sufficient {item} in machine.")
            return False
    return True


def take_money(coffee_cost):
    """Take the coins from the user and calculate the cost of coffee and return the change to the user."""
    global profit
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    money_inserted = (quarters * 0.25) + (dimes * .10) + (nickles * 0.05) + (pennies * 0.01)

    if money_inserted < coffee_cost:
        print("Not sufficient coins inserted...")
        return
    else:
        change_money = money_inserted - coffee_cost
        formatted_change_money = "{:.2f}".format(change_money)
        print(f"Here is your change ${formatted_change_money}.")
        print("Here is your coffee. Enjoy!")
        profit += coffee_cost
        return profit


def report():
    """Returns the status of resources available."""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g"


coffee_machine = 'on'

while coffee_machine == 'on':
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        coffee_machine = 'off'

    elif user_input == "report":
        print(f"{report()}")
        print(f"Money: ${profit}")

    elif user_input in ("espresso", "latte", "cappuccino"):
        drink = MENU[user_input]
        if sufficient_resources(drink["ingredients"]):
            take_money(drink["cost"])
            for reduce_item in drink["ingredients"]:
                resources[reduce_item] -= drink["ingredients"][reduce_item]

    else:
        print("Wrong input...")
