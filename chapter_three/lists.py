bicycles = ['trek', 'cannondale', 'dale', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[1].title())
print(bicycles[-1].upper())
message = f"\n\n My first bike was a {bicycles[0].title()}"
print(message)

## Modifying Elements in a List

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

## Adding elements to a List
    # append()
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
    # insert()
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

## Removing elements of a List
    # "del" Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

    # pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)

    # by value
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('honda')
print(motorcycles)