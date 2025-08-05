toppings = ['mushrooms', 'onions', 'pineapple']
print('onions' in toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish!\n")

########################################################
# Checking for special items in list
# Loop through the list of toppings and print a message for each one.
# If the topping is 'onions', print a message that onions are out of stock.
# Otherwise, print a message that the topping is being added to the pizza.

toppings = ['mushrooms', 'onions', 'pineapple']
for topping in toppings:
    if topping == "onions":
        print("Sorry, we're out of onions")
    else:
        print(f"Adding {topping} to your pizza")
print("We finished making your pizza!\n")        

## Checking a list is not empty
toppings = []

if toppings:
    for topping in toppings:
        if topping == "onions":
            print("Sorry, we're out of onions")
        else:
            print(f"Adding {topping} to your pizza")
    print("We finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?\n")        

## Using multiple lists
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping} to your pizza")
    else:
        print(f"Sorry, we don't have {requested_topping}")

print("We have finished your pizza!\n")


