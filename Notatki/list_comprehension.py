numbers = [1, 2, 3, 4]
new_numbers = []

for number in numbers:
    new_numbers.append(number ** 3)

print(new_numbers)

new_numbers2 = [number ** 3 for number in numbers if number < 3]
print(new_numbers2)

numbers = [1, 2, 3, 4, 4, 3, 2]

new_set = {number for number in numbers}
print(new_set)
print(type(new_set))

dictionary = {"name": "Jan", "surname": "Kowalski"}
print(dictionary["name"])
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

new_dictionary = {value: key for key, value in dictionary.items()}
print(new_dictionary)
print(new_dictionary.keys())

# Krotka
krotka = (1, 2, 3, 4, 5)
print(krotka)

krotka = 1, 2, 3, 4, 5
print(krotka)

owoc = "banan",
print(owoc)
print(type(owoc))

