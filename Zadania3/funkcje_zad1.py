"""
Przygotuj prosty kalkulator (dodawanie, odejmowanie). Użytkownik powinien mieć możliwość wyboru działania i podania dwóch liczb.
"""

# Stałe
OPTION_ADD = 1
OPTION_SUBTRACT = 2
OPTION_EXIT = 3
OPTION_DIVISION = 4


def add(number_1, number_2):
    return number_1 + number_2


def subtract(number_1, number_2):
    return number_1 - number_2


def division(number_1, number_2):
    return number_1 / number_2


if __name__ == '__main__':

    while True:
        print("Wybierz opcję: \n 1: dodawanie \n 2: odejmowanie \n 3:Wyjście \n 4:Dzielenie")

        try:
            choice = int(input())

            if choice == OPTION_ADD:
                user_number_1 = float(input("Podaj liczbę..."))
                user_number_2 = float(input("Podaj liczbę..."))
                result = add(user_number_1, user_number_2)
                print(f"Wynik: {result}")

            elif choice == OPTION_SUBTRACT:
                user_number_1 = float(input("Podaj liczbę..."))
                user_number_2 = float(input("Podaj liczbę..."))
                result = subtract(user_number_1, user_number_2)
                print(f"Wynik: {result}")

            elif choice == OPTION_DIVISION:
                user_number_1 = float(input("Podaj liczbę..."))
                user_number_2 = float(input("Podaj liczbę..."))
                result = division(user_number_1, user_number_2)
                print(f"Wynik: {result}")

            elif choice == OPTION_EXIT:
                break
            else:
                print("Nieprawidłowa opcja")

        # wszystkie bledy

        except ValueError:
            print("Nieprawidłowa wartość")
        except ZeroDivisionError:
            print("Nie dziel przez zero")
        except:
            print("Bład")
