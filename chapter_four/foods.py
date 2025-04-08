# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# this is to show how each list keeps track of each person's favorite foods

my_foods.append('cannoli')
friend_foods.append('ice-cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# try it yourself section exercises
print("\nMy favorite foods are:")
for food in my_foods:
    print(food.title())
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food.title())

