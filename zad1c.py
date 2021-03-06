"""
c) Napisz program, w którym zostanie wyliczony koszt zamówienia książek.
Użytkownik podaje ilość zamówionych książek, program wypisuje koszt.
Założenia:
- koszt jednej ksiązki przy zakupie powyżej 2000 ksiązek - 20zł
- koszt jednej ksiązki przy zakupie od 1000 do 2000 ksiązek - 25zł
- standardowa cena - 30zł
Wyliczanie kosztu zamówienia książek umieść w funkcji, która zwróci wynik (return).
Wynik zapisz do nowej zmiennej i wypisz na ekran.
"""


def get_price(book_number):
    if book_number > 2000:
        return 20
    elif book_number >= 1000:
        return 25
    else:
        return 30


if __name__ == '__main__':
    user_book_number = float(input("Podaj liczbę książek: "))

    cost = user_book_number * get_price(user_book_number)
    print(cost)
