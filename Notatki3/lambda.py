def double(number):
    return number * 2


print(double(3))
print(double(4))

# Lambda - funkcja anonimowa


double2 = lambda x: x * 2

print(double2(3))
print(double2(4))
# print(double2(4, 3))
multiply = lambda x, y, z: x * y
print(multiply(4, 3, 2))

numbers = [1, 2, 3, 4, 5]

# Opcja
new_numbers = [number * 2 for number in numbers]
print(new_numbers)

# map
new_numbers = map(lambda x: x * 2, numbers)
print(list(new_numbers))

new_numbers = map(double, numbers)
print(list(new_numbers))



numbers = [1, 2, 3, 4, 5]
numbers_greater_than_3 = filter(lambda x: x > 3, numbers)
print(list(numbers_greater_than_3))


def greater_than_3(number):
    return number > 3


numbers_greater_than_3 = filter(greater_than_3, numbers)
print(list(numbers_greater_than_3))

# List comprehension

numbers = [1, 2, 3, 4, 5]
numbers_greater_than_3 = [number for number in numbers if number > 3]
print(numbers_greater_than_3)

numbers = [1, 2, 3, 4, 5]
new_numbers = []

for number in numbers:
    if number > 3:
        new_numbers.append(number)

print(new_numbers)
