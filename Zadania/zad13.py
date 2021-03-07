"""
13. Pliki. Stwórz program, który stworzy plik i wypisze do niego
a)liczby od 0 do 10, każda w nowej linii
b)tabliczkę mnożenia 10 x 10

"""
# a)
# with open("plik3.txt", "a", encoding="UTF-8") as f:
#     for number in range(11):
#         f.write(str(number) + '\n')

# b)
with open("plik3.txt", "w", encoding="UTF-8") as f:
    for number in range(1, 11):
        for number2 in range(1, 11):
            print(f"{number} X {number2} = {number * number2}")
            line = f"{number} X {number2} = {number * number2} \n"
            f.write(line)
