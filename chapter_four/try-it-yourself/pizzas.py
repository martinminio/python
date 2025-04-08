pizzas = ['muzzarella', 'napolitana', 'fugazzeta']

for pizza in pizzas:
    print(f"I like {pizza.title()} pizza")

print("I really love pizza")

# try it yourself section exercises
friend_pizzas = pizzas[:]
pizzas.append('verdeo')
friend_pizzas.append('caprese')

print(f"\n My pizzas are:\n")
for pizza in pizzas:
    print(pizza.title())


print(f"\n My friend's pizzas are:\n")
for pizza in friend_pizzas:
    print(pizza.title())

