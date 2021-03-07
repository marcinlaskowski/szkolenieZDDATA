"""11. List comprehension. Na podstawie listy zawierającej
 liczby od 1 do 10 utwórz nową, która będzie zawierać
liczbę powiększone o 2. Użyj do tego ‘List comprehension’."""
# 1
numbers = [number + 2 for number in range(1, 11)]
print(numbers)

# 2
numbers = list(range(1, 11))
new_numbers = [number + 2 for number in numbers]
