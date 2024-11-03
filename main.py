# Coffee Machine Requirements :
# 1. print Report
# 2. check resources sufficient
# 3. process coins
# 4. check transaction successful
# 5. make coffee

menu = {
  "espresso" : {
    "ingredients" : {
      "water" : 50,
      "coffee" : 18,
    },
    "cost" : 1.5,
  },
  "latte" : {
    "ingredients" : {
      "water" : 200,
      "milk" : 150,
      "coffee" : 24
    },
    "cost" : 2.5,
  },
  "cappuccino" : {
    "ingredients" : {
      "water" : 250,
      "milk" : 100,
      "coffee" : 24,
    },
    "cost" : 3.0,
  }
}

resources = {
  "water" : 300,
  "milk" : 200,
  "coffee" : 100,
  "money" : 0
}


def display_resources():
  for key, val in resources.items():
    if key in ["water", "milk"]:
       print(f"{key}: {val}ml")
    elif key == "coffee":
      print(f"{key}: {val}g")
    elif key == "money":
      print(f"{key}: ${val}")
    else:
       print(f"{key}: {val}")

def check_out(drink_price):
  print("Please insert coins.")
  quarters = int(input("How many quarters? (0.25$) : ")) * 0.25
  dimes = int(input("How many dimes? (0.10$) : ")) * 0.10
  nickles = int(input("How many nickles? (0.05$) : ")) * 0.05
  pennies = int(input("How many pennies? (0.01$) : ")) * 0.01
  costumer_paid = (quarters + dimes + nickles + pennies)
  if costumer_paid < drink_price:
    print("Sorry, your amount is not enough")
    return False
  else:
    chargee = costumer_paid - drink_price
    resources['money'] += drink_price
    print(f"Here is your Charge! {chargee}")

def make_drink(drink_name):
  drink = menu[drink_name]
  ingredients = drink['ingredients']
  drink_price = drink['cost']

  is_available = True
  for ingredient, amount in ingredients.items():
    if resources[ingredient] < amount:
      print(f"Sorry we dont have enough {ingredient}")
      is_available = False
  if not is_available:
    return False
  
  check_out(drink_price)

  for ingredient, amount in ingredients.items():
    resources[ingredient] -= amount

  print(f"here is your {drink_name}")

while True:
  user_input = input("What would you like? (espresso/latte/cappuccino):")
  if user_input == "report":
    display_resources()
  elif user_input == "latte":
    make_drink("latte")
  elif user_input == "espresso":
    make_drink("espresso")
  elif user_input == "cappuccino":
    make_drink("cappuccino")
    