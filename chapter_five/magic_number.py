## evaluando desigualdad 
answer= 17
if answer != 42:
    print("This is not the correct answer. Please try again!")

## condiciones con and
print("condiciones con and")
age_0 = 18
age_1 = 22

test_result = age_0 >= 21 and age_1 >= 21
print(test_result)

age_0 = 23
test_result = age_0 >= 21 and age_1 >= 21
print(test_result)

## condiones con or
age_0 = 18
age_1 = 22

print("condiciones con or")
test_result = age_0 >= 21 or age_1 >= 21
print(test_result)

age_0 = 18
age_1 = 17

test_result = age_0 >= 21 or age_1 >= 21
print(test_result)
