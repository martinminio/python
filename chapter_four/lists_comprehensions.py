## Gerating a list in just one line of code using for loop and the creation of new elements and their insertion into the list
squares = [value**2 for value in range(1,11)]
print(squares)

# Generating pairs of numbers
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]
print(pairs)

