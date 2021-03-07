"""
Zbiory. Program powinien umożliwić użytkownikowi podanie 3 liczb, z tych liczb program
musi utworzyć zbiór, następnie:
a) wypisać zawartość zbioru
b) podać najmniejszą i największą wartość ze zbioru
"""
if __name__ == '__main__':
    number1 = float(input("Podaj liczbę: "))
    number2 = float(input("Podaj liczbę: "))
    number3 = float(input("Podaj liczbę: "))

    numbers = {number1, number2, number3}
    # LUB
    # numbers = set()
    # numbers.add(number1)
    # numbers.add(number2)
    # numbers.add(number3)

    print(numbers)
    print(max(numbers))
    print(min(numbers))
