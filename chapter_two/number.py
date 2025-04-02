# underscore numbers => you can use underscores to group big numbers into chunks that are more readable
universe_age = 14_000_000_000

# when printing these numbers python will only print the digits, i.o no underscores
print(universe_age)

## Multiple Assignment

# with this mechanism you can assign multiple variables with their values
# rules to follow: the number of values must match the number of variables separated by commas
x, y , z = 0 , 1 , 2
print(x)
print(y)
print(z)

## Constants
# Python doesn't have built-in constant types but there's a convention to follow for this cases
# variables to be treated as constants must be name in CAPITAL letters

THIS_IS_A_CONSTANT = 3000
print(THIS_IS_A_CONSTANT)

