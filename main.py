from res import resources, MENU, make_coffee

while True:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == "report":
        print(f"""
        Water: {resources["water"]}ml
        Milk: {resources["milk"]}ml
        Coffee: {resources["coffee"]}g
        Money: ${resources["money"]}
        """)
    elif drink == "off":
        break
    else:
        if MENU[drink]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water")
        elif MENU[drink]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk")
        elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee")
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
            if money > MENU[drink]["cost"]:
                change = money - MENU[drink]["cost"]
                resources["money"] += MENU[drink]["cost"]
                print(f"Here is ${round(change, 2)} dollars in change.")
                make_coffee(drink)
            elif money == MENU[drink]["cost"]:
                resources["money"] += MENU[drink]["cost"]
                make_coffee(drink)
            else:
                print("Sorry that's not enough money. Money refunded.")