result = 4
print("Is result == 4? I predict True.")
print(result == 4)

result_bis = 3
print ("Is result_bis greater than 4? I predict false")
print(result_bis > 4)

# testing equality and inequality with strings
print("\ntesting equality and inequality with strings\n")
name = "martin"
print ("Is my name martin? I predict True")
print(name == "martin")

name = "martin"
print ("Is my name marcos? I predict False")
print(name == "marcos")

# testing using the lower() method

print("\ntesting using the lower() method\n")
name = "Martin"
print("Is my name Martin? I predict True")
print(name == "Martin")
print("Is my name martin? I predict False")
print(name == "martin")

# testing the use of "and" and "or"

print("\ntesting the use of 'and' and 'or'\n")
name = "martin"
age = 31
print("is my name martin and my age 31? I predict True")
print(name == "martin" and age == 31)
print("is my name martin and my age 30? I predict False")
print(name == "martin" and age == 30)

print("is my name martin or my age 31? I predict True")
print(name == "martin" or age == 31)
print("is my name martin or my age 30? I predict True")
print(name == "martin" or age == 30)
print("is my name marcos or my age 30? I predict False")
print(name == "marcos" or age == 30)

# testing whether an item is in a list
print("\ntesting whether an item is in a list\n")
list = ["martin", "marcos", "julieta", "ivan"]
print("Is martin in the list? I predict True")
print("martin" in list)

# testing whether an item is not in a list
print("\ntesting whether an item is not in a list\n")
list = ["martin", "marcos", "julieta", "ivan"]
print("Mariela is not in the list? I predict True")
print("mariela" not in list)