"""
Napisz program, który wczyta 2 liczby, wypisze większą z nich, obliczy ich sumę,
iloczyn i średnią
"""


def get_greater_number(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2


def calculate_sum(number1, number2):
    return number1 + number2


def calculate_avg(number1, number2):
    # 1 sposób
    avg_numbers = (number1 + number2) / 2
    # 2 sposób
    # avg_numbers = calculate_sum(number1, number2) / 2

    return avg_numbers


if __name__ == '__main__':
    number1 = float(input("Podaj liczbę: "))
    number2 = float(input("Podaj drugą liczbę: "))

    print("Większa liczba: ", get_greater_number(number1, number2))
    print(f'Większa liczba: {get_greater_number(number1, number2)}')

    sum_numbers = calculate_sum(number1, number2)
    print(f'Suma: {sum_numbers}')

    avg_numbers = calculate_avg(number1, number2)
    print(f'Średnia: {avg_numbers}')
