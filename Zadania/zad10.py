"""
10.
Pętle. Stwórz program, w którym użytkownik będzie zgadywał wylosowaną
przez program liczbę. Program powinien wylosować liczbę z zakresu 1-10,
następnie dać możliwość użytkownikowi zgadywania, aż do momentu podania
prawidłowej liczby.
"""
import random

if __name__ == "__main__":
    random_number = random.randint(1, 10)

    while True:
        user_number = int(input("Podaj liczbę:"))

        if random_number == user_number:
            print("Gratulacje!")
            break


