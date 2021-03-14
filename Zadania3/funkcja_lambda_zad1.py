"""
Napisz funkcję lambda, która sprawdzi czy liczba jest parzysta czy nie
"""

def is_even(number):
    return number % 2 == 0

print(is_even(10))
print(is_even(3))

is_even2 = lambda x: x % 2 == 0

print(is_even2(10))
print(is_even2(3))
