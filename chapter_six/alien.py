

# This script demonstrates basic dictionary usage in Python.
# It creates a dictionary representing an alien with a color attribute,
# and prints the value associated with the 'color' key.
# Useful for practicing dictionary creation and value access.

alien_0 = {'color': 'green'}
print(alien_0['color'])

# Practice: Adding new key-value pairs to a dictionary and printing the updated dictionary
alien_0['x-coordinate'] = 0
alien_0['y-coordinate'] = 25
print(alien_0)

# Practice: Creating an empty dictionary and adding key-value pairs individually.
# This demonstrates how to build a dictionary step by step and print the result.
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Practice: Moving the alien based on its speed.
# This demonstrates how to use conditional statements to update dictionary values.

alien_0 = {'x-coordinate': 0, 'y-coordinate': 25, 'speed': 'medium'}

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x-coordinate'] = alien_0['x-coordinate'] + x_increment
print(f"The alien has moved to {alien_0['x-coordinate']} in the x-axis")

# Practice: Removing a key-value pair from a dictionary using del.
# This demonstrates how to delete the 'speed' key from the alien_0 dictionary and print the updated dictionary.

del alien_0['speed']
print(alien_0)

