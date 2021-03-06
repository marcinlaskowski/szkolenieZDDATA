"""
Dane: "jabłko”, “banan”, “truskawka”, “banan”, “banan”, “truskawka”, “mango”, “kiwi”
a) Stwórz listę owoców z zebranych danych
b) Do listy dodaj swój ulubiony owoc (użyj odpowiedniej funkcji, aby dodać element na listę)  - append
c) Wyświetl całą listę
d) Wyświetl pierwszy i ostatni element listy
e) Policz ile osób wybrało "banan" jako swój ulubiony owoc - count
f) Sprawdź czy owoc "kiwi" występuje na liście  - in
g) Usuń z listy pierwszy element (użyj odpowiedniej funkcji, aby usunąć element)
h) Stwórz nową listę zawierająca ulubione warzywa
i) Stwórz nową listę 'favourites', która będzie zawierać wszystkie owoce i warzywa (połącz obie listy) - +
"""

if __name__ == '__main__':
    # a) Stwórz listę owoców z zebranych danych
    fruits = ["jabłko", "banan", "truskawka", "banan", "banan", "truskawka", "mango", "kiwi"]

    # b) Do listy dodaj swój ulubiony owoc (użyj odpowiedniej funkcji, aby dodać element na listę)  - append
    fruits.append("kiwi")

    # c) Wyświetl całą listę
    print(fruits)

    # d) Wyświetl pierwszy i ostatni element listy
    print(fruits[0])
    print(fruits[-1])

    # e) Policz ile osób wybrało "banan" jako swój ulubiony owoc - count
    print(fruits.count("banan"))

    # f) Sprawdź czy owoc "kiwi" występuje na liście  - in
    print("kiwi" in fruits)

    # g) Usuń z listy pierwszy element (użyj odpowiedniej funkcji, aby usunąć element)
    del fruits[0]
    print(fruits)

    # h) Stwórz nową listę zawierająca ulubione warzywa
    vegetables = ["marchewka", "burak", "ziemniak"]

    # i) Stwórz nową listę 'favourites', która będzie zawierać wszystkie owoce i warzywa (połącz obie listy) - +
    favourites = fruits + vegetables
    print(vegetables)
