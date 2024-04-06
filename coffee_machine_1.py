
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
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

def report():
    global wa
    global mi
    global co
    global mo
    wa=wa-(MENU[inp]["ingredients"]["water"])
    mi=mi-(MENU[inp]["ingredients"]["milk"])
    co=co-(MENU[inp]["ingredients"]["coffee"])
    mo=mo+(MENU[inp]["cost"])
    print(f"Water: {wa}ml")
    print(f"Milk: {mi}ml")
    print(f"Coffee: {co}g")
    print(f"Money: ${mo}")
    print()

def process_coin():
    global wa
    global mi
    global co
    global mo
    quarters =0.25
    dimes =0.10
    nickles =0.05
    pennies =0.01
    print("Insert coins. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies. ")
    print()
    coin_quarter=int(input("Insert the number of quarters:"))
    coin_dimes=int(input("Insert the number of dimes:"))
    coin_nickel=int(input("Insert the number of nickel:"))
    coin_pennies=int(input("Insert the number of pennies:"))
    total=coin_quarter*quarters+coin_dimes*dimes+coin_nickel*nickles+coin_pennies*pennies
    if total > MENU[inp]["cost"]:
        print()
        print(f"Here is your {inp}. Enjoy!")
        print()
        print(f"Report after purchasing {inp}:")
        '''
        wa=wa-(MENU[inp]["ingredients"]["water"])
        mi=mi-(MENU[inp]["ingredients"]["milk"])
        co=co-(MENU[inp]["ingredients"]["coffee"])
        mo=mo+(MENU[inp]["cost"])
        print(f"Water: {wa}ml")
        print(f"Milk: {mi}ml")
        print(f"Coffee: {co}g")
        print(f"Money: ${mo}")
        print()
        '''
        report()
        print(f'Here is ${round(total-MENU[inp]["cost"],2)} dollars in change.')
    elif total < MENU[inp]["cost"]:
        print()
        print("Sorry that's not enough money. Money refunded.")
        print()
        print(f"Report after purchasing {inp}:")
        print(f"Water: {wa}ml")
        print(f"Milk: {mi}ml")
        print(f"Coffee: {co}g")
        print(f"Money: ${mo}")
        print()
        print()
    else:
        print()
        print(f"Here is your {inp}. Enjoy!")
        print()
        print(f"Report after purchasing {inp}:")
        '''
        wa=wa-(MENU[inp]["ingredients"]["water"])
        mi=mi-(MENU[inp]["ingredients"]["milk"])
        co=co-(MENU[inp]["ingredients"]["coffee"])
        mo=mo+(MENU[inp]["cost"])
        print(f"Water: {wa}ml")
        print(f"Milk: {mi}ml")
        print(f"Coffee: {co}g")
        print(f"Money: ${mo}")
        print()
        '''
        report()


def resource_check():
    global wa
    global mi
    global co
    global mo
    p=0
    if wa>=(MENU[inp]["ingredients"]["water"]):
        p=p+1
    else:
        print()
        print(f'Sorry there is not enough water.')
    if mi>=(MENU[inp]["ingredients"]["milk"]):
        p=p+1
    else:
        print()
        print(f'Sorry there is not enough milk.')
    if co>=(MENU[inp]["ingredients"]["coffee"]):
        p=p+1
    else:
        print()
        print(f'Sorry there is not enough coffee.')
    if p==3:
        process_coin()
 
  
wa=resources['water']
mi=resources['milk']
co=resources['coffee']
mo=0
  
while(True): 
    print(r'''
     )  (
     (   ) )
      ) ( (
    __)____)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'
    ''')
    print("Type off to turn off the coffee machine. ")
    print()
    print(f"Report before purchasing :")
    print(f"Water: {wa}ml")
    print(f"Milk: {mi}ml")
    print(f"Coffee: {co}g")
    print(f"Money: ${mo}")
    print()
    inp=input("What would you like? (espresso/latte/cappuccino): ")
    if inp=='off':
        break
    elif inp=='espresso' or inp=='latte' or inp=='cappuccino':
        print()
        resource_check()
        print()
    










