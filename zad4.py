"""
Krotki.
Jesteś ankieterem, właśnie zebrałeś dane o ulubionych owocach ankietowanych.
Dane: "jabłko”, “banan”, “truskawka”, “banan”, “banan”, “truskawka”, “mango”, “kiwi”
a) Stwórz krotkę owoców z zebranych danych
b) Wyświetl całą krotkę
c) Wyświetl pierwszy i ostatni element krotki
d) Policz ile osób wybrało "truskawka" jako swój ulubiony owoc
e) Sprawdź czy owoc "mango" występuje w krotce
i) Stwórz nową krotkę zawierająca ulubione warzywa
j) Stwórz nową krotkę 'favourites', która będzie zawierać wszystkie owoce i warzywa
(połącz obie krotki)
"""

if __name__ == '__main__':
    # a) Stwórz krotkę owoców z zebranych danych
    fruits = ("jabłko", "banan", "truskawka", "banan", "banan", "truskawka", "mango", "kiwi")

    # b) Wyświetl całą krotkę
    print(fruits)

    # c) Wyświetl pierwszy i ostatni element krotki
    print(fruits[0], fruits[-1])

    # d) Policz ile osób wybrało "truskawka" jako swój ulubiony owoc
    print(fruits.count("truskawka"))

    # e) Sprawdź czy owoc "mango" występuje w krotce
    print("mango" in fruits)

    # i) Stwórz nową krotkę zawierająca ulubione warzywa
    vegetables = ("kalafior", "burak", "brokuł")

    # j) Stwórz nową krotkę 'favourites', która będzie zawierać wszystkie owoce i warzywa
    # (połącz obie krotki)
    favourites = fruits + vegetables
    print(favourites)
