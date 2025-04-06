## range()
for value in range(1,5):
    print(value)


for value in range(5):
    print(value)


numbers = list(range(1,11))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

###########
squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)

# min(), max(), sum()

numbers = list(range(10))
print(min(numbers))
print(max(numbers))
print(sum(numbers))