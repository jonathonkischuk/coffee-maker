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
water = 300
milk = 200
coffee = 100
print(f"You currently have {resources}.")
print(f"You can order from the following... {MENU}.")
order = input("From the above menu what would you like. Type 'e' for espresso, 'l' for latte, or 'c' for cappuccino: ").lower()
print("Thank you, please insert your coins.")
quarters = int(input("How many quarters? "))
quarter_value = quarters * 0.25
dimes = int(input("How many dimes? "))
dime_value = dimes * 0.10
nickles = int(input("How many nickles? "))
nickle_value = nickles * 0.05
pennies = int(input("How many pennies? "))
penny_value = pennies * 0.01
user_money = quarter_value + dime_value + nickle_value + penny_value
ordering = True
while ordering:
    if again == 'y':
        print(f"You have ${user_money} left.")
        again = input("Would you like anything else? Type y or n. ")
        ordering = True
        if order == 'e':
            order = 'espresso'
            cost = 1.50
            if user_money >= cost:
                if water >= MENU[order]['ingredients']['water']:
                    if coffee >= MENU[order]['ingredients']['coffee']:
                        user_money = round(user_money - cost, 2)
                        water = water - 50
                        coffee = coffee - 18
                        print("Here is your espresso, please enjoy.")
                    else:
                        print("Sorry, there is not enough coffee left.")
                        ordering = False
                else:
                    print("Sorry, there is not enough water left.")
                    ordering = False
            else:
                print("Sorry, that is not enough money.")
                ordering = False
        elif order == 'l':
            order = 'latte'
            cost = 2.50
            if user_money >= cost:
                if water >= MENU[order]['ingredients']['water']:
                    if coffee >= MENU[order]['ingredients']['coffee']:
                        if milk >= MENU[order]['ingredients']['milk']:
                            user_money = round(user_money - cost, 2)
                            water = water - 200
                            coffee = coffee - 24
                            milk = milk - 150
                            print("Here is your latte, please enjoy.")
                        else:
                            print("Sorry, there is not enough milk left.")
                            ordering = False
                    else:
                        print("Sorry, there is not enough coffee left.")
                        ordering = False
                else:
                    print("Sorry, there is not enough water left.")
                    ordering = False
            else:
                print("Sorry, that is not enough money.")
                ordering = False
        elif order == 'c':
            order = 'cappuccino'
            cost = 3.00
            if user_money >= cost:
                if water >= MENU[order]['ingredients']['water']:
                    if coffee >= MENU[order]['ingredients']['coffee']:
                        if milk >= MENU[order]['ingredients']['milk']:
                            user_money = round(user_money - cost, 2)
                            water = water - 250
                            coffee = coffee - 24
                            milk = milk - 100
                            print("Here is your cappuccino, please enjoy.")
                        else:
                            print("Sorry, there is not enough milk left.")
                            ordering = False
                    else:
                        print("Sorry, there is not enough coffee left.")
                        ordering = False
                else:
                    print("Sorry, there is not enough water left.")
                    ordering = False
            else:
                print("Sorry, that is not enough money.")
                ordering = False
        else:
            print("That is an invalid order... Sorry!")
        order = input("From the above menu what would you like. Type 'e' for espresso, 'l' for latte, or 'c' for cappuccino: ").lower()
    else:
        ordering = False
        print("Have a great day!")

