"""
Mając listę liczby = [10,12, 30], stwórz nową tablicę liczb o podwojonej wartości.
z użyciem fora
z użyciem list comprehension
z użyciem map i stworzonej funkcji double()
z użyciem map i stworzonej funkcji lambda
"""

numbers = [10, 12, 30]

# z użyciem fora
new_numbers = []

for number in numbers:
    new_numbers.append(number * 2)

print(new_numbers)

# z użyciem list comprehension
new_numbers2 = [number * 2 for number in numbers]
print(new_numbers2)


# z użyciem map i stworzonej funkcji double()

def double(number):
    return number * 2


new_numbers3 = map(double, numbers)
print(list(new_numbers3))

# z użyciem map i stworzonej funkcji lambda

new_numbers4 = map(lambda number: number * 2, numbers)
print(list(new_numbers4))
